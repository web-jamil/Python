import abc

# --- 1. Basic NotADirectoryError Usage (As a Placeholder) ---

class BaseShape:
    def area(self):
        # NotImplementedError signals that subclasses MUST implement this method.
        # If a subclass forgets to implement it, calling this will raise the error.
        raise NotImplementedError("Subclasses must implement the 'area' method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the 'perimeter' method.")

class Circle(BaseShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    # Oops! Forgot to implement perimeter in Circle.
    # If perimeter() is called on a Circle instance, it will raise NotImplementedError.

class Square(BaseShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

def basic_not_implemented_example():
    print("\n--- 1. Basic NotImplementedError Usage ---")
    
    circle = Circle(5)
    square = Square(4)

    try:
        print(f"Circle area: {circle.area()}")
        print(f"Square area: {square.area()}")
        print(f"Square perimeter: {square.perimeter()}")

        # This will raise NotImplementedError because Circle doesn't implement it
        print(f"Circle perimeter: {circle.perimeter()}")

    except NotImplementedError as e:
        print(f"[CAUGHT ERROR] NotImplementedError: {e}")
        print("  This indicates a method was called that was expected to be implemented by a subclass.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

# --- 2. Using NotImplemented as a Special Value ---

# NotImplemented is a special constant, not an exception.
# It's primarily used in special methods (like __eq__, __add__) to signal
# that the operation cannot be handled by the current object's type,
# allowing Python to try the reverse operation or a different type.

class MyNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # If 'other' is also MyNumber, perform addition
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        # If 'other' is not MyNumber, return NotImplemented to let Python
        # try the reverse operation (other.__radd__(self)) or raise TypeError.
        # This signals "I don't know how to add myself to this type."
        return NotImplemented

    def __radd__(self, other): # Called if other.__add__(self) returns NotImplemented
        if isinstance(other, (int, float)):
            return MyNumber(other + self.value)
        return NotImplemented # If still can't handle, let Python raise TypeError

    def __repr__(self):
        return f"MyNumber({self.value})"

def not_implemented_value_example():
    print("\n--- 2. Using NotImplemented as a Special Value ---")
    n1 = MyNumber(10)
    n2 = MyNumber(20)

    try:
        # MyNumber + MyNumber -> Handled by MyNumber.__add__
        result1 = n1 + n2
        print(f"MyNumber(10) + MyNumber(20) = {result1}")

        # int + MyNumber -> int.__add__ is called, returns NotImplemented, then MyNumber.__radd__ is called
        result2 = 5 + n1
        print(f"5 + MyNumber(10) = {result2}")

        # MyNumber + list -> MyNumber.__add__ returns NotImplemented, list.__radd__ returns NotImplemented, then TypeError
        try:
            result3 = n1 + [1, 2]
            print(f"MyNumber(10) + [1,2] = {result3}")
        except TypeError as e:
            print(f"[EXPECTED ERROR] TypeError (as both __add__ and __radd__ returned NotImplemented): {e}")

    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

# --- 3. Using ABCs (Abstract Base Classes) for Enforced Implementation ---

# ABCs provide a more robust way to ensure methods are implemented by subclasses
# by making them truly abstract. If a non-abstract subclass doesn't implement
# an abstract method, instantiating it will raise a TypeError.

class AbstractWorker(abc.ABC): # Inherit from abc.ABC
    @abc.abstractmethod
    def work(self, task):
        # No implementation here. This method MUST be overridden.
        pass

    @abc.abstractmethod
    def get_status(self):
        pass

    def common_method(self):
        return "This is a common method for all workers."

class ConcreteWorker(AbstractWorker):
    def __init__(self, name):
        self.name = name
        self._current_task = None

    def work(self, task):
        self._current_task = task
        return f"{self.name} is working on: {task}"

    # Forgot to implement get_status() here!

class AnotherConcreteWorker(AbstractWorker):
    def __init__(self, name):
        self.name = name
        self._current_task = None
        self._status = "Idle"

    def work(self, task):
        self._current_task = task
        self._status = f"Working on {task}"
        return f"{self.name} started {task}."

    def get_status(self):
        return self._status

def abc_not_implemented_example():
    print("\n--- 3. Using ABCs for Enforced Implementation ---")

    try:
        # This will raise TypeError because ConcreteWorker doesn't implement get_status()
        worker1 = ConcreteWorker("Alice")
        print(f"Worker1 common method: {worker1.common_method()}")
        print(f"Worker1 work: {worker1.work('report')}")
        # If we tried to call worker1.get_status() even if it could be instantiated,
        # it would raise NotImplementedError from the base class (if it had one, but ABC prevents instantiation).
    except TypeError as e:
        print(f"[CAUGHT ERROR] TypeError (as expected): {e}")
        print("  This indicates that ConcreteWorker failed to implement all abstract methods.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

    print("\n  Demonstrating a correctly implemented ABC subclass:")
    try:
        worker2 = AnotherConcreteWorker("Bob")
        print(f"Worker2 common method: {worker2.common_method()}")
        print(f"Worker2 status: {worker2.get_status()}")
        print(f"Worker2 work: {worker2.work('analysis')}")
        print(f"Worker2 new status: {worker2.get_status()}")
        print("[SUCCESS] AnotherConcreteWorker was instantiated and used correctly.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

# --- 4. Future/Planned Features Placeholder ---

# Sometimes, you might use NotImplementedError for features that are planned
# but not yet implemented.
class FeatureManager:
    def __init__(self):
        self.version = "1.0"

    def process_data(self, data):
        # Current version processes data
        return f"Processing data: {data}"

    def generate_report(self, data):
        # This feature is planned for v2.0
        raise NotImplementedError("Report generation feature is not yet implemented in this version (v1.0).")

def future_feature_example():
    print("\n--- 4. Future/Planned Features Placeholder ---")
    manager = FeatureManager()

    try:
        print(manager.process_data("raw input"))
        manager.generate_report({"stats": 123})
    except NotImplementedError as e:
        print(f"[CAUGHT ERROR] NotImplementedError: {e}")
        print("  This signals that the requested feature is not available yet.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

# --- Main Execution Block ---
if __name__ == "__main__":
    basic_not_implemented_example()
    input("\nPress Enter to run the next example: Using NotImplemented as a Special Value...")

    not_implemented_value_example()
    input("\nPress Enter to run the next example: Using ABCs for Enforced Implementation...")

    abc_not_implemented_example()
    input("\nPress Enter to run the next example: Future/Planned Features Placeholder...")

    future_feature_example()

    print("\nAll NotImplementedError demonstrations concluded.")


    import abc

# --- 5. Customizing a Built-in Type's Behavior (Example: Custom List Method) ---

class MyCustomList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sort_complex(self, key=None, reverse=False):
        """
        A more advanced sorting method that is not yet implemented.
        This signals that users should use the standard sort() for now.
        """
        raise NotImplementedError("Advanced 'sort_complex' with specific algorithms is not yet available.")

    def reverse_in_place(self):
        """Standard list reverse operation, implemented."""
        super().reverse()


def custom_list_example():
    print("\n--- 5. Customizing a Built-in Type's Behavior ---")
    my_list = MyCustomList([5, 2, 8, 1, 9])
    print(f"Original list: {my_list}")

    try:
        my_list.reverse_in_place()
        print(f"Reversed list: {my_list}")

        # Attempt to call the unimplemented method
        my_list.sort_complex()
    except NotImplementedError as e:
        print(f"[CAUGHT ERROR] NotImplementedError: {e}")
        print("  This feature is marked as not yet implemented for this custom list.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

# --- 6. Interface Enforcement in Plugins/Frameworks (Simulated) ---

# Imagine a simple plugin system where plugins must adhere to an interface.

class PluginInterface(abc.ABC):
    @abc.abstractmethod
    def initialize(self, config):
        """Initializes the plugin with given configuration."""
        pass

    @abc.abstractmethod
    def process_data(self, data):
        """Processes incoming data."""
        pass

    @abc.abstractmethod
    def shutdown(self):
        """Performs cleanup before plugin unloads."""
        pass

class GoodPlugin(PluginInterface):
    def __init__(self, name):
        self.name = name
        self.is_initialized = False

    def initialize(self, config):
        self.config = config
        self.is_initialized = True
        print(f"  [{self.name}] Initialized with config: {config}")

    def process_data(self, data):
        if not self.is_initialized:
            raise RuntimeError(f"[{self.name}] Not initialized!")
        processed_data = f"[{self.name}] Processed: {data.upper()}"
        print(f"  {processed_data}")
        return processed_data

    def shutdown(self):
        self.is_initialized = False
        print(f"  [{self.name}] Shutting down.")

class BadPlugin(PluginInterface):
    def __init__(self, name):
        self.name = name

    def initialize(self, config):
        print(f"  [{self.name}] Initializing (partially)...")
        # Missing full implementation, or just forgot other methods

    # Missing process_data and shutdown methods!

def plugin_framework_example():
    print("\n--- 6. Interface Enforcement in Plugins/Frameworks ---")

    print("  Attempting to load GoodPlugin:")
    try:
        good_plugin = GoodPlugin("DataProcessorV1")
        good_plugin.initialize({"log_level": "info"})
        good_plugin.process_data("sensor_reading_123")
        good_plugin.shutdown()
        print("[SUCCESS] GoodPlugin loaded and used correctly.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

    print("\n  Attempting to load BadPlugin (missing implementations):")
    try:
        # This will raise TypeError because BadPlugin doesn't implement all abstract methods
        bad_plugin = BadPlugin("FaultyReader")
        bad_plugin.initialize({"source": "bad_data_feed"}) # This part might run
        # If it were instantiated, calling missing methods would raise NotImplementedError
    except TypeError as e:
        print(f"[CAUGHT ERROR] TypeError: {e}")
        print("  BadPlugin could not be instantiated because it failed to implement all abstract methods of PluginInterface.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

# --- 7. When a Method is Inherited But Not Relevant for a Subclass ---

# Sometimes a method from a base class is simply not applicable to a specific subclass.
# Instead of providing a dummy implementation, raising NotImplementedError can be clearer.

class Vehicle(abc.ABC):
    @abc.abstractmethod
    def start_engine(self):
        pass

    @abc.abstractmethod
    def stop_engine(self):
        pass

    def drive(self):
        print("Vehicle is driving.")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with ignition key.")

    def stop_engine(self):
        print("Car engine stopped.")

class Bicycle(Vehicle):
    def start_engine(self):
        # A bicycle doesn't have an engine to start.
        # Raising NotImplementedError clearly states this.
        raise NotImplementedError("Bicycles do not have an engine to start.")

    def stop_engine(self):
        raise NotImplementedError("Bicycles do not have an engine to stop.")

    def drive(self):
        print("Bicycle is pedaling.") # Overriding drive for specific behavior

def non_relevant_method_example():
    print("\n--- 7. When a Method is Inherited But Not Relevant for a Subclass ---")

    my_car = Car()
    try:
        my_car.start_engine()
        my_car.drive()
        my_car.stop_engine()
        print("[SUCCESS] Car operations successful.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

    print("\n  Attempting Bicycle operations:")
    my_bicycle = Bicycle()
    try:
        my_bicycle.drive() # This works
        my_bicycle.start_engine() # This will raise NotImplementedError
    except NotImplementedError as e:
        print(f"[CAUGHT ERROR] NotImplementedError: {e}")
        print("  Attempted to start engine on a Bicycle, which is not applicable.")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")

# --- Main Execution Block ---
if __name__ == "__main__":
    custom_list_example()
    input("\nPress Enter to run the next example: Interface Enforcement in Plugins/Frameworks...")

    plugin_framework_example()
    input("\nPress Enter to run the next example: When a Method is Inherited But Not Relevant...")

    non_relevant_method_example()

    print("\nAll additional NotImplementedError demonstrations concluded.")