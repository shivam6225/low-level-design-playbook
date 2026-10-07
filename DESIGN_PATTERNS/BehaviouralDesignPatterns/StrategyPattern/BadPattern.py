class DiscountService:

    #Change code to add new discount , violated O from SOLID
    def calculate_discount(self , discount_type:str):
        if discount_type =="diwali":
            print("Applying Diwali discount of 20%")
        elif discount_type =="first_order":
            print("Applying first order discount of 15%")
        else:
            print("No discount applied")