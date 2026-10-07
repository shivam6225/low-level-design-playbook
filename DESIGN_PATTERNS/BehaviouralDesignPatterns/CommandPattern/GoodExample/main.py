from chef import Chef
from pasta import PastaOrder
from pizza import PizzaOrder
from Waiter import Waiter


chef = Chef()
pasta = PastaOrder(chef)
pizza = PizzaOrder(chef)


waiter = Waiter()

waiter.take_order(pasta)

waiter.take_order(pizza)