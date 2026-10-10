from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza(Food):
     def prepare(self):
         print("Preparing pizza")

class Burger(Food):
     def prepare(self):
         print("Preparing burger")


class Pasta(Food):
    def prepare(self):
        print("Preparing pasta")