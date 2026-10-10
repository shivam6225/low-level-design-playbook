from abc import ABC
from Food import *

class FoodFactory:
    @staticmethod
    def create_food(food_type:str) -> Food|None:
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        elif food_type == "pasta":
            return Pasta()
        else:
            return None
