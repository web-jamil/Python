# --- AttributeError: All About in Code ---

# An AttributeError is raised when you try to access an attribute (a property or method)
# on an object that does not possess that attribute.

# --- 1. Basic AttributeError ---
print("--- 1. Basic AttributeError ---")

class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

obj = MyClass(10)

# Accessing an existing attribute (OK)
print(f"Accessing existing attribute 'value': {obj.value}")

# Accessing an existing method (OK)
obj.display()

# Attempting to access a non-existent attribute (causes AttributeError)
try:
    print(obj.non_existent_attribute)
except AttributeError as e:
    print(f"Caught AttributeError (expected): {e}")
    print("Reason: 'MyClass' object has no attribute 'non_existent_attribute'.")

print("-" * 50 + "\n")


# --- 2. AttributeError on Built-in Types ---
print("--- 2. AttributeError on Built-in Types ---")

# Strings
my_string = "hello"
try:
    my_string.append(" world") # Strings do not have an 'append' method
except AttributeError as e:
    print(f"Caught AttributeError for string (expected): {e}")
    print("Reason: 'str' object has no attribute 'append'.")

# Lists
my_list = [1, 2, 3]
try:
    my_list.length # Lists have len(), not .length
except AttributeError as e:
    print(f"Caught AttributeError for list (expected): {e}")
    print("Reason: 'list' object has no attribute 'length'. (Use len(my_list) instead)")

# Integers
my_int = 5
try:
    my_int.add(3) # Integers do not have methods like 'add' for arithmetic
except AttributeError as e:
    print(f"Caught AttributeError for int (expected): {e}")
    print("Reason: 'int' object has no attribute 'add'. (Use + operator instead)")

# NoneType
my_none = None
try:
    my_none.some_method() # NoneType has no attributes or methods
except AttributeError as e:
    print(f"Caught AttributeError for NoneType (expected): {e}")
    print("Reason: 'NoneType' object has no attribute 'some_method'.")
    print("Important: Always check for None before accessing attributes/methods.")

print("-" * 50 + "\n")


# --- 3. AttributeError during Class Definition / Inheritance ---
print("--- 3. AttributeError during Class Definition / Inheritance ---")

class Parent:
    def method_a(self):
        print("Method A from Parent")

class Child(Parent):
    def method_b(self):
        print("Method B from Child")

child_obj = Child()
child_obj.method_a() # Inherited method (OK)
child_obj.method_b() # Child's own method (OK)

try:
    child_obj.method_c() # Neither Parent nor Child has method_c
except AttributeError as e:
    print(f"Caught AttributeError (expected): {e}")
    print("Reason: 'Child' object has no attribute 'method_c'.")

print("-" * 50 + "\n")


# --- 4. AttributeError with Dynamic Attributes (__getattr__, __setattr__) ---
print("--- 4. AttributeError with Dynamic Attributes ---")

class DynamicAttributes:
    def __init__(self):
        self._data = {}

    # __getattr__ is called when an attribute is not found in the usual places
    def __getattr__(self, name):
        if name in self._data:
            print(f"__getattr__ called for '{name}'")
            return self._data[name]
        # Important: If __getattr__ cannot handle the attribute, it MUST raise AttributeError
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    # __setattr__ is called for every attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('data_'):
            self._data[name[5:]] = value # Store under a simplified name
            print(f"__setattr__ storing '{name}' as '{name[5:]}' in _data")
        else:
            # For other attributes, use the default way of setting attributes
            super().__setattr__(name, value)

dyn_obj = DynamicAttributes()

# Setting an attribute via __setattr__
dyn_obj.data_item1 = "Value 1"
dyn_obj.data_item2 = 42

# Accessing an attribute via __getattr__
print(f"Accessing 'item1' via __getattr__: {dyn_obj.item1}")
print(f"Accessing 'item2' via __getattr__: {dyn_obj.item2}")

# Attempting to access a truly non-existent attribute, causing AttributeError from __getattr__
try:
    print(dyn_obj.non_existent_data)
except AttributeError as e:
    print(f"Caught AttributeError from __getattr__ (expected): {e}")
    print("Reason: '__getattr__' explicitly raised it because the key was not in '_data'.")

# Accessing a regular attribute (not handled by __getattr__)
dyn_obj.regular_prop = "Hello"
print(f"Accessing 'regular_prop': {dyn_obj.regular_prop}")

print("-" * 50 + "\n")


# --- 5. Preventing AttributeError (Best Practices) ---
print("--- 5. Preventing AttributeError (Best Practices) ---")

