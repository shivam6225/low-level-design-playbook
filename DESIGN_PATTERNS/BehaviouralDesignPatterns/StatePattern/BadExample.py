from enum import Enum


class TransportMode(Enum):
    WALKING = "walking"
    BIKE = "bike"
    TRAIN = "train"

class TransportService:

    def __init__(self,transportMode:TransportMode):
        self._transportMode : TransportMode = transportMode

    def set_mode(self,transportMode:TransportMode):
        self._transportMode = transportMode

    def eta(self):
        if self._transportMode == TransportMode.WALKING:
            print("Walking will take 15 mins")
        elif self._transportMode == TransportMode.BIKE:
            print("Bike will take 10 mins")
        elif self._transportMode == TransportMode.TRAIN:
            print("Train will take 5 mins")

    def directions(self):
        if self._transportMode == TransportMode.WALKING:
            print("Go Straight and take left")
        elif self._transportMode == TransportMode.BIKE:
            print("Go to Flyover")
        elif self._transportMode == TransportMode.TRAIN:
            print("Go to Train Station")


transport_service = TransportService(TransportMode.WALKING)
transport_service.eta()
transport_service.directions()

transport_service.set_mode(TransportMode.BIKE)
transport_service.eta()
transport_service.directions()



