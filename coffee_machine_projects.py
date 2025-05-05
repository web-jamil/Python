import json
import logging
import hashlib
import getpass  # For secure password input
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum, auto

# Set up logging
logging.basicConfig(filename='coffee_machine.log', level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

class UserRole(Enum):
    CUSTOMER = auto()
    STAFF = auto()
    ADMIN = auto()

class User:
    def __init__(self, username, password_hash, role=UserRole.CUSTOMER):
        self.username = username
        self.password_hash = password_hash
        self.role = role
    
    def verify_password(self, password):
        return self.password_hash == self._hash_password(password)
    
    @staticmethod
    def _hash_password(password):
        """Secure password hashing using SHA-256 with salt"""
        salt = "coffee_machine_salt"  # In production, use unique salt per user
        return hashlib.sha256((password + salt).encode()).hexdigest()

class AuthenticationSystem:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.load_users()
    
    def load_users(self):
        try:
            with open('users.json', 'r') as f:
                users_data = json.load(f)
                for username, data in users_data.items():
                    self.users[username] = User(
                        username=username,
                        password_hash=data['password_hash'],
                        role=UserRole[data['role']]
                    )
        except (FileNotFoundError, json.JSONDecodeError):
            # Create default admin user if no users file exists
            admin = User("admin", User._hash_password("admin123"), UserRole.ADMIN)
            self.users["admin"] = admin
            self.save_users()
    
    def save_users(self):
        users_data = {
            username: {
                'password_hash': user.password_hash,
                'role': user.role.name
            }
            for username, user in self.users.items()
        }
        with open('users.json', 'w') as f:
            json.dump(users_data, f, indent=4)
    
    def login(self):
        print("\n=== COFFEE MACHINE LOGIN ===")
        while True:
            username = input("Username: ").strip()
            if not username:
                print("Username cannot be empty")
                continue
            
            password = getpass.getpass("Password: ").strip()
            if not password:
                print("Password cannot be empty")
                continue
            
            user = self.users.get(username)
            if user and user.verify_password(password):
                self.current_user = user
                logging.info(f"User {username} logged in")
                print(f"\nWelcome, {username}!")
                return True
            
            print("Invalid username or password")
            logging.warning(f"Failed login attempt for username: {username}")
            return False
    
    def logout(self):
        if self.current_user:
            logging.info(f"User {self.current_user.username} logged out")
            self.current_user = None
        print("Logged out successfully")
    
    def create_user(self, username, password, role=UserRole.CUSTOMER):
        if username in self.users:
            raise ValueError("Username already exists")
        if not username or not password:
            raise ValueError("Username and password cannot be empty")
        
        new_user = User(username, User._hash_password(password), role)
        self.users[username] = new_user
        self.save_users()
        logging.info(f"New user created: {username} ({role.name})")
        return new_user
    
    def change_password(self, username, new_password):
        if username not in self.users:
            raise ValueError("User not found")
        if not new_password:
            raise ValueError("Password cannot be empty")
        
        self.users[username].password_hash = User._hash_password(new_password)
        self.save_users()
        logging.info(f"Password changed for user: {username}")

class DrinkType(Enum):
    ESPRESSO = auto()
    LATTE = auto()
    CAPPUCCINO = auto()
    AMERICANO = auto()
    FLAT_WHITE = auto()

class Ingredient:
    def __init__(self, name, unit, current_level, max_capacity):
        self.name = name
        self.unit = unit
        self.current_level = current_level
        self.max_capacity = max_capacity
    
    def add(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.current_level + amount > self.max_capacity:
            excess = (self.current_level + amount) - self.max_capacity
            self.current_level = self.max_capacity
            return excess
        self.current_level += amount
        return 0
    
    def use(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.current_level:
            raise ValueError(f"Not enough {self.name}")
        self.current_level -= amount
    
    def __str__(self):
        return f"{self.name}: {self.current_level}{self.unit}"

class Recipe(ABC):
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost
    
    @abstractmethod
    def prepare(self):
        pass

class EspressoRecipe(Recipe):
    def __init__(self):
        ingredients = {
            'water': 50,
            'coffee': 18
        }
        super().__init__("Espresso", ingredients, 1.5)
    
    def prepare(self):
        print("Grinding coffee beans...")
        print("Extracting espresso shot...")
        print("Espresso ready!")

class LatteRecipe(Recipe):
    def __init__(self):
        ingredients = {
            'water': 200,
            'milk': 150,
            'coffee': 24
        }
        super().__init__("Latte", ingredients, 2.5)
    
    def prepare(self):
        print("Steaming milk...")
        print("Preparing espresso...")
        print("Combining milk and espresso...")
        print("Latte ready!")

class CappuccinoRecipe(Recipe):
    def __init__(self):
        ingredients = {
            'water': 250,
            'milk': 100,
            'coffee': 24
        }
        super().__init__("Cappuccino", ingredients, 3.0)
    
    def prepare(self):
        print("Steaming milk...")
        print("Preparing espresso...")
        print("Creating milk foam...")
        print("Cappuccino ready!")

class CoffeeMachineState(ABC):
    @abstractmethod
    def insert_money(self, machine, amount):
        pass
    
    @abstractmethod
    def select_drink(self, machine, drink_type):
        pass
    
    @abstractmethod
    def dispense_drink(self, machine):
        pass
    
    @abstractmethod
    def cancel(self, machine):
        pass

class IdleState(CoffeeMachineState):
    def insert_money(self, machine, amount):
        if amount <= 0:
            print("Amount must be positive")
            return
        machine.balance += amount
        machine.state = PaymentState()
        print(f"Balance: ${machine.balance:.2f}")
    
    def select_drink(self, machine, drink_type):
        print("Please insert money first")
    
    def dispense_drink(self, machine):
        print("No drink selected")
    
    def cancel(self, machine):
        print("No transaction to cancel")

class PaymentState(CoffeeMachineState):
    def insert_money(self, machine, amount):
        if amount <= 0:
            print("Amount must be positive")
            return
        machine.balance += amount
        print(f"Balance: ${machine.balance:.2f}")
    
    def select_drink(self, machine, drink_type):
        recipe = machine.recipes.get(drink_type)
        if not recipe:
            print("Invalid drink selection")
            return
        
        if machine.balance < recipe.cost:
            print(f"Please insert ${recipe.cost - machine.balance:.2f} more")
            return
        
        machine.selected_recipe = recipe
        machine.state = DispensingState()
        machine.dispense_drink()
    
    def dispense_drink(self, machine):
        print("Please select a drink first")
    
    def cancel(self, machine):
        print(f"Refunding ${machine.balance:.2f}")
        machine.balance = 0
        machine.state = IdleState()

class DispensingState(CoffeeMachineState):
    def insert_money(self, machine, amount):
        print("Please wait, your drink is being prepared")
    
    def select_drink(self, machine, drink_type):
        print("Please wait, your drink is being prepared")
    
    def dispense_drink(self, machine):
        try:
            # Check and use ingredients
            for ingredient, amount in machine.selected_recipe.ingredients.items():
                machine.inventory[ingredient].use(amount)
            
            # Prepare the drink
            machine.selected_recipe.prepare()
            
            # Calculate change
            change = machine.balance - machine.selected_recipe.cost
            if change > 0:
                print(f"Returning change: ${change:.2f}")
            
            # Update machine stats
            machine.balance = 0
            machine.total_sales += machine.selected_recipe.cost
            machine.drinks_served += 1
            logging.info(f"Served {machine.selected_recipe.name} for ${machine.selected_recipe.cost:.2f}")
            
            # Return to idle
            machine.state = IdleState()
            machine.selected_recipe = None
        
        except ValueError as e:
            print(f"Error: {str(e)}")
            print("Refunding money")
            machine.balance = 0
            machine.state = IdleState()
            machine.selected_recipe = None
    
    def cancel(self, machine):
        print("Cannot cancel during dispensing")

class CoffeeMachine:
    def __init__(self):
        self.inventory = {
            'water': Ingredient("Water", "ml", 1000, 2000),
            'milk': Ingredient("Milk", "ml", 500, 1000),
            'coffee': Ingredient("Coffee", "g", 200, 500)
        }
        
        self.recipes = {
            DrinkType.ESPRESSO: EspressoRecipe(),
            DrinkType.LATTE: LatteRecipe(),
            DrinkType.CAPPUCCINO: CappuccinoRecipe()
        }
        
        self.state = IdleState()
        self.balance = 0
        self.selected_recipe = None
        self.total_sales = 0
        self.drinks_served = 0
        self.maintenance_mode = False
    
    def insert_money(self, amount):
        self.state.insert_money(self, amount)
    
    def select_drink(self, drink_type):
        self.state.select_drink(self, drink_type)
    
    def dispense_drink(self):
        self.state.dispense_drink(self)
    
    def cancel(self):
        self.state.cancel(self)
    
    def report(self):
        print("\n=== MACHINE REPORT ===")
        for ingredient in self.inventory.values():
            print(ingredient)
        print(f"Total Sales: ${self.total_sales:.2f}")
        print(f"Drinks Served: {self.drinks_served}")
        print("=====================")
    
    def enter_maintenance(self):
        self.maintenance_mode = True
        print("\nMaintenance Mode Activated")
    
    def exit_maintenance(self):
        self.maintenance_mode = False
        print("Maintenance Mode Deactivated")
    
    def refill_ingredient(self, ingredient_name, amount):
        if not self.maintenance_mode:
            print("Must be in maintenance mode to refill")
            return
        
        if ingredient_name not in self.inventory:
            print("Invalid ingredient")
            return
        
        try:
            excess = self.inventory[ingredient_name].add(amount)
            if excess > 0:
                print(f"Warning: {excess}{self.inventory[ingredient_name].unit} of {ingredient_name} overflowed")
            else:
                print(f"{ingredient_name} refilled successfully")
        except ValueError as e:
            print(f"Error: {str(e)}")
    
    def save_state(self, filename):
        state = {
            'inventory': {
                name: {
                    'current': ing.current_level,
                    'max': ing.max_capacity
                }
                for name, ing in self.inventory.items()
            },
            'total_sales': self.total_sales,
            'drinks_served': self.drinks_served,
            'last_updated': datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, indent=4)
        
        print("Machine state saved successfully")
    
    def load_state(self, filename):
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            for name, data in state['inventory'].items():
                if name in self.inventory:
                    self.inventory[name].current_level = data['current']
                    self.inventory[name].max_capacity = data['max']
            
            self.total_sales = state.get('total_sales', 0)
            self.drinks_served = state.get('drinks_served', 0)
            print(f"Machine state loaded (last updated: {state.get('last_updated', 'unknown')})")
        
        except (FileNotFoundError, json.JSONDecodeError):
            print("No saved state found or invalid file - starting with default values")

class CoffeeMachineUI:
    def __init__(self, machine):
        self.machine = machine
        self.auth = AuthenticationSystem()
    
    def display_main_menu(self):
        print("\n==== MAIN MENU ====")
        print("1. Login")
        print("2. Exit")
    
    def display_drinks(self):
        print("\nAvailable Drinks:")
        for i, (drink_type, recipe) in enumerate(self.machine.recipes.items(), 1):
            print(f"{i}. {recipe.name} - ${recipe.cost:.2f}")
    
    def display_user_menu(self):
        print("\n==== COFFEE MACHINE ====")
        print("1. Insert Money")
        print("2. Select Drink")
        print("3. Dispense Drink")
        print("4. Cancel Transaction")
        
        if self.auth.current_user.role in [UserRole.STAFF, UserRole.ADMIN]:
            print("5. Machine Report")
        
        if self.auth.current_user.role == UserRole.ADMIN:
            print("6. Maintenance Menu")
            print("7. User Management")
        
        print("8. Logout")
    
    def user_management_menu(self):
        print("\n==== USER MANAGEMENT ====")
        print("1. Create New User")
        print("2. Change Password")
        print("3. List Users")
        print("4. Back to Main Menu")
    
    def maintenance_menu(self):
        print("\n==== MAINTENANCE MENU ====")
        print("1. Refill Water")
        print("2. Refill Milk")
        print("3. Refill Coffee")
        print("4. View Report")
        print("5. Exit Maintenance")
    
    def run(self):
        print("=== WELCOME TO COFFEE MACHINE ===")
        
        while True:
            if not self.auth.current_user:
                self.display_main_menu()
                choice = input("Enter your choice: ")
                
                if choice == '1':
                    if self.auth.login():
                        self.machine.load_state('coffee_machine_state.json')
                        self.user_loop()
                elif choice == '2':
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice")
            else:
                self.user_loop()
    
    def user_loop(self):
        while self.auth.current_user:
            self.display_user_menu()
            choice = input("Enter your choice: ")
            
            try:
                if choice == '1':
                    amount = float(input("Enter amount to insert: $"))
                    if amount <= 0:
                        print("Amount must be positive")
                        continue
                    self.machine.insert_money(amount)
                
                elif choice == '2':
                    self.display_drinks()
                    drink_choice = input("Select drink (or 'back' to cancel): ")
                    if drink_choice.lower() == 'back':
                        continue
                    
                    try:
                        drink_choice = int(drink_choice) - 1
                        drink_types = list(self.machine.recipes.keys())
                        if 0 <= drink_choice < len(drink_types):
                            self.machine.select_drink(drink_types[drink_choice])
                        else:
                            print("Invalid selection")
                    except ValueError:
                        print("Please enter a valid number")
                
                elif choice == '3':
                    self.machine.dispense_drink()
                
                elif choice == '4':
                    self.machine.cancel()
                
                elif choice == '5' and self.auth.current_user.role in [UserRole.STAFF, UserRole.ADMIN]:
                    self.machine.report()
                
                elif choice == '6' and self.auth.current_user.role == UserRole.ADMIN:
                    self.maintenance_loop()
                
                elif choice == '7' and self.auth.current_user.role == UserRole.ADMIN:
                    self.user_management_loop()
                
                elif choice == '8':
                    self.machine.save_state('coffee_machine_state.json')
                    self.auth.logout()
                
                else:
                    print("Invalid choice or insufficient permissions")
            
            except ValueError as e:
                print(f"Error: {str(e)}")
    
    def maintenance_loop(self):
        self.machine.enter_maintenance()
        
        while self.machine.maintenance_mode:
            self.maintenance_menu()
            choice = input("Enter choice: ")
            
            if choice == '1':
                self.handle_refill('water')
            elif choice == '2':
                self.handle_refill('milk')
            elif choice == '3':
                self.handle_refill('coffee')
            elif choice == '4':
                self.machine.report()
            elif choice == '5':
                self.machine.exit_maintenance()
            else:
                print("Invalid choice")
    
    def handle_refill(self, ingredient_name):
        try:
            amount = int(input(f"Enter amount of {ingredient_name} to add: "))
            if amount <= 0:
                print("Amount must be positive")
                return
            self.machine.refill_ingredient(ingredient_name, amount)
        except ValueError:
            print("Please enter a valid number")
    
    def user_management_loop(self):
        while True:
            self.user_management_menu()
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.handle_create_user()
            elif choice == '2':
                self.handle_change_password()
            elif choice == '3':
                self.display_user_list()
            elif choice == '4':
                break
            else:
                print("Invalid choice")
    
    def handle_create_user(self):
        username = input("Enter new username: ").strip()
        if not username:
            print("Username cannot be empty")
            return
        
        password = getpass.getpass("Enter password: ").strip()
        confirm = getpass.getpass("Confirm password: ").strip()
        
        if password != confirm:
            print("Passwords don't match!")
            return
        if not password:
            print("Password cannot be empty")
            return
        
        print("Select role:")
        print("1. Customer")
        print("2. Staff")
        print("3. Admin")
        role_choice = input("Enter role (1-3): ")
        
        roles = {
            '1': UserRole.CUSTOMER,
            '2': UserRole.STAFF,
            '3': UserRole.ADMIN
        }
        
        if role_choice in roles:
            try:
                self.auth.create_user(username, password, roles[role_choice])
                print(f"User {username} created successfully")
            except ValueError as e:
                print(str(e))
        else:
            print("Invalid role selection")
    
    def handle_change_password(self):
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty")
            return
        
        new_password = getpass.getpass("Enter new password: ").strip()
        confirm = getpass.getpass("Confirm new password: ").strip()
        
        if new_password != confirm:
            print("Passwords don't match!")
            return
        if not new_password:
            print("Password cannot be empty")
            return
        
        try:
            self.auth.change_password(username, new_password)
            print("Password changed successfully")
        except ValueError as e:
            print(str(e))
    
    def display_user_list(self):
        print("\n=== USER LIST ===")
        for username, user in self.auth.users.items():
            print(f"{username} - {user.role.name}")
        print("=================")

if __name__ == "__main__":
    machine = CoffeeMachine()
    ui = CoffeeMachineUI(machine)
    ui.run()