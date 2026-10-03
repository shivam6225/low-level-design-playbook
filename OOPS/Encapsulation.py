"""
Protecting the data
Data Hiding
Public , Private ,Protected
Sensitive Data is marked Private -> it can't be accessed directly
getter and setter can be used to access private attributes
"""

class Bank:

    def __init__(self,name=None,balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self,amount:int):
        if self.__is_server_live():
            self.__balance += amount
            print("Amount deposited",amount)

    def __is_server_live(self):
        return True

    def withdraw(self,amount=0):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn",amount)
        else:
            print("Not enough money")

    def get_balance(self):
        print("Current balance",self.__balance)


acc = Bank("Shivam", 1000)
acc.deposit(100)
#This shouldn't be allowed
#After making private this won't be able to access
acc.balance = 3000
acc.get_balance()
acc.withdraw(200)
#won't be able to access this
#acc.__is_server_live()