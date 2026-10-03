class PaymentProcessor:
    def pay(self,payment_method:str,amount:int):
        if payment_method == "UPI":
            print("Starting UPI Transaction")
        elif payment_method == "credit_card":
            print("Starting Credit Card Transaction")
        elif payment_method == "debit_card":
            print("Starting Debit Card Transaction")


payment_processor = PaymentProcessor()
payment_processor.pay(payment_method="UPI",amount=100)

#Suppose I want to add paypal in future
#I will need to modify the code which could lead to bug or changed behavior
