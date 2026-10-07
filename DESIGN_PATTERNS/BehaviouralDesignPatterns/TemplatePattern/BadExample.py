class CSVParser:

    def parse(self):
        self.openFile()

        print("Parsing file")

        self.closeFile()

    def openFile(self):
        print("Opening the file")

    def closeFile(self):
        print("Closing the file")


class JSONParser:

    def parse(self):
        self.openFile()

        print("Parsing JSON")

        self.closeFile()

    def openFile(self):
        print("Opening the JSON")

    def closeFile(self):
        print("Closing the JSON")


csvParser = CSVParser()
csvParser.parse()

jsonParser = JSONParser()
jsonParser.parse()

#Redundant code , and if any issue , you modify everywhere