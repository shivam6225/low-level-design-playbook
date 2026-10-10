class AirplaneDemo:
    def __init__(self, flight_number:str):
        self.__flight_number = flight_number

    def send_message(self ,msg: str ,a:Airplane):
        print(f"{self.__flight_number} is sending {msg} to {a.get_flight_number()}")

    def get_flight_number(self) -> str:
        return self.__flight_number

spicejet = AirplaneDemo("spice")
indigo = AirplaneDemo("indigo")
airIndia = AirplaneDemo("airIndia")

spicejet.send_message("Landing on runway", airIndia)
indigo.send_message("Landing on runway", airIndia)