from NotificationChannel import NotificationChannel

class SMSService(NotificationChannel):
    def send(self,message):
        print(f"Sending SMS {message}")