

import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple, Union
import threading
import time

# Enhanced logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('coffee_machine.log'),
        logging.StreamHandler()
    ]
)

class DrinkType(Enum):
    ESPRESSO = auto()
    LATTE = auto()
    CAPPUCCINO = auto()
    AMERICANO = auto()
    FLAT_WHITE = auto()
    MACCHIATO = auto()
    MOCHA = auto()
    HOT_WATER = auto()
    HOT_MILK = auto()
    CUSTOM = auto()  # Added for custom recipes

class Temperature(Enum):
    LOW = 140  # Fahrenheit
    MEDIUM = 160
    HIGH = 180
    EXTRA_HOT = 200

class Size(Enum):
    SMALL = 8  # oz
    MEDIUM = 12
    LARGE = 16

class Strength(Enum):
    MILD = 1
    MEDIUM = 2
    STRONG = 3

class Ingredient:
    def __init__(self, name: str, unit: str, current_level: float, max_capacity: float, 
                 alert_threshold: float = 0.2, expiry_days: Optional[int] = None):
        self.name = name
        self.unit = unit
        self.current_level = current_level
        self.max_capacity = max_capacity
        self.alert_threshold = alert_threshold
        self.expiry_date = datetime.now() + timedelta(days=expiry_days) if expiry_days else None
        self.last_refilled = datetime.now()
        
    def add(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.current_level + amount > self.max_capacity:
            excess = (self.current_level + amount) - self.max_capacity
            self.current_level = self.max_capacity
            self.last_refilled = datetime.now()
            return excess
        self.current_level += amount
        self.last_refilled = datetime.now()
        return 0
    
    def use(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.current_level:
            raise ValueError(f"Not enough {self.name}")
        self.current_level -= amount
    
    def is_low(self) -> bool:
        return self.current_level < (self.max_capacity * self.alert_threshold)
    
    def is_expired(self) -> bool:
        if self.expiry_date:
            return datetime.now() > self.expiry_date
        return False
    
    def __str__(self) -> str:
        status = f"{self.name}: {self.current_level:.1f}{self.unit}/{self.max_capacity}{self.unit}"
        if self.is_low():
            status += " (LOW)"
        if self.is_expired():
            status += " (EXPIRED)"
        return status

class Recipe(ABC):
    def __init__(self, name: str, ingredients: Dict[str, float], cost: float, 
                 prep_time: int = 30, default_temp: Temperature = Temperature.MEDIUM,
                 default_size: Size = Size.MEDIUM):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost
        self.prep_time = prep_time  # seconds
        self.default_temp = default_temp
        self.default_size = default_size
        
    @abstractmethod
    def prepare(self, temperature: Temperature, size: Size, strength: Strength) -> None:
        pass
    
    def get_adjusted_ingredients(self, size: Size) -> Dict[str, float]:
        size_factor = size.value / self.default_size.value
        return {ing: amount * size_factor for ing, amount in self.ingredients.items()}

class EspressoRecipe(Recipe):
    def __init__(self):
        ingredients = {
            'water': 50,
            'coffee': 18
        }
        super().__init__("Espresso", ingredients, 1.5, 25, Temperature.HIGH, Size.SMALL)
    
    def prepare(self, temperature: Temperature, size: Size, strength: Strength) -> None:
        print(f"Grinding coffee beans for {strength.name.lower()} strength...")
        print(f"Heating water to {temperature.value}°F...")
        print("Extracting espresso shot...")
        time.sleep(self.prep_time * (strength.value / 2))
        print("Espresso ready!")

class LatteRecipe(Recipe):
    def __init__(self):
        ingredients = {
            'water': 50,
            'milk': 150,
            'coffee': 18
        }
        super().__init__("Latte", ingredients, 2.5, 40, Temperature.MEDIUM, Size.MEDIUM)
    
    def prepare(self, temperature: Temperature, size: Size, strength: Strength) -> None:
        print(f"Grinding coffee beans for {strength.name.lower()} strength...")
        print(f"Steaming milk to {temperature.value}°F...")
        print("Preparing espresso...")
        time.sleep(self.prep_time * (strength.value / 2))
        print("Combining milk and espresso...")
        print("Latte ready!")

class CappuccinoRecipe(Recipe):
    def __init__(self):
        ingredients = {
            'water': 50,
            'milk': 100,
            'coffee': 18,
            'cocoa': 5
        }
        super().__init__("Cappuccino", ingredients, 3.0, 45, Temperature.MEDIUM, Size.MEDIUM)
    
    def prepare(self, temperature: Temperature, size: Size, strength: Strength) -> None:
        print(f"Grinding coffee beans for {strength.name.lower()} strength...")
        print(f"Steaming milk to {temperature.value}°F...")
        print("Preparing espresso...")
        time.sleep(self.prep_time * (strength.value / 2))
        print("Adding foam...")
        print("Cappuccino ready!")

class CustomRecipe(Recipe):
    def __init__(self, name: str, ingredients: Dict[str, float], cost: float):
        super().__init__(name, ingredients, cost)
    
    def prepare(self, temperature: Temperature, size: Size, strength: Strength) -> None:
        print(f"Preparing custom drink '{self.name}'...")
        print(f"Size: {size.name}, Temp: {temperature.value}°F, Strength: {strength.name}")
        time.sleep(self.prep_time)
        print(f"{self.name} ready!")

class CoffeeMachineState(ABC):
    @abstractmethod
    def insert_money(self, machine, amount: float) -> None:
        pass
    
    @abstractmethod
    def select_drink(self, machine, drink_type: DrinkType, 
                    temperature: Temperature, size: Size, strength: Strength) -> None:
        pass
    
    @abstractmethod
    def dispense_drink(self, machine) -> None:
        pass
    
    @abstractmethod
    def cancel(self, machine) -> None:
        pass
    
    @abstractmethod
    def maintenance(self, machine) -> None:
        pass

class IdleState(CoffeeMachineState):
    def insert_money(self, machine, amount: float) -> None:
        machine.balance += amount
        machine.state = PaymentState()
        print(f"Balance: ${machine.balance:.2f}")
        logging.info(f"Money inserted: ${amount:.2f}")
    
    def select_drink(self, machine, drink_type: DrinkType, 
                    temperature: Temperature, size: Size, strength: Strength) -> None:
        print("Please insert money first")
    
    def dispense_drink(self, machine) -> None:
        print("No drink selected")
    
    def cancel(self, machine) -> None:
        print("No transaction to cancel")
    
    def maintenance(self, machine) -> None:
        machine.enter_maintenance()

class PaymentState(CoffeeMachineState):
    def insert_money(self, machine, amount: float) -> None:
        machine.balance += amount
        print(f"Balance: ${machine.balance:.2f}")
        logging.info(f"Additional money inserted: ${amount:.2f}")
    
    def select_drink(self, machine, drink_type: DrinkType, 
                    temperature: Temperature, size: Size, strength: Strength) -> None:
        recipe = machine.get_recipe(drink_type, size)
        if not recipe:
            print("Invalid drink selection")
            return
        
        if machine.balance < recipe.cost:
            print(f"Please insert ${recipe.cost - machine.balance:.2f} more")
            return
        
        machine.selected_recipe = recipe
        machine.selected_temp = temperature
        machine.selected_size = size
        machine.selected_strength = strength
        machine.state = DispensingState()
        machine.dispense_drink()
    
    def dispense_drink(self, machine) -> None:
        print("Please select a drink first")
    
    def cancel(self, machine) -> None:
        print(f"Refunding ${machine.balance:.2f}")
        logging.info(f"Transaction canceled. Refunded: ${machine.balance:.2f}")
        machine.balance = 0
        machine.state = IdleState()
    
    def maintenance(self, machine) -> None:
        print("Please cancel transaction first")

class DispensingState(CoffeeMachineState):
    def insert_money(self, machine, amount: float) -> None:
        print("Please wait, your drink is being prepared")
    
    def select_drink(self, machine, drink_type: DrinkType, 
                    temperature: Temperature, size: Size, strength: Strength) -> None:
        print("Please wait, your drink is being prepared")
    
    def dispense_drink(self, machine) -> None:
        try:
            with machine._lock:
                # Check and use ingredients
                adjusted_ingredients = machine.selected_recipe.get_adjusted_ingredients(machine.selected_size)
                for ingredient, amount in adjusted_ingredients.items():
                    if ingredient not in machine.inventory:
                        raise ValueError(f"Ingredient '{ingredient}' not found in inventory")
                    if machine.inventory[ingredient].current_level < amount:
                        raise ValueError(f"Not enough {ingredient} (needed: {amount}, available: {machine.inventory[ingredient].current_level})")
                
                # Use the ingredients
                for ingredient, amount in adjusted_ingredients.items():
                    machine.inventory[ingredient].use(amount)
            
            # Prepare the drink in a separate thread
            def prepare_drink():
                machine.selected_recipe.prepare(
                    machine.selected_temp, 
                    machine.selected_size, 
                    machine.selected_strength
                )
                
                with machine._lock:
                    # Calculate change
                    change = machine.balance - machine.selected_recipe.cost
                    if change > 0:
                        print(f"Returning change: ${change:.2f}")
                    
                    # Update machine stats
                    machine.balance = 0
                    machine.total_sales += machine.selected_recipe.cost
                    machine.drinks_served += 1
                    logging.info(
                        f"Served {machine.selected_recipe.name} (Size: {machine.selected_size.name}, "
                        f"Temp: {machine.selected_temp.value}°F) for ${machine.selected_recipe.cost:.2f}"
                    )
                    
                    # Check if cleaning is needed
                    if machine.drinks_served % 10 == 0:
                        machine.cleaning_required = True
                        logging.warning("Machine needs cleaning")
                
                # Return to idle
                machine.state = IdleState()
                machine.selected_recipe = None
                machine.selected_temp = None
                machine.selected_size = None
                machine.selected_strength = None
            
            # Start drink preparation thread
            preparation_thread = threading.Thread(target=prepare_drink)
            preparation_thread.start()
        
        except ValueError as e:
            print(f"Error: {str(e)}")
            print("Refunding money")
            logging.error(f"Dispensing error: {str(e)}")
            machine.balance = 0
            machine.state = IdleState()
            machine.selected_recipe = None
            machine.selected_temp = None
            machine.selected_size = None
            machine.selected_strength = None
    
    def cancel(self, machine) -> None:
        print("Cannot cancel during dispensing")
    
    def maintenance(self, machine) -> None:
        print("Cannot enter maintenance during dispensing")

class CleaningState(CoffeeMachineState):
    def insert_money(self, machine, amount: float) -> None:
        print("Machine is being cleaned. Please wait.")
    
    def select_drink(self, machine, drink_type: DrinkType, 
                    temperature: Temperature, size: Size, strength: Strength) -> None:
        print("Machine is being cleaned. Please wait.")
    
    def dispense_drink(self, machine) -> None:
        print("Machine is being cleaned. Please wait.")
    
    def cancel(self, machine) -> None:
        print("No transaction to cancel during cleaning")
    
    def maintenance(self, machine) -> None:
        print("Already in maintenance mode")

class CoffeeMachine:
    def __init__(self):
        self._lock = threading.Lock()
        self.inventory = {
            'water': Ingredient("water", "ml", 1000, 2000),
            'milk': Ingredient("milk", "ml", 500, 1000, expiry_days=7),
            'coffee': Ingredient("coffee", "g", 200, 500),
            'sugar': Ingredient("sugar", "g", 300, 500),
            'cocoa': Ingredient("cocoa", "g", 100, 200, expiry_days=30),
            'vanilla': Ingredient("vanilla", "ml", 50, 100, expiry_days=60)
        }
        
        self.recipes = self._initialize_recipes()
        self.custom_recipes: List[Recipe] = []
        
        self.state: CoffeeMachineState = IdleState()
        self.balance: float = 0
        self.selected_recipe: Optional[Recipe] = None
        self.selected_temp: Optional[Temperature] = None
        self.selected_size: Optional[Size] = None
        self.selected_strength: Optional[Strength] = None
        
        self.total_sales: float = 0
        self.drinks_served: int = 0
        self.maintenance_mode: bool = False
        self.cleaning_required: bool = False
        self.cleaning_cycles: int = 0
        self.last_cleaned: Optional[datetime] = None
        
        # Start background monitoring thread
        self.monitor_thread = threading.Thread(target=self._monitor_machine, daemon=True)
        self.monitor_thread.start()
    
    def _initialize_recipes(self) -> Dict[DrinkType, Recipe]:
        return {
            DrinkType.ESPRESSO: EspressoRecipe(),
            DrinkType.LATTE: LatteRecipe(),
            DrinkType.CAPPUCCINO: CappuccinoRecipe(),
            DrinkType.AMERICANO: CustomRecipe("Americano", {'water': 200, 'coffee': 18}, 2.0),
            DrinkType.FLAT_WHITE: CustomRecipe("Flat White", {'water': 50, 'milk': 100, 'coffee': 18}, 2.5),
            DrinkType.MACCHIATO: CustomRecipe("Macchiato", {'water': 30, 'milk': 30, 'coffee': 18}, 2.0),
            DrinkType.MOCHA: CustomRecipe("Mocha", {'water': 50, 'milk': 100, 'coffee': 18, 'cocoa': 10}, 3.0),
            DrinkType.HOT_WATER: CustomRecipe("Hot Water", {'water': 250}, 0.5),
            DrinkType.HOT_MILK: CustomRecipe("Hot Milk", {'milk': 250}, 1.5)
        }
    
    def _monitor_machine(self) -> None:
        """Background thread to monitor machine status"""
        while True:
            time.sleep(60)  # Check every minute
            
            with self._lock:
                # Check for low ingredients
                low_ingredients = [ing.name for ing in self.inventory.values() if ing.is_low()]
                if low_ingredients:
                    logging.warning(f"Low ingredients: {', '.join(low_ingredients)}")
                
                # Check for expired ingredients
                expired_ingredients = [ing.name for ing in self.inventory.values() if ing.is_expired()]
                if expired_ingredients:
                    logging.error(f"Expired ingredients: {', '.join(expired_ingredients)}")
    
    def get_recipe(self, drink_type: DrinkType, size: Size) -> Optional[Recipe]:
        """Get recipe adjusted for size"""
        if drink_type == DrinkType.CUSTOM and self.custom_recipes:
            # For custom drinks, use the first one (UI should handle selection properly)
            recipe = self.custom_recipes[0]
        else:
            recipe = self.recipes.get(drink_type)
        
        if not recipe:
            return None
        
        # Create a temporary adjusted recipe
        adjusted_recipe = CustomRecipe(
            recipe.name,
            recipe.get_adjusted_ingredients(size),
            recipe.cost * (size.value / recipe.default_size.value)
        )
        return adjusted_recipe
    
    def insert_money(self, amount: float) -> None:
        if amount <= 0:
            print("Amount must be positive")
            return
        self.state.insert_money(self, amount)
    
    def select_drink(self, drink_type: DrinkType, 
                    temperature: Temperature = Temperature.MEDIUM,
                    size: Size = Size.MEDIUM,
                    strength: Strength = Strength.MEDIUM) -> None:
        if self.cleaning_required and not self.maintenance_mode:
            print("Machine needs cleaning. Please contact staff.")
            return
        self.state.select_drink(self, drink_type, temperature, size, strength)
    
    def dispense_drink(self) -> None:
        self.state.dispense_drink(self)
    
    def cancel(self) -> None:
        self.state.cancel(self)
    
    def report(self) -> None:
        with self._lock:
            print("\n=== MACHINE REPORT ===")
            print(f"Status: {'Maintenance' if self.maintenance_mode else 'Operational'}")
            print(f"Cleaning Needed: {'Yes' if self.cleaning_required else 'No'}")
            print(f"Last Cleaned: {self.last_cleaned.strftime('%Y-%m-%d %H:%M') if self.last_cleaned else 'Never'}")
            
            print("\nIngredients:")
            for ingredient in self.inventory.values():
                print(f"  {ingredient}")
                if ingredient.last_refilled:
                    print(f"    Last refilled: {ingredient.last_refilled.strftime('%Y-%m-%d %H:%M')}")
                if ingredient.expiry_date:
                    print(f"    Expires: {ingredient.expiry_date.strftime('%Y-%m-%d %H:%M')}")
            
            print("\nFinancial:")
            print(f"Total Sales: ${self.total_sales:.2f}")
            print(f"Drinks Served: {self.drinks_served}")
            print("=====================")
        logging.info("Machine report generated")
    
    def enter_maintenance(self) -> None:
        if isinstance(self.state, DispensingState):
            print("Cannot enter maintenance during dispensing")
            return
        
        self.maintenance_mode = True
        self.state = CleaningState()
        print("\nMaintenance Mode Activated")
        logging.info("Entered maintenance mode")
    
    def exit_maintenance(self) -> None:
        self.maintenance_mode = False
        self.state = IdleState()
        print("Maintenance Mode Deactivated")
        logging.info("Exited maintenance mode")
    
    def refill_ingredient(self, ingredient_name: str, amount: float) -> None:
        if not self.maintenance_mode:
            print("Must be in maintenance mode to refill")
            return
        
        if ingredient_name not in self.inventory:
            print("Invalid ingredient")
            return
        
        if amount <= 0:
            print("Amount must be positive")
            return
        
        with self._lock:
            excess = self.inventory[ingredient_name].add(amount)
            if excess > 0:
                print(f"Warning: {excess}{self.inventory[ingredient_name].unit} of {ingredient_name} overflowed")
            else:
                print(f"{ingredient_name} refilled successfully")
            logging.info(f"Refilled {ingredient_name} with {amount}{self.inventory[ingredient_name].unit}")
    
    def clean_machine(self) -> None:
        if not self.maintenance_mode:
            print("Must be in maintenance mode to clean")
            return
        
        print("Starting cleaning cycle...")
        time.sleep(10)  # Simulate cleaning time
        with self._lock:
            self.cleaning_required = False
            self.cleaning_cycles += 1
            self.last_cleaned = datetime.now()
        print("Cleaning complete!")
        logging.info("Machine cleaning completed")
    
    def add_custom_recipe(self, name: str, ingredients: Dict[str, float], cost: float) -> None:
        if not self.maintenance_mode:
            print("Must be in maintenance mode to add recipes")
            return
        
        # Validate ingredients
        for ing in ingredients:
            if ing not in self.inventory:
                print(f"Invalid ingredient: {ing}")
                return
        
        # Check for duplicate names
        if any(recipe.name.lower() == name.lower() for recipe in self.custom_recipes):
            print(f"Recipe with name '{name}' already exists")
            return
        
        if cost <= 0:
            print("Cost must be positive")
            return
        
        new_recipe = CustomRecipe(name, ingredients, cost)
        with self._lock:
            self.custom_recipes.append(new_recipe)
        print(f"Custom recipe '{name}' added successfully")
        logging.info(f"Added custom recipe: {name}")
    
    def save_state(self, filename: str) -> None:
        with self._lock:
            state = {
                'inventory': {
                    name: {
                        'current': ing.current_level,
                        'max': ing.max_capacity,
                        'last_refilled': ing.last_refilled.isoformat(),
                        'expiry_date': ing.expiry_date.isoformat() if ing.expiry_date else None
                    }
                    for name, ing in self.inventory.items()
                },
                'total_sales': self.total_sales,
                'drinks_served': self.drinks_served,
                'cleaning_cycles': self.cleaning_cycles,
                'last_cleaned': self.last_cleaned.isoformat() if self.last_cleaned else None,
                'last_updated': datetime.now().isoformat(),
                'custom_recipes': [
                    {
                        'name': recipe.name,
                        'ingredients': recipe.ingredients,
                        'cost': recipe.cost
                    }
                    for recipe in self.custom_recipes
                ]
            }
            
            with open(filename, 'w') as f:
                json.dump(state, f, indent=2)
        
        print("Machine state saved successfully")
        logging.info("Machine state saved")
    
    def load_state(self, filename: str) -> None:
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            with self._lock:
                for name, data in state['inventory'].items():
                    if name in self.inventory:
                        self.inventory[name].current_level = data['current']
                        self.inventory[name].max_capacity = data['max']
                        self.inventory[name].last_refilled = datetime.fromisoformat(data['last_refilled'])
                        if data['expiry_date']:
                            self.inventory[name].expiry_date = datetime.fromisoformat(data['expiry_date'])
                
                self.total_sales = state['total_sales']
                self.drinks_served = state['drinks_served']
                self.cleaning_cycles = state['cleaning_cycles']
                self.last_cleaned = datetime.fromisoformat(state['last_cleaned']) if state['last_cleaned'] else None
                
                # Load custom recipes
                self.custom_recipes = []
                for recipe_data in state.get('custom_recipes', []):
                    self.custom_recipes.append(
                        CustomRecipe(
                            recipe_data['name'],
                            recipe_data['ingredients'],
                            recipe_data['cost']
                        )
                    )
            
            print(f"Machine state loaded (last updated: {state['last_updated']})")
            logging.info("Machine state loaded")
        
        except FileNotFoundError:
            print("No saved state found - starting with default values")
        except Exception as e:
            print(f"Error loading state: {str(e)}")
            logging.error(f"Error loading state: {str(e)}")

class CoffeeMachineUI:
    def __init__(self, machine: CoffeeMachine):
        self.machine = machine
        self.running = True
    
    def display_menu(self) -> None:
        print("\n==== COFFEE MACHINE ====")
        print("1. Insert Money")
        print("2. Select Drink")
        print("3. Dispense Drink")
        print("4. Cancel Transaction")
        print("5. Machine Report")
        print("6. Maintenance Menu")
        print("7. Exit")
    
    def display_drinks(self) -> None:
        print("\nAvailable Drinks:")
        for i, (drink_type, recipe) in enumerate(self.machine.recipes.items(), 1):
            print(f"{i}. {recipe.name} - ${recipe.cost:.2f}")
        
        if self.machine.custom_recipes:
            print("\nCustom Drinks:")
            for i, recipe in enumerate(self.machine.custom_recipes, len(self.machine.recipes)+1):
                print(f"{i}. {recipe.name} - ${recipe.cost:.2f}")
    
    def display_options(self) -> None:
        print("\nDrink Options:")
        print("1. Temperature:")
        for i, temp in enumerate(Temperature, 1):
            print(f"   {i}. {temp.name} ({temp.value}°F)")
        
        print("2. Size:")
        for i, size in enumerate(Size, 1):
            print(f"   {i}. {size.name} ({size.value}oz)")
        
        print("3. Strength:")
        for i, strength in enumerate(Strength, 1):
            print(f"   {i}. {strength.name}")
    
    def run(self) -> None:
        self.machine.load_state('coffee_machine_state.json')
        
        while self.running:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            try:
                if choice == '1':
                    amount = float(input("Enter amount to insert: $"))
                    self.machine.insert_money(amount)
                
                elif choice == '2':
                    self.display_drinks()
                    drink_choice = int(input("Select drink: ")) - 1
                    
                    # Get all available recipes
                    all_recipes = list(self.machine.recipes.items())
                    if self.machine.custom_recipes:
                        all_recipes.extend([(None, r) for r in self.machine.custom_recipes])
                    
                    if 0 <= drink_choice < len(all_recipes):
                        self.display_options()
                        
                        # Get temperature
                        temp_choice = int(input("Select temperature (1-4): ")) - 1
                        temperature = list(Temperature)[temp_choice] if 0 <= temp_choice < len(Temperature) else Temperature.MEDIUM
                        
                        # Get size
                        size_choice = int(input("Select size (1-3): ")) - 1
                        size = list(Size)[size_choice] if 0 <= size_choice < len(Size) else Size.MEDIUM
                        
                        # Get strength
                        strength_choice = int(input("Select strength (1-3): ")) - 1
                        strength = list(Strength)[strength_choice] if 0 <= strength_choice < len(Strength) else Strength.MEDIUM
                        
                        drink_type, recipe = all_recipes[drink_choice]
                        if drink_type is not None:
                            self.machine.select_drink(drink_type, temperature, size, strength)
                        else:
                            # Handle custom recipe
                            temp_recipe = CustomRecipe(
                                recipe.name,
                                recipe.get_adjusted_ingredients(size),
                                recipe.cost * (size.value / Size.MEDIUM.value)
                            )
                            self.machine.selected_recipe = temp_recipe
                            self.machine.selected_temp = temperature
                            self.machine.selected_size = size
                            self.machine.selected_strength = strength
                            self.machine.state = DispensingState()
                            self.machine.dispense_drink()
                    else:
                        print("Invalid selection")
                
                elif choice == '3':
                    self.machine.dispense_drink()
                
                elif choice == '4':
                    self.machine.cancel()
                
                elif choice == '5':
                    self.machine.report()
                
                elif choice == '6':
                    self.maintenance_menu()
                
                elif choice == '7':
                    self.machine.save_state('coffee_machine_state.json')
                    print("Goodbye!")
                    self.running = False
                
                else:
                    print("Invalid choice")
            
            except ValueError as e:
                print(f"Invalid input: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                logging.error(f"UI error: {str(e)}")
    
    def maintenance_menu(self) -> None:
        self.machine.enter_maintenance()
        
        while self.machine.maintenance_mode:
            print("\n==== MAINTENANCE ====")
            print("1. Refill Ingredients")
            print("2. Clean Machine")
            print("3. Add Custom Recipe")
            print("4. View Report")
            print("5. Exit Maintenance")
            
            choice = input("Enter choice: ")
            
            try:
                if choice == '1':
                    print("\nAvailable Ingredients:")
                    for i, (name, ing) in enumerate(self.machine.inventory.items(), 1):
                        print(f"{i}. {ing}")
                    
                    ing_choice = int(input("Select ingredient to refill: ")) - 1
                    ingredient_names = list(self.machine.inventory.keys())
                    if 0 <= ing_choice < len(ingredient_names):
                        amount = float(input(f"Enter amount to add ({self.machine.inventory[ingredient_names[ing_choice]].unit}): "))
                        self.machine.refill_ingredient(ingredient_names[ing_choice], amount)
                    else:
                        print("Invalid selection")
                
                elif choice == '2':
                    if self.machine.cleaning_required:
                        print("Starting cleaning cycle...")
                        self.machine.clean_machine()
                    else:
                        print("Machine doesn't need cleaning yet")
                
                elif choice == '3':
                    name = input("Enter recipe name: ")
                    ingredients = {}
                    print("\nAvailable Ingredients:")
                    for i, (name, ing) in enumerate(self.machine.inventory.items(), 1):
                        print(f"{i}. {name} ({ing.unit})")
                    
                    while True:
                        ing_choice = input("Add ingredient (number) or 'done' to finish: ")
                        if ing_choice.lower() == 'done':
                            break
                        
                        try:
                            ing_num = int(ing_choice) - 1
                            if 0 <= ing_num < len(self.machine.inventory):
                                ing_name = list(self.machine.inventory.keys())[ing_num]
                                amount = float(input(f"Enter amount of {ing_name} ({self.machine.inventory[ing_name].unit}): "))
                                ingredients[ing_name] = amount
                            else:
                                print("Invalid number")
                        except ValueError:
                            print("Please enter a number or 'done'")
                    
                    if not ingredients:
                        print("No ingredients added")
                        continue
                    
                    cost = float(input("Enter drink cost: $"))
                    self.machine.add_custom_recipe(name, ingredients, cost)
                
                elif choice == '4':
                    self.machine.report()
                
                elif choice == '5':
                    self.machine.exit_maintenance()
                
                else:
                    print("Invalid choice")
            
            except ValueError as e:
                print(f"Invalid input: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                logging.error(f"Maintenance menu error: {str(e)}")

if __name__ == "__main__":
    try:
        machine = CoffeeMachine()
        ui = CoffeeMachineUI(machine)
        ui.run()
    except Exception as e:
        logging.critical(f"Fatal error: {str(e)}")
        print(f"A critical error occurred: {str(e)}")