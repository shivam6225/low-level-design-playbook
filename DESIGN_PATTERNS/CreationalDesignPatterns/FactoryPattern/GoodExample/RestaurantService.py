from FoodFactory import FoodFactory

class RestaurantService:

    def create_order(self,food_type:str):
        food = FoodFactory.create_food(food_type)
        if food is not None:
            food.prepare()
            return food
        else:
            return None


restaurant_service = RestaurantService()
restaurant_service.create_order("pizza")
restaurant_service.create_order("burger")
restaurant_service.create_order("pasta")