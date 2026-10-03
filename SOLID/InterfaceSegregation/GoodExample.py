from abc import ABC , abstractmethod

class Workable(ABC):

    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass

class Employee(Workable,Eatable):

    def eat(self):
        print("Employee is eating")

    def work(self):
        print("Working is working")

class Robot(Workable):
    def eat(self):
        #Violates Interface Segregation
        raise Exception("Robot cannot eat")