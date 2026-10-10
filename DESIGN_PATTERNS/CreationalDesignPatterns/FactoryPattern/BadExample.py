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

#Responsible for making objects

class RestaurantService:
    ## Tightly Coupled
    ## Not good for extension
    ## Violated Open/Closed Principle
    def create_order(self,food_type:str):
        if food_type == "Pizza":
            f = Pizza()
        elif food_type == "Burger":
            f = Burger()
        elif food_type == "Pasta":
            f = Pasta()
        else:
            print("Invalid food type")
            return None
        f.prepare()
        return f

restaurant_service = RestaurantService()
restaurant_service.create_order("Pizza")
restaurant_service.create_order("Burger")
restaurant_service.create_order("Pasta")
