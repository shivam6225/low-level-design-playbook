from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from AirTrafficControl import AirTrafficControl

class Airplane:

    def __init__(self, flight_number: str, tower: "AirTrafficControl"):
        self.__flight_number = flight_number
        self.__tower = tower
        #Register plane to tower
        self.__tower.register_airplane(self)

    def send_message(self, message: str):
        self.__tower.send_message(message, self)

    def receive_message(self, message: str, who_sent: "Airplane"):
        print(f"{self.__flight_number} got {message} received from {who_sent.get_flight_number()}")

    def get_flight_number(self):
        return self.__flight_number