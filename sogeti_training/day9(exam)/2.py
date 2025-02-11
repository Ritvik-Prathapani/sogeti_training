class BankAccount:
    def __init__(self):
        self.balence=100
    def deposit(self,amount):
        self.balence+=amount
        print(f"updated balence is {self.balence} ")
    def withdraw(self,amount):
        if(amount>self.balence):
            print("not enough balence")
        else:
            self.balence-=amount
        print(f"available balence is {self.balence}")
    def view_balance(self):
        print(f"balance is: {self.balence}")
    

usr1=BankAccount()
usr1.deposit(100)
usr1.withdraw(100)
usr1.view_balance()