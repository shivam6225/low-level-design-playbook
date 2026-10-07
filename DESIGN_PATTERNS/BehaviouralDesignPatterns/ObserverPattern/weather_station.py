from typing import List

from DESIGN_PATTERNS.BehaviouralDesignPatterns.ObserverPattern.observer import Observer


class WeatherStation:

    def __init__(self):
        self.__temperatures =0
        self.__observers:List[Observer] = []


    def add_observer(self,new_observer:Observer):
        self.__observers.append(new_observer)

    def remove_observer(self,observer:Observer):
        self.__observers.remove(observer)


    def update_temperature(self,new_temp):
        self.__temperatures = new_temp
        self.notify_observers()


    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__temperatures)