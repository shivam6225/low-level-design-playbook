class Logger:
    def __init__(self,file_name:str):
        self.file_name = file_name
        self.log_count = 0

    def log(self,text:str):
        self.log_count += 1
        print(f"Logger is logging {text} in file {self.file_name}")


#file - userservice
#file2 - txn
#file3 -staff

log1 = Logger("app.log")
log2 = Logger("app.log")
log3 = Logger("app.log")

log1.log("User is doing txn")
log2.log("Staff is banning someone")
log3.log("Bank is under service")

print(log1.log_count)
print(log2.log_count)
print(log3.log_count)
#This is wrong as they all are logging in same log file , log_count should have been 3
print(id(log1))
print(id(log2))
print(id(log3))
#All three are different objects