# 5.1 Check if an object is None before accessing attributes
def process_user_data(user):
    if user is None:
        print("Error: User object is None, cannot process.")
        return
    print(f"Processing user: {user.name}")

class User:
    def __init__(self, name):
        self.name = name

user1 = User("Alice")
user2 = None

process_user_data(user1)
process_user_data(user2)

# 5.2 Using `hasattr()` to check for attribute existence
class Config:
    def __init__(self, mode="production"):
        self.mode = mode

settings = Config()
# settings = Config(mode="debug") # Uncomment to test 'debug_mode' attribute

if hasattr(settings, 'debug_mode'):
    print(f"Debug mode attribute exists: {settings.debug_mode}")
else:
    print("Debug mode attribute does not exist on 'settings' object.")

# 5.3 Using `getattr()` with a default value
# getattr(object, name[, default])
# Returns the value of the named attribute of object. If the named attribute does not exist,
# default is returned if provided, otherwise AttributeError is raised.
username = getattr(user1, 'name', 'Guest')
print(f"User's name (using getattr): {username}")

non_existent_attr = getattr(user1, 'email', 'N/A')
print(f"Non-existent attribute (using getattr with default): {non_existent_attr}")

try:
    # This will raise AttributeError because no default is provided
    getattr(user1, 'phone_number')
except AttributeError as e:
    print(f"Caught AttributeError (expected from getattr without default): {e}")

print("-" * 50 + "\n")


# --- 6. Common Scenarios Leading to AttributeError ---
print("--- 6. Common Scenarios Leading to AttributeError ---")

# 6.1 Typo in attribute name
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
# my_vehicle = Vehicle("Toyota")
# try:
#     print(my_vehicle.brnd) # Typo
# except AttributeError as e:
#     print(f"Caught AttributeError (typo): {e}")

# 6.2 Object not initialized or assigned correctly
# obj_uninitialized = None
# try:
#     obj_uninitialized.some_method()
# except AttributeError as e:
#     print(f"Caught AttributeError (uninitialized object): {e}")

# 6.3 Using instance attributes on a class, or vice-versa
class Counter:
    count = 0 # Class attribute

    def __init__(self):
        self.instance_id = "abc" # Instance attribute

# Accessing class attribute (OK)
print(f"Class attribute 'count': {Counter.count}")

# Accessing instance attribute via instance (OK)
c1 = Counter()
print(f"Instance attribute 'instance_id': {c1.instance_id}")

try:
    print(Counter.instance_id) # Instance attribute on class (causes error)
except AttributeError as e:
    print(f"Caught AttributeError (instance attr on class): {e}")
    print("Reason: 'Counter' class has no attribute 'instance_id'.")

try:
    print(c1.count) # Accessing class attribute via instance (OK, but usually accessed via class)
except AttributeError as e:
    # This specifically would NOT cause an AttributeError, as instances can access class attributes
    print("This line would not cause an AttributeError for 'count'.")

print("-" * 50 + "\n")

print("--- End of AttributeError demonstration ---")



# --- AttributeError: More Examples ---

# This section provides additional scenarios where AttributeError commonly occurs
# and demonstrates various ways to handle or avoid them.

# --- 7. Accessing Attributes on Imported Modules/Objects Before Initialization ---
print("--- 7. Accessing Attributes on Imported Modules/Objects Before Initialization ---")

# Imagine a scenario where a module or a global object needs to be set up
# before its attributes can be accessed.

# Example: A (simplified) config manager
class ConfigManager:
    _instance = None # Singleton instance
    _config_data = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    def load_config(self, filepath="default_config.json"):
        # In a real scenario, this would load from a file
        print(f"Loading config from {filepath}...")
        self._config_data = {
            "api_key": "some_secret_key_123",
            "log_level": "INFO",
            "database_url": "sqlite:///app.db"
        }
        print("Config loaded.")

    @property # Allows accessing _config_data values like attributes
    def api_key(self):
        return self._config_data.get("api_key")

    @property
    def log_level(self):
        return self._config_data.get("log_level")

# Simulate application start-up without loading config first
config = ConfigManager()

