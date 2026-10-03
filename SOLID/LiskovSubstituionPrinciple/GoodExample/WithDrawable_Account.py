from abc import  abstractmethod
from Account import Account

class WithdrawableAccount(Account):
    def __init__(self,balance:int):
        super().__init__(balance)

    @abstractmethod
    def withdraw(self,amount):
        pass