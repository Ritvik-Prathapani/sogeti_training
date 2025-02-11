#this is just a simulater so only the balance can be set by the user
balance=0

#this function is used to get the balance
def get_balance():
    global balance
    return balance

#this function is used to set the balance
def set_balance(new_balance):
    global balance
    balance=new_balance

#all the below functions are used to perfrom ATM operations
#this functiono is used to withdraw the money
def withdraw_money():
    my_balance=get_balance()
    amount=int(input("Enter the amount you want to withdraw: "))
    if amount>my_balance:
        print("Insufficient balance")
    else:
        set_balance(my_balance - amount)
        print("amount withdrawn successfully")
        print(f"Your new balance is {get_balance()}")

#this function is used to deposit the money
def deposit_money():
    amount=int(input("Enter the amount you want to deposit: "))
    set_balance(get_balance() + amount)
    print(f"Your new balance is {get_balance()}")

#this function is used to check the balance
def check_balance():
    print(f"Your balance is {get_balance()}")

#this code starts the progarm
def main():
    global balance
    function=0
    print("Set initial balance for your account")
    balance=int(input("Enter the initial balance: "))
    set_balance(balance)
    while(function!=4):
        function=int(input("Enter 1 to check balance\nEnter 2 to deposit money\nEnter 3 to withdraw money\nEnter 4 to exit\n: "))
        if function==1:
            check_balance()
        elif function==2:
            deposit_money()
        elif function==3:
            withdraw_money()
    if function==4:
        print("Thank you for using our ATM")

main() #this line runs the main function