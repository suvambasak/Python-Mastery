from abc import ABC, abstractmethod


############################################
# Example 1
############################################

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass

# Subclass implementing the abstract method


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"

# Abstract class cannot be instantiated
# animal = Animal()  # Raises TypeError


dog = Dog()
print(dog.sound())  # Output: Bark

cat = Cat()
print(cat.sound())  # Output: Meow


############################################
# Example 2
############################################

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(5, 10)
print(rect.area())       # Output: 50
print(rect.perimeter())  # Output: 30


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


c = Circle(5)
print(c.area())       # Output: 78.5
print(c.perimeter())  # Output: 31.400000000000002


class Account(ABC):
    balance = 0

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def get_balance(self):
        return self.balance

    @abstractmethod
    def interest(self):
        pass


class SavingsAccount(Account):
    def interest(self):
        return self.balance * 0.05


class CurrentAccount(Account):
    def interest(self):
        return self.balance * 0.02

    def benefits(self):
        return "No benefits"


class LoanAccount(Account):
    def interest(self):
        return self.balance * 0.08
