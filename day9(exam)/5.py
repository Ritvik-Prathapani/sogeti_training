class product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def check_available(self,user_quantity):
        if(user_quantity>self.stock):
            print("not available")
        else:
            print("available")
        
carrots=product('carrots',200,500)
carrots.check_available(500)
carrots.check_available(600)