"""
Abstract class is inherited by the Child Class
then Abstract method should be defined in Child Class
It's compulsory to add them. This way be enforce some rules using abstraction
You can't make object of Abstract Class. It's not possible.
"""
# For Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

#Concrete classes
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Area of Rectangle", self.width*self.height)

    def perimeter(self):
        print("Perimeter of Rectangle", 2*(self.width+self.height))


#This can't be made
# s = Shape()
# print(s.area())
# print(s.shape.area())

# it need both methods to be valid
# TypeError: Can't instantiate abstract class Rectangle without an implementation for abstract method 'perimeter'
rectangle = Rectangle(10, 20)
rectangle.area()
rectangle.perimeter()