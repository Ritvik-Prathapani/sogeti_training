class notification:
    def send(self):
        print(f"notification recieved")
    
class emailnotification:
    def send(self):
        print(f"email notification recieved")

class smsnotification:
    def send(self):
        print(f"sms notification recieved")

obj1=notification()
obj1.send()

obj2=emailnotification()
obj2.send()

obj3=smsnotification()
obj3.send()