print("\nAttempting to access config BEFORE loading:")
try:
    # Initially, _config_data is empty, so .get("api_key") would return None,
    # but if we tried to access a non-existent *attribute* of _config_data itself
    # or if we designed ConfigManager differently, we might hit AttributeError.
    # In this specific @property design, .get() returns None, which is then accessed.
    # Let's force an AttributeError by accessing a property that relies on data
    # that's truly not there or in a different structure.
    print(config.api_key) # This will print None, not AttributeError due to .get()
    print("No AttributeError, but API Key is:", config.api_key)

    # Let's create a scenario where a property might fail if _config_data isn't populated
    class BadConfigManager(ConfigManager):
        @property
        def required_setting(self):
            # If _config_data is empty or not a dict, this could fail
            return self._config_data['a_key_that_must_exist']

    bad_config = BadConfigManager()
    print("\nAttempting to access config BEFORE loading (designed to fail):")
    try:
        print(bad_config.required_setting)
    except KeyError as e: # Catching KeyError here, as .get() was not used
        print(f"Caught KeyError (expected): {e}")
        print("Reason: Tried to access a key in an empty or uninitialized dictionary.")
    except AttributeError as e:
        print(f"Caught AttributeError (less likely here, but possible): {e}")


except AttributeError as e:
    print(f"Caught AttributeError (expected): {e}")
    print("Reason: Config was not loaded, underlying data structure not set up.")

# Now, load the config and retry
print("\nLoading config and trying again:")
config.load_config()
print(f"API Key: {config.api_key}") # Now it works

print("-" * 50 + "\n")


# --- 8. Accessing Attributes on Dynamic/Mock Objects ---
print("--- 8. Accessing Attributes on Dynamic/Mock Objects ---")

# When using mock objects in testing, if a mock isn't configured correctly,
# accessing an un-mocked attribute can lead to AttributeError.

from unittest.mock import Mock

# Scenario: A service that fetches user data
class UserService:
    def get_user_by_id(self, user_id):
        # In a real app, this would query a database or API
        if user_id == 1:
            return {"id": 1, "name": "Eve", "email": "eve@example.com"}
        return None

# Create a mock for UserService
mock_user_service = Mock(spec=UserService) # spec=UserService ensures valid methods/attributes

# Mock a specific method
mock_user_service.get_user_by_id.return_value = {"id": 10, "name": "MockUser", "email": "mock@test.com"}

# Accessing a mocked method (OK)
user = mock_user_service.get_user_by_id(10)
print(f"Mocked user data: {user}")

# Attempting to access an attribute that was NOT mocked and does not exist on the original spec
try:
    # If UserService didn't have 'get_user_by_id_extra' or if spec was used wrongly
    print(mock_user_service.get_user_by_id_extra(5))
except AttributeError as e:
    print(f"Caught AttributeError (expected for un-mocked method not in spec): {e}")
    print("Reason: The mock object (or its spec) does not have 'get_user_by_id_extra'.")

# Without spec=UserService, a Mock would allow accessing any attribute,
# returning another Mock object by default, not an AttributeError.
mock_no_spec = Mock()
print(f"Mock without spec allows anything: {mock_no_spec.non_existent_attribute_creates_another_mock}")
print(f"Type of new mock: {type(mock_no_spec.non_existent_attribute_creates_another_mock)}")

print("-" * 50 + "\n")


# --- 9. Race Conditions or State Changes Leading to AttributeError ---
print("--- 9. Race Conditions or State Changes Leading to AttributeError ---")

# In multi-threaded or asynchronous environments, an object's state might change
# between checking for an attribute and accessing it.
import threading
import time

class SharedResource:
    def __init__(self):
        self.data = "initial_data"
        self.lock = threading.Lock()

    def process(self):
        with self.lock:
            # Simulate some work that might remove the attribute
            time.sleep(0.01) # Small delay
            if hasattr(self, 'data'):
                # In a race condition, 'data' might be deleted by another thread *here*
                # before the next line executes.
                try:
                    result = self.data.upper() # AttributeError if 'data' was deleted
                    print(f"Processed: {result}")
                except AttributeError as e:
                    print(f"Caught AttributeError in race condition (simulated): {e}")
                    print("Reason: 'data' attribute was likely removed by another thread.")
            else:
                print("Data attribute was already removed.")

    def clear_data(self):
        with self.lock:
            print("Clearing data...")
            if hasattr(self, 'data'):
                del self.data
            print("Data cleared.")

resource = SharedResource()

def worker_process():
    resource.process()

def worker_clear():
    # This thread tries to clear the data while others might be processing
    time.sleep(0.005) # Clear slightly earlier
    resource.clear_data()

# Run multiple threads that try to process and one that tries to clear
threads = []
for _ in range(5):
    threads.append(threading.Thread(target=worker_process))
threads.append(threading.Thread(target=worker_clear)) # The thread that removes the attribute

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Race condition simulation complete.")
print("-" * 50 + "\n")


# --- 10. Common Typo/Misconception Examples ---
print("--- 10. Common Typo/Misconception Examples ---")

# 10.1 `len` vs `.length()`
my_list = [1, 2, 3]
try:
    print(my_list.length()) # Incorrect for lists
