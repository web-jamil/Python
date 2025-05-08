
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import math
import cmath
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import partial
import json
import os

class AdvancedCalculatorEngine:
    """Advanced calculator engine with multiple modes and functions"""
    def __init__(self):
        self.reset()
        self.mode = "scientific"  # scientific, programmer, matrix, graph
        self.angle_mode = "deg"  # deg or rad
        self.memory = {}
        self.user_functions = {}
        self.history = []
        self.settings = {
            "theme": "light",
            "precision": 10,
            "autosave": True
        }
        
    def reset(self):
        """Reset the calculator to initial state"""
        self.current_input = "0"
        self.stored_value = None
        self.operation = None
        self.reset_input = True
        self.last_operation = None
        self.matrix_buffer = None
        self.graph_equation = ""
        
    def save_state(self):
        """Save calculator state to file"""
        state = {
            "memory": self.memory,
            "user_functions": self.user_functions,
            "history": self.history[-20:],  # Save last 20 entries
            "settings": self.settings
        }
        with open("calculator_state.json", "w") as f:
            json.dump(state, f)
            
    def load_state(self):
        """Load calculator state from file"""
        try:
            with open("calculator_state.json", "r") as f:
                state = json.load(f)
                self.memory = state.get("memory", {})
                self.user_functions = state.get("user_functions", {})
                self.history = state.get("history", [])
                self.settings = state.get("settings", self.settings)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    
    def add_to_history(self, entry):
        """Add an entry to calculation history"""
        self.history.append(entry)
        if len(self.history) > 100:  # Keep last 100 entries
            self.history.pop(0)
        
        if self.settings["autosave"]:
            self.save_state()
    
    def evaluate_expression(self, expression):
        """Evaluate a mathematical expression string"""
        try:
            # Replace user functions and constants
            for func_name, func_def in self.user_functions.items():
                expression = expression.replace(func_name, f"({func_def})")
                
            # Replace constants
            expression = expression.replace("π", "math.pi")
            expression = expression.replace("e", "math.e")
            
            # Handle complex numbers
            expression = expression.replace("i", "j")
            
            # Evaluate safely
            result = eval(expression, {
                "__builtins__": None,
                "math": math,
                "cmath": cmath,
                "sin": math.sin if self.angle_mode == "rad" else lambda x: math.sin(math.radians(x)),
                "cos": math.cos if self.angle_mode == "rad" else lambda x: math.cos(math.radians(x)),
                "tan": math.tan if self.angle_mode == "rad" else lambda x: math.tan(math.radians(x)),
                "log": math.log10,
                "ln": math.log,
                "sqrt": math.sqrt,
                "abs": abs,
                "exp": math.exp
            }, {})
            
            return result
        except Exception as e:
            raise ValueError(f"Evaluation error: {str(e)}")
    
    def matrix_operation(self, operation, matrix1, matrix2=None):
        """Perform matrix operations"""
        try:
            if operation == "add":
                result = np.add(matrix1, matrix2)
            elif operation == "subtract":
                result = np.subtract(matrix1, matrix2)
            elif operation == "multiply":
                if matrix2 is None:
                    result = np.multiply(matrix1, matrix2)
                else:
                    result = np.dot(matrix1, matrix2)
            elif operation == "inverse":
                result = np.linalg.inv(matrix1)
            elif operation == "determinant":
                return np.linalg.det(matrix1)
            elif operation == "transpose":
                result = np.transpose(matrix1)
            elif operation == "eigenvalues":
                return np.linalg.eigvals(matrix1)
            else:
                raise ValueError("Unknown matrix operation")
                
            return result
        except Exception as e:
            raise ValueError(f"Matrix error: {str(e)}")
    
    def plot_function(self, expression, x_range=(-10, 10), num_points=100):
        """Plot a mathematical function"""
        try:
            x = np.linspace(x_range[0], x_range[1], num_points)
            y = []
            
            for x_val in x:
                try:
                    expr = expression.replace("x", f"({x_val})")
                    y_val = self.evaluate_expression(expr)
                    y.append(y_val)
                except:
                    y.append(np.nan)
            
            y = np.array(y)
            
            # Handle complex numbers
            if np.iscomplexobj(y):
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
                ax1.plot(x, np.real(y), label='Real part')
                ax1.set_title(f"Plot of {expression} (Real part)")
                ax1.grid(True)
                ax1.legend()
                
                ax2.plot(x, np.imag(y), label='Imaginary part')
                ax2.set_title(f"Plot of {expression} (Imaginary part)")
                ax2.grid(True)
                ax2.legend()
            else:
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.plot(x, y)
                ax.set_title(f"Plot of {expression}")
                ax.grid(True)
            
            return fig
        except Exception as e:
            raise ValueError(f"Plotting error: {str(e)}")

