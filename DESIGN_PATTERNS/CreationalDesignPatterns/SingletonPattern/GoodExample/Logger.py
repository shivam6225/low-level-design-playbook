class Logger:
    #Class Variable
    __instance = None

    #new method is called to create object
    def __new__(cls,file_name:str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.file_name = file_name
            cls.__instance.log_count = 0
        return cls.__instance

    def log(self, text: str):
        self.log_count += 1
        print(f"Logger is logging {text} in file {self.file_name}")

    def get_log_count(self) -> int:
        return self.log_count


log1 = Logger("app.log")
print(f"log1 ={log1}, ID = {id(log1)}")
log1.log("Bye")
log2 = Logger("app.log")
print(f"log2 ={log2}, ID = {id(log2)}")
log2.log("Hi")
log3 = Logger("app.log")
print(f"log3 ={log3}, ID = {id(log3)}")
log3.log("Good")

print(log1.get_log_count())
print(log2.get_log_count())
print(log3.get_log_count())