except AttributeError as e:
    print(f"Caught AttributeError (for list.length()): {e}")
    print("Correct: `len(my_list)` is the function for length.")

# 10.2 String methods that don't exist
my_str = "Python"
try:
    print(my_str.upper_case()) # Typo, should be .upper()
except AttributeError as e:
    print(f"Caught AttributeError (for string.upper_case()): {e}")
    print("Correct: `my_str.upper()`.")

# 10.3 Misunderstanding return values
# Many methods return None, and if you then try to call a method on None, it fails.
def configure_device(dev):
    # This function might return None if configuration fails, or the device object
    # If it returns None and not handled, the next line will fail.
    # For demonstration, let's make it return None sometimes.
    if dev == "bad_device":
        return None
    return dev # Simulate returning a device object

class Device:
    def __init__(self, name):
        self.name = name
    def activate(self):
        print(f"{self.name} activated.")

device1 = Device("Sensor")
device2_name = "bad_device"

configured_device1 = configure_device(device1)
if configured_device1: # Important check!
    configured_device1.activate()

configured_device2 = configure_device(device2_name)
try:
    # If configure_device returns None, this will cause AttributeError
    configured_device2.activate()
except AttributeError as e:
    print(f"Caught AttributeError (result of a function returning None): {e}")
    print("Reason: 'configured_device2' is None, and NoneType has no 'activate' method.")

print("-" * 50 + "\n")


print("--- End of More AttributeError Examples ---")



# --- AttributeError: More Examples ---

# This section provides additional scenarios where AttributeError commonly occurs
# and demonstrates various ways to handle or avoid them.

# --- 7. Accessing Attributes on Imported Modules/Objects Before Initialization ---
print("--- 7. Accessing Attributes on Imported Modules/Objects Before Initialization ---")

# Imagine a scenario where a module or a global object needs to be set up
# before its attributes can be accessed.

# Example: A (simplified) config manager
class ConfigManager:
    _instance = None # Singleton instance
    _config_data = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    def load_config(self, filepath="default_config.json"):
        # In a real scenario, this would load from a file
        print(f"Loading config from {filepath}...")
        self._config_data = {
            "api_key": "some_secret_key_123",
            "log_level": "INFO",
            "database_url": "sqlite:///app.db"
        }
        print("Config loaded.")

    @property # Allows accessing _config_data values like attributes
    def api_key(self):
        return self._config_data.get("api_key")

    @property
    def log_level(self):
        return self._config_data.get("log_level")

# Simulate application start-up without loading config first
config = ConfigManager()

print("\nAttempting to access config BEFORE loading:")
try:
    # Initially, _config_data is empty, so .get("api_key") would return None,
    # but if we tried to access a non-existent *attribute* of _config_data itself
    # or if we designed ConfigManager differently, we might hit AttributeError.
    # In this specific @property design, .get() returns None, which is then accessed.
    # Let's force an AttributeError by accessing a property that relies on data
    # that's truly not there or in a different structure.
    print(config.api_key) # This will print None, not AttributeError due to .get()
    print("No AttributeError, but API Key is:", config.api_key)

    # Let's create a scenario where a property might fail if _config_data isn't populated
    class BadConfigManager(ConfigManager):
        @property
        def required_setting(self):
            # If _config_data is empty or not a dict, this could fail
            return self._config_data['a_key_that_must_exist']

    bad_config = BadConfigManager()
    print("\nAttempting to access config BEFORE loading (designed to fail):")
    try:
        print(bad_config.required_setting)
    except KeyError as e: # Catching KeyError here, as .get() was not used
        print(f"Caught KeyError (expected): {e}")
        print("Reason: Tried to access a key in an empty or uninitialized dictionary.")
    except AttributeError as e:
        print(f"Caught AttributeError (less likely here, but possible): {e}")


except AttributeError as e:
    print(f"Caught AttributeError (expected): {e}")
    print("Reason: Config was not loaded, underlying data structure not set up.")

# Now, load the config and retry
print("\nLoading config and trying again:")
config.load_config()
print(f"API Key: {config.api_key}") # Now it works

print("-" * 50 + "\n")


# --- 8. Accessing Attributes on Dynamic/Mock Objects ---
print("--- 8. Accessing Attributes on Dynamic/Mock Objects ---")

# When using mock objects in testing, if a mock isn't configured correctly,
# accessing an un-mocked attribute can lead to AttributeError.

from unittest.mock import Mock

# Scenario: A service that fetches user data
class UserService:
    def get_user_by_id(self, user_id):
        # In a real app, this would query a database or API
        if user_id == 1:
            return {"id": 1, "name": "Eve", "email": "eve@example.com"}
        return None

