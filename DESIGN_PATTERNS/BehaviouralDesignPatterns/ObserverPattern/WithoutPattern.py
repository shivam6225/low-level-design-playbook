class PhoneDisplay:
    def update(self,new_temp):
        print(f"Phone Display updated : {new_temp}")


#When you add new Display , you need to change code in Weather Display
class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__phone_display = PhoneDisplay()

    def update_temperature(self,new_temp):
        self.__temperature = new_temp
        self.notify_display()

    def notify_display(self):
        self.__phone_display.update(self.__temperature)




ws = WeatherStation()
ws.update_temperature(30)

