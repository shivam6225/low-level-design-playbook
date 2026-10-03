from WithDrawable_Account import WithdrawableAccount


class SavingsAccount(WithdrawableAccount):

    def __init__(self,balance):
        super().__init__(balance)

    def withdraw(self,amount):
        if self.balance < amount:
            print("You can't withdraw , not enough balance")
        else:
            self.balance -= amount
            print(f"You withdrew , current balance : {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited , current balance : {self.balance}")