# Create a mock for UserService
mock_user_service = Mock(spec=UserService) # spec=UserService ensures valid methods/attributes

# Mock a specific method
mock_user_service.get_user_by_id.return_value = {"id": 10, "name": "MockUser", "email": "mock@test.com"}

# Accessing a mocked method (OK)
user = mock_user_service.get_user_by_id(10)
print(f"Mocked user data: {user}")

# Attempting to access an attribute that was NOT mocked and does not exist on the original spec
try:
    # If UserService didn't have 'get_user_by_id_extra' or if spec was used wrongly
    print(mock_user_service.get_user_by_id_extra(5))
except AttributeError as e:
    print(f"Caught AttributeError (expected for un-mocked method not in spec): {e}")
    print("Reason: The mock object (or its spec) does not have 'get_user_by_id_extra'.")

# Without spec=UserService, a Mock would allow accessing any attribute,
# returning another Mock object by default, not an AttributeError.
mock_no_spec = Mock()
print(f"Mock without spec allows anything: {mock_no_spec.non_existent_attribute_creates_another_mock}")
print(f"Type of new mock: {type(mock_no_spec.non_existent_attribute_creates_another_mock)}")

print("-" * 50 + "\n")


# --- 9. Race Conditions or State Changes Leading to AttributeError ---
print("--- 9. Race Conditions or State Changes Leading to AttributeError ---")

# In multi-threaded or asynchronous environments, an object's state might change
# between checking for an attribute and accessing it.
import threading
import time

class SharedResource:
    def __init__(self):
        self.data = "initial_data"
        self.lock = threading.Lock()

    def process(self):
        with self.lock:
            # Simulate some work that might remove the attribute
            time.sleep(0.01) # Small delay
            if hasattr(self, 'data'):
                # In a race condition, 'data' might be deleted by another thread *here*
                # before the next line executes.
                try:
                    result = self.data.upper() # AttributeError if 'data' was deleted
                    print(f"Processed: {result}")
                except AttributeError as e:
                    print(f"Caught AttributeError in race condition (simulated): {e}")
                    print("Reason: 'data' attribute was likely removed by another thread.")
            else:
                print("Data attribute was already removed.")

    def clear_data(self):
        with self.lock:
            print("Clearing data...")
            if hasattr(self, 'data'):
                del self.data
            print("Data cleared.")

resource = SharedResource()

def worker_process():
    resource.process()

def worker_clear():
    # This thread tries to clear the data while others might be processing
    time.sleep(0.005) # Clear slightly earlier
    resource.clear_data()

# Run multiple threads that try to process and one that tries to clear
threads = []
for _ in range(5):
    threads.append(threading.Thread(target=worker_process))
threads.append(threading.Thread(target=worker_clear)) # The thread that removes the attribute

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Race condition simulation complete.")
print("-" * 50 + "\n")


# --- 10. Common Typo/Misconception Examples ---
print("--- 10. Common Typo/Misconception Examples ---")

# 10.1 `len` vs `.length()`
my_list = [1, 2, 3]
try:
    print(my_list.length()) # Incorrect for lists
except AttributeError as e:
    print(f"Caught AttributeError (for list.length()): {e}")
    print("Correct: `len(my_list)` is the function for length.")

# 10.2 String methods that don't exist
my_str = "Python"
try:
    print(my_str.upper_case()) # Typo, should be .upper()
except AttributeError as e:
    print(f"Caught AttributeError (for string.upper_case()): {e}")
    print("Correct: `my_str.upper()`.")

# 10.3 Misunderstanding return values
# Many methods return None, and if you then try to call a method on None, it fails.
def configure_device(dev):
    # This function might return None if configuration fails, or the device object
    # If it returns None and not handled, the next line will fail.
    # For demonstration, let's make it return None sometimes.
    if dev == "bad_device":
        return None
    return dev # Simulate returning a device object

class Device:
    def __init__(self, name):
        self.name = name
    def activate(self):
        print(f"{self.name} activated.")

device1 = Device("Sensor")
device2_name = "bad_device"

configured_device1 = configure_device(device1)
if configured_device1: # Important check!
    configured_device1.activate()

configured_device2 = configure_device(device2_name)
try:
    # If configure_device returns None, this will cause AttributeError
    configured_device2.activate()
except AttributeError as e:
    print(f"Caught AttributeError (result of a function returning None): {e}")
    print("Reason: 'configured_device2' is None, and NoneType has no 'activate' method.")

print("-" * 50 + "\n")


print("--- End of More AttributeError Examples ---")