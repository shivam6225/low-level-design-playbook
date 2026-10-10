from Starter import Starter
from MainCourse import MainCourse
from Dessert import Dessert

# ====== NORTH INDIAN ========

class PaneerTikka(Starter):
    def prepare(self):
        print("Preparing PaneerTikka (North Indian Starter)")

class ButterChicken(MainCourse):
    def prepare(self):
        print("Preparing Butter Chicken (North Indian Main Course)")

class GulabJamun(Dessert):
    def prepare(self):
        print("Preparing Gulab Jamun (North Indian Dessert)")


# ====== SOUTH INDIAN ========

class MeduVada(Starter):
    def prepare(self):
        print("Preparing Medu Vada (South Indian Starter)")

class Dosa(MainCourse):
    def prepare(self):
        print("Preparing Dosa (South Indian Main Course)")

class Payasam(Dessert):
    def prepare(self):
        print("Preparing Payasam (South Indian Dessert)")

