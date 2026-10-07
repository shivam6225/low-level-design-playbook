from weather_station import WeatherStation
from tv_display import TVDisplay
from mobile_display import MobileDisplay

ws = WeatherStation()
tv = TVDisplay()

ws.add_observer(tv)
ws.update_temperature(30)

mobile_display = MobileDisplay()
ws.add_observer(mobile_display)

ws.update_temperature(35)

ws.remove_observer(tv)

ws.update_temperature(40)
