class payment:
    def pay(self):
        print(f"payment done")

class creditcardpayment(payment):
    def pay(self):
        print(f"payment done using credit card")

class paypalpayment(payment):
    def pay(self):
        print(f"payment done using paypal")

class bitcoinpayment(payment):
    def pay(self):
        print(f"payment done using bitcoin")
    
obj1=creditcardpayment()
obj1.pay()

obj2=paypalpayment()
obj2.pay()

obj3=bitcoinpayment()
obj3.pay()

