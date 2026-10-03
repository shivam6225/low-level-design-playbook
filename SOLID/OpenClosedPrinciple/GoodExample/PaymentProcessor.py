from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount:int):
        pass

class UPI(PaymentMethod):
    def pay(self, amount:int):
        print(f"UPI: amount {amount}")

class CreditCard(PaymentMethod):
    def pay(self, amount:int):
        print(f"CreditCard: amount {amount}")

class DebitCard(PaymentMethod):
    def pay(self, amount:int):
        print(f"DebitCard: amount {amount}")


class PaymentProcessor():

    def process_payment(self, payment_method:PaymentMethod, amount:int):
        payment_method.pay(amount)


debit = DebitCard()
credit = CreditCard()

payment_processor = PaymentProcessor()
payment_processor.process_payment(debit,100)
payment_processor.process_payment(credit,100)

#I can easily add more payment method without changing anything in existing code

