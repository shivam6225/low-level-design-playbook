from TransportMode import TransportMode


class TransportService:

    def __init__(self,mode:TransportMode):
        self.__mode = mode

    def set_mode(self,mode:TransportMode):
        self.__mode = mode

    def eta(self):
        return self.__mode.eta()

    def direction(self):
        return self.__mode.direction()
    
