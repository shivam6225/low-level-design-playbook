#OOP -> Object-Oriented Programming
"""
Class is Template (Blueprint) -> defines what attributes and methods an object will have
Object is instance of class
Reduces the repetitiveness
Easier to maintain , debug
Modular approach
Annotations -> the type of the Attribute that we give
"""

class Student:
    #Attributes
    # name = ""
    # age =0
    # gender = ""

    #Initialisation Method
    #self has object reference (same memory/location)
    def __init__(self,name=None,age=0 ,gender=None) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self) -> None:
        print(f"My name is {self.name} and I am {self.age} years old and my gender is {self.gender}")

    def get_age(self) -> int:
        return self.age


name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
s1 =Student(name,age,gender)

print(s1)
print(s1.name)
print(s1.age)
print(s1.gender)
s1.display()
s1.get_age()

# s2 is independent object of the class Student and not related to s1
s2 = Student()
print(s2)
print(s2.name)
print(s2.age)