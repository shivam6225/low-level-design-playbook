from AirTrafficControl import AirTrafficControl
from typing import List
from Airplane import Airplane


class ControlTower(AirTrafficControl):

    def __init__(self):
        self.__airplanes:List[Airplane] = []

    def register_airplane(self, airplane:Airplane):
        self.__airplanes.append(airplane)


    def send_message(self, message:str,sender:Airplane):
        for airplane in self.__airplanes:
            if airplane != sender:
                airplane.receive_message(message,sender)


