from DiscountStrategy import DiscountStrategy


class DiwaliSale(DiscountStrategy):

    def calculate_discount(self):
        print("Applying Diwali discount of 20%")