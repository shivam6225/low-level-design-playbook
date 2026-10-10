from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Airplane import Airplane

class AirTrafficControl(ABC):

    @abstractmethod
    def register_airplane(self, airplane: "Airplane"):
        pass

    @abstractmethod
    def send_message(self, message: str, sender: "Airplane"):
        pass