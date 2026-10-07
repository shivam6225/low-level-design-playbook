from DiscountStrategy import DiscountStrategy

class DiscountService:

    def __init__(self,discount_strategy:DiscountStrategy):
        self.discount_strategy = discount_strategy

    def set_strategy(self,new_discount_strategy:DiscountStrategy):
        self.discount_strategy = new_discount_strategy

    def process(self):
        self.discount_strategy.calculate_discount()