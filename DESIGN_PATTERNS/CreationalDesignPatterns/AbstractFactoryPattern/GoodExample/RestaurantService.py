from CuisineFactory import *


class RestaurantService:

    def __init__(self,cuisine_factory: CuisineFactory):
        self.__factory = cuisine_factory

    def create_meal(self):
        starter = self.__factory.create_starter()
        main_course = self.__factory.create_main_course()
        dessert = self.__factory.create_dessert()

        starter.prepare()
        main_course.prepare()
        dessert.prepare()

    def set_cuisine_factory(self, cuisine_factory: CuisineFactory):
        self.__factory = cuisine_factory

north_indian = NorthIndianCuisineFactory()
restaurant_service = RestaurantService(north_indian)
restaurant_service.create_meal()

south_indian = SouthIndianCuisineFactory()
restaurant_service.set_cuisine_factory(south_indian)
restaurant_service.create_meal()