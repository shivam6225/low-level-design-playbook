from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,balance:int):
        self.balance = balance

    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def deposit(self,amount):
        pass

class SavingsAccount(BankAccount):
    def __init__(self,balance:int):
        super().__init__(balance)

    def withdraw(self,amount):
        if self.balance < amount:
            print("You can't withdraw , not enough balance")
        else:
            self.balance -= amount
            print(f"You withdrew : {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited : {self.balance}")

class FixedDepositAccount(BankAccount):
    def __init__(self,balance:int):
        super().__init__(balance)

    def withdraw(self,amount):
        raise Exception("You can't withdraw from FixedDepositAccount")

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited : {self.balance}")


s = SavingsAccount(100)
s.withdraw(100)
s.deposit(100)

fd = FixedDepositAccount(100)
fd.withdraw(100) # We are getting Exception when withdrew from FD which is not allowed
fd.deposit(100)