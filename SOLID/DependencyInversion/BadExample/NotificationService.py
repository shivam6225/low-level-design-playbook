from EmailService import EmailService
from SMSService import SMSService

class NotificationService:

    def __init__(self):
        #Tightly Coupled by the Email and SMS Service
        #Violation of Dependency Injection
        #There is no flexibility
        self.emailService = EmailService()
        self.smService = SMSService()

    def notifyByEmail(self,message):
        self.emailService.send_email(message)

    def notifyBySMS(self,message):
        self.smService.send_sms(message)


ns = NotificationService()
ns.notifyByEmail("Good Morning")
ns.notifyBySMS("Good Morning")

#Suppose you want to add WhatsAPP service -> you will need to modify the init directly

