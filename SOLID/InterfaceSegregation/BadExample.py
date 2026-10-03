from abc import ABC , abstractmethod


class Employee(ABC):

    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def work(self):
        pass

class Worker(Employee):
    def eat(self):
        print("Worker is eating")

    def work(self):
        print("Working is working")

class Robot(Employee):
    def eat(self):
        #Violates Interface Segregation
        raise Exception("Robot cannot eat")

    def work(self):
        print("Robot is working")