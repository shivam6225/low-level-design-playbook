from DiscountStrategy import DiscountStrategy


class HoliSale(DiscountStrategy):

    def calculate_discount(self):
        print("Applying Holi discount of 15%")