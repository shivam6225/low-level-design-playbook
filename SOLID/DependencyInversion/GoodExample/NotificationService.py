from NotificationChannel import NotificationChannel

class NotificationService:

    def __init__(self,channel:NotificationChannel):
        #Tightly Coupled by the Email and SMS Service
        #Violation of Dependency Injection
        #There is no flexibility
        self.channel = channel


    def notify(self,message):
        self.channel.send(message)



