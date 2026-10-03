from SMSService import SMSService
from EmailService import EmailService
from NotificationService import NotificationService

smsService = SMSService()

notificationService = NotificationService(smsService)
notificationService.notify("Good Morning")

emailService = EmailService()
notificationService2 = NotificationService(emailService)
notificationService2.notify("Good Morning")