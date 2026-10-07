from DiscountService import DiscountService
from diwali_sale import DiwaliSale
from holi_sale import HoliSale

diwali_sale = DiwaliSale()
ds = DiscountService(diwali_sale)
ds.process()
holi_sale = HoliSale()
ds.set_strategy(holi_sale)
ds.process()