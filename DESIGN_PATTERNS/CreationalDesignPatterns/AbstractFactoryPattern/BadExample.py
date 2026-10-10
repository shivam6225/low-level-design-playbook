from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

# ====== NORTH INDIAN ========

class PaneerTikka(Food):
    def prepare(self):
        print("Preparing PaneerTikka (North Indian Starter)")

class ButterChicken(Food):
    def prepare(self):
        print("Preparing Butter Chicken (North Indian Main Course)")

class GulabJamun(Food):
    def prepare(self):
        print("Preparing Gulab Jamun (North Indian Dessert)")


# ====== SOUTH INDIAN ========

class MeduVada(Food):
    def prepare(self):
        print("Preparing Medu Vada (South Indian Starter)")

class Dosa(Food):
    def prepare(self):
        print("Preparing Dosa (South Indian Main Course)")

class Payasam(Food):
    def prepare(self):
        print("Preparing Payasam (South Indian Dessert)")



class RestaurantService:

    def create_meal(self,cuisine_type:str):
        if cuisine_type == "north_indian":
            starter = PaneerTikka()
            main_course = ButterChicken()
            dessert = GulabJamun()

        elif cuisine_type == "south_indian":
            starter = MeduVada()
            main_course = Dosa()
            dessert = Payasam()

        else:
            print("Invalid cuisine type")
            return None

        starter.prepare()
        main_course.prepare()
        dessert.prepare()


restaurant_service = RestaurantService()
restaurant_service.create_meal(cuisine_type="north_indian")
restaurant_service.create_meal(cuisine_type="south_indian")

#Tightly Coupled
#Violates Open/Closed Principle