class AdvancedCalculatorUI(tk.Tk):
    """Advanced calculator GUI with multiple modes and features"""
    def __init__(self):
        super().__init__()
        self.title("Advanced Scientific Calculator")
        self.geometry("1000x800")
        self.engine = AdvancedCalculatorEngine()
        self.graph_figure = None
        self.graph_canvas = None
        
        # Load saved state
        self.engine.load_state()
        
        # Configure styles
        self.configure_styles()
        
        # Build UI
        self.create_widgets()
        
        # Set initial mode
        self.set_mode("scientific")
    
    def configure_styles(self):
        """Configure UI styles based on theme"""
        self.style = ttk.Style()
        
        if self.engine.settings["theme"] == "dark":
            self.style.theme_use('alt')
            self.configure(bg='#333333')
            self.style.configure('TFrame', background='#333333')
            self.style.configure('TLabel', background='#333333', foreground='white')
            self.style.configure('TButton', background='#444444', foreground='white')
            self.style.configure('Scientific.TButton', background='#555555', foreground='white')
            self.style.configure('Mode.TButton', background='#666666', foreground='white')
            self.style.configure('TEntry', fieldbackground='#222222', foreground='white')
        else:
            self.style.theme_use('clam')
            self.configure(bg='#f0f0f0')
            self.style.configure('TFrame', background='#f0f0f0')
            self.style.configure('TLabel', background='#f0f0f0', foreground='black')
            self.style.configure('TButton', background='#e0e0e0')
            self.style.configure('Scientific.TButton', background='#d0d0d0')
            self.style.configure('Mode.TButton', background='#c0c0c0')
    
    def create_widgets(self):
        """Create all UI widgets"""
        # Main container
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Display area
        self.create_display_area()
        
        # Mode selector
        self.create_mode_selector()
        
        # Main buttons
        self.create_main_buttons()
        
        # Scientific buttons (initially hidden)
        self.scientific_frame = ttk.Frame(self.main_frame)
        
        # Programmer mode buttons (initially hidden)
        self.programmer_frame = ttk.Frame(self.main_frame)
        
        # Matrix mode interface (initially hidden)
        self.matrix_frame = ttk.Frame(self.main_frame)
        
        # Graph mode interface (initially hidden)
        self.graph_frame = ttk.Frame(self.main_frame)
        self.create_graph_interface()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(
            self.main_frame, 
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.update_status()
    
    def create_display_area(self):
        """Create the calculator display area"""
        display_frame = ttk.Frame(self.main_frame)
        display_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Main display
        self.display_var = tk.StringVar(value="0")
        self.display = ttk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=('Consolas', 24),
            justify='right',
            state='readonly'
        )
        self.display.pack(fill=tk.X, ipady=10)
        
        # History display
        self.history_var = tk.StringVar()
        history_label = ttk.Label(
            display_frame,
            textvariable=self.history_var,
            font=('Consolas', 10),
            anchor='e'
        )
        history_label.pack(fill=tk.X)
    
    def create_mode_selector(self):
        """Create the mode selection buttons"""
        mode_frame = ttk.Frame(self.main_frame)
        mode_frame.pack(fill=tk.X, padx=5, pady=5)
        
        modes = [
            ("Scientific", "scientific"),
            ("Programmer", "programmer"),
            ("Matrix", "matrix"),
            ("Graph", "graph"),
            ("Settings", "settings")
        ]
        
        for text, mode in modes:
            btn = ttk.Button(
                mode_frame,
                text=text,
                style='Mode.TButton',
                command=partial(self.set_mode, mode)
            )
            btn.pack(side=tk.LEFT, expand=True)
    
    def create_main_buttons(self):
        """Create the main calculator buttons"""
        main_btn_frame = ttk.Frame(self.main_frame)
        main_btn_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button configuration for main calculator
        buttons = [
            ('C', 0, 0, partial(self.on_clear, 'C'), 1),
            ('CE', 0, 1, partial(self.on_clear, 'CE'), 1),
            ('⌫', 0, 2, self.on_backspace, 1),
            ('±', 0, 3, self.on_change_sign, 1),
            ('=', 0, 4, self.on_equals, 1),
            
            ('7', 1, 0, partial(self.on_digit, '7'), 1),
            ('8', 1, 1, partial(self.on_digit, '8'), 1),
            ('9', 1, 2, partial(self.on_digit, '9'), 1),
            ('÷', 1, 3, partial(self.on_operation, '/'), 1),
            ('^', 1, 4, partial(self.on_operation, '^'), 1),
            
            ('4', 2, 0, partial(self.on_digit, '4'), 1),
            ('5', 2, 1, partial(self.on_digit, '5'), 1),
            ('6', 2, 2, partial(self.on_digit, '6'), 1),
            ('×', 2, 3, partial(self.on_operation, '*'), 1),
            ('√', 2, 4, partial(self.on_scientific, 'sqrt'), 1),
            
            ('1', 3, 0, partial(self.on_digit, '1'), 1),
            ('2', 3, 1, partial(self.on_digit, '2'), 1),
            ('3', 3, 2, partial(self.on_digit, '3'), 1),
            ('-', 3, 3, partial(self.on_operation, '-'), 1),
            ('sin', 3, 4, partial(self.on_scientific, 'sin'), 1),
            
            ('0', 4, 0, partial(self.on_digit, '0'), 2),
            ('.', 4, 2, partial(self.on_digit, '.'), 1),
            ('+', 4, 3, partial(self.on_operation, '+'), 1),
            ('cos', 4, 4, partial(self.on_scientific, 'cos'), 1),
            
            ('(', 5, 0, partial(self.on_parenthesis, '('), 1),
            (')', 5, 1, partial(self.on_parenthesis, ')'), 1),
            ('π', 5, 2, partial(self.on_constant, 'π'), 1),
            ('e', 5, 3, partial(self.on_constant, 'e'), 1),
            ('tan', 5, 4, partial(self.on_scientific, 'tan'), 1),
            
            ('Hist', 6, 0, self.show_history, 1),
            ('Mem', 6, 1, self.show_memory, 1),
            ('Func', 6, 2, self.show_functions, 1),
            ('Deg/Rad', 6, 3, self.toggle_angle_mode, 1),
            ('Plot', 6, 4, self.prepare_plot, 1)
        ]
        
        # Create buttons in grid
        for (text, row, col, command, colspan) in buttons:
            btn = ttk.Button(
                main_btn_frame,
                text=text,
                command=command
            )
            if text in ['sin', 'cos', 'tan', '√', '^', 'π', 'e']:
                btn.configure(style='Scientific.TButton')
            btn.grid(
                row=row, 
                column=col, 
                columnspan=colspan,
                sticky='nsew', 
                padx=2, 
                pady=2
            )
        
        # Configure grid weights
        for i in range(7):
            main_btn_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            main_btn_frame.grid_columnconfigure(i, weight=1)
    
    def create_graph_interface(self):
        """Create the graphing interface components"""
        # Graph controls frame
        graph_controls = ttk.Frame(self.graph_frame)
        graph_controls.pack(fill=tk.X, pady=5)
        
        ttk.Label(graph_controls, text="y =").pack(side=tk.LEFT)
        
        self.graph_equation_var = tk.StringVar()
        graph_entry = ttk.Entry(
            graph_controls,
            textvariable=self.graph_equation_var,
            width=30
        )
        graph_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        plot_btn = ttk.Button(
            graph_controls,
            text="Plot",
            command=self.plot_current_equation
        )
        plot_btn.pack(side=tk.LEFT, padx=5)
        
        # Graph display area
        self.graph_display = ttk.Frame(self.graph_frame)
        self.graph_display.pack(fill=tk.BOTH, expand=True)
    
    def set_mode(self, mode):
        """Set the calculator mode"""
        self.engine.mode = mode
        
        # Hide all mode-specific frames
        self.scientific_frame.pack_forget()
        self.programmer_frame.pack_forget()
        self.matrix_frame.pack_forget()
        self.graph_frame.pack_forget()
        
        if mode == "scientific":
            pass  # Default buttons are already visible
        elif mode == "programmer":
            # Would add programmer-specific buttons here
            pass
        elif mode == "matrix":
            # Would add matrix operation buttons here
            pass
        elif mode == "graph":
            self.graph_frame.pack(fill=tk.BOTH, expand=True)
            self.graph_equation_var.set(self.engine.graph_equation)
        elif mode == "settings":
            self.show_settings()
        
        self.update_status()
    
    def plot_current_equation(self):
        """Plot the equation currently in the graph entry"""
        equation = self.graph_equation_var.get()
        if not equation:
            return
            
        try:
            # Clear previous graph
            for widget in self.graph_display.winfo_children():
                widget.destroy()
            
            # Create new plot
            fig = self.engine.plot_function(equation)
            self.graph_figure = fig
            
            # Embed in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self.graph_display)
            self.graph_canvas = canvas
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            # Update engine with current equation
            self.engine.graph_equation = equation
            self.engine.add_to_history(f"Plotted: {equation}")
            
        except ValueError as e:
            messagebox.showerror("Plot Error", str(e))
    
    def show_settings(self):
        """Show settings dialog"""
        settings_window = tk.Toplevel(self)
        settings_window.title("Calculator Settings")
        
        # Theme selection
        ttk.Label(settings_window, text="Theme:").grid(row=0, column=0, sticky='w')
        theme_var = tk.StringVar(value=self.engine.settings["theme"])
        ttk.Combobox(
            settings_window,
            textvariable=theme_var,
            values=["light", "dark"],
            state="readonly"
        ).grid(row=0, column=1, sticky='ew')
        
        # Precision setting
        ttk.Label(settings_window, text="Precision:").grid(row=1, column=0, sticky='w')
        precision_var = tk.IntVar(value=self.engine.settings["precision"])
        ttk.Spinbox(
            settings_window,
            from_=1,
            to=15,
            textvariable=precision_var
        ).grid(row=1, column=1, sticky='ew')
        
        # Autosave
        autosave_var = tk.BooleanVar(value=self.engine.settings["autosave"])
        ttk.Checkbutton(
            settings_window,
            text="Autosave settings and history",
            variable=autosave_var
        ).grid(row=2, column=0, columnspan=2, sticky='w')
        
        # Save button
        def save_settings():
            self.engine.settings = {
                "theme": theme_var.get(),
                "precision": precision_var.get(),
                "autosave": autosave_var.get()
            }
            self.configure_styles()
            settings_window.destroy()
            
        ttk.Button(
            settings_window,
            text="Save",
            command=save_settings
        ).grid(row=3, column=0, columnspan=2, pady=10)
        
        settings_window.columnconfigure(1, weight=1)
    
    def update_status(self):
        """Update the status bar"""
        status = f"Mode: {self.engine.mode.capitalize()}"
        if self.engine.mode == "scientific":
            status += f" | Angle: {self.engine.angle_mode}"
        self.status_var.set(status)

    # Placeholder methods for button actions
    def on_clear(self, clear_type):
        pass
    
    def on_backspace(self):
        pass
    
    def on_change_sign(self):
        pass
    
    def on_equals(self):
        pass
    
    def on_digit(self, digit):
        pass
    
    def on_operation(self, op):
        pass
    
    def on_scientific(self, func):
        pass
    
    def on_parenthesis(self, paren):
        pass
    
    def on_constant(self, const):
        pass
    
    def show_history(self):
        pass
    
    def show_memory(self):
        pass
    
    def show_functions(self):
        pass
    
    def toggle_angle_mode(self):
        pass
    
    def prepare_plot(self):
        pass

if __name__ == "__main__":
    app = AdvancedCalculatorUI()
    app.mainloop()