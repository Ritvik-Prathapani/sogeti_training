total_price=0
all_items=[]
def add_items():
    global total_price
    item=[]
    item_name=input("enter the item name: ")
    item_cost=int(input("enter the item cost: "))
    item.append(item_name)
    item.append(item_cost)
    all_items.append(item)
    total_price+=item_cost

def view_cart():
    print("welcome to cart")
    for i in all_items:
        for j in i:
            print(j,end=" ")
        print("\n")

def get_price():
    global total_price
    print(total_price)

def main():
    print("Welcome to shopping cart")
    option=0
    while(option!=4):
        option = int(input("Enter 1 to add items\nenter 2 to view cart\nenter 3 to see the overall price\n"))
        if(option==1):
            add_items()
        if(option==2):
            view_cart()
        if(option==3):
            get_price()
    if(option==4):
        print("Thank you for visiting")

main()