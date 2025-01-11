
###########################################
# Protected
###########################################


class MyClass:
    def __init__(self):
        self._protected_var = "This is protected"


obj = MyClass()
print(obj._protected_var)  # Possible to access, but not recommended

###########################################
# Private
###########################################


class MyClass:
    def __init__(self):
        self.__private_var = 42  # Private variable

    def set_private_var(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.__private_var = value

    def get_private_var(self):
        return self.__private_var  # Method to access private variable


obj = MyClass()
# AttributeError: 'MyClass' object has no attribute '__private_var'
# print(obj.__private_var)
obj.set_private_var(-10)  # Access using method
print(obj.get_private_var())  # Access using method

print(obj._MyClass__private_var)  # Access using name mangling


###########################################
# Encapsulation
###########################################


class Circle:

    def __init__(self):
        self.__radius = None

    @property
    def radius(self):
        """Getter for radius"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value

    @radius.deleter
    def radius(self):
        """Deleter for radius"""
        print("Deleting radius...")
        del self.__radius


# # Usage
c = Circle()
c.radius = 15    # Modify using @property (Setter)
print(c.radius)  # Access using @property (Getter)
del c.radius     # Delete using @property (Deleter)


###########################################
# Derived Attributes
###########################################


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


# Usage
rect = Rectangle(10, 5)
print(rect.area)  # Access derived property: 50
rect.width = 7
print(rect.area)  # Automatically updates: 35
