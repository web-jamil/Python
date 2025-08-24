# classes are the foundation of object oriented programming (oop) in python . they allow you to create your own custom data tyoes with associated attributes and methods .

class MyClass:
    """ A simple example class"""
    class_attribute="I'm a class attributes"
    # this attributes is shared among all classes intances
    def __init__(self,param1, param2):
        """ Constructor method - initializes instance attributes """
        self.instance_attr1=param1 # instance attribute
        self.instance_attr2=param2 # instance attribute

    def instance_method(self):
        """ A method that operates on instance data """
        return f"Values : {self.instance_attr1}, {self.instance_attr2}"


""" the ___init__ method
1. called automatically when creating a new instance 
2.self refers to the instance being created
3.used to initialize instance attributes 
"""
obj=MyClass("hello",42)

# instance methods 
# functions defined inside the class
# first parameter is always self(convention)
# can access and modify instance attributes 
obj.instance_method() # calls the method on the instance 


#  class attibutes 
# variables defined directly in the classs(not in methods )
# shared by all instances of the class
# can be accessed via class or instance 
print(MyClass.class_attribute)
print(obj.class_attribute)


# instance attributes 
# variables specific to each instance 
# typically create in __init__
# accessed via self in methods or via instance name 
print(obj.instance_attr1)

# advance class feature 
class MyClass:
    @classmethod
    def class_method(cls):
        """ receives class as first argument instead of instance """
        return f"Called from {cls.__name__}"

    @staticmethod
    def static_method():
        """no self or cls parameter - just a regular functions """
        return "I'm a static method"

# property decorators(getters / setters)
