"""
Parent Class : Base Class
Child Class : Derived Class -> inherits everything from the parent class
Child Class also adds its own specific feature
Parent Class changes automatically reflect in child class
Example : Animal with method eat() and sleep()
Dog child class adds bark()
Cat child class adds meow()
Polymorphism -> Same method name works differently for different classes
Method overriding : child class provides its own version of a parent's method
"""

class Animal:

    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

    def move(self):
        print("I am moving")

#Inherits the Animal class -> we add it in ()
class Dog(Animal):

    def __init__(self,name=None,age=0,breed=None):
        super().__init__(name,age)
        self.breed=breed

    def who(self):
        print(f"I am dog and my name is {self.name} and I am {self.age} years old. My breed is {self.breed}")

    def bark(self):
        print("I am barking")

    #Method Overriding - Polymorphism
    def move(self):
        print("I am running on 4 legs")

class Cat(Animal):
    def meow(self):
        print("I am meowing")


dog=Dog("Harry",20,"German-Shepherd")
dog.eat()
dog.sleep()
dog.bark()
dog.who()
dog.move()


cat=Cat()
cat.meow()

animal=Animal()
animal.eat()
animal.sleep()