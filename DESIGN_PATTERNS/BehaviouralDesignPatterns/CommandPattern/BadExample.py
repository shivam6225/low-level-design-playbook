class Chef:
    def cook_pasta(self):
        print("Chef is cooking Pasta")
    def cook_pizza(self):
        print("Chef is cooking Pizza")
    #If you add new item in Chef

class Waiter:
    def __init__(self, chef:Chef):
        self.__chef = chef

    def place_order(self,item:str):
        if item=="pasta":
            self.__chef.cook_pasta()
        elif item=="pizza":
            self.__chef.cook_pizza()
        #Add new item in Waiter
        #Open-Closed Principle is violated
        else:
            print("Invalid Item")


chef = Chef()
waiter = Waiter(chef)
waiter.place_order("pasta")
waiter.place_order("pizza")