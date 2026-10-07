from data import Data

class CSVParser(Data):

    def _dataParser(self):
        print("Parsing CSV")



csvParser = CSVParser()
csvParser._parse()