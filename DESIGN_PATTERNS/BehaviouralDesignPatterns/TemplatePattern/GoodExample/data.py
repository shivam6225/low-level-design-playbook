from abc import ABC, abstractmethod

class Data(ABC):

    def _parse(self):
        self._open()
        #Parse
        self._dataParser()
        self._close()

    def _open(self):
        print("Opening the file")

    def _close(self):
        print("Closing the file")

    @abstractmethod
    def _dataParser(self):
        pass
