import random
class Orders:
    def __init__(self, customer, **kwargs):
        self._order_id = random.randint(10000, 99999)  
        self.customer = customer  
        self.order_status = kwargs.get('order_status')
        self.order_date = kwargs.get('order_date')
        self.required_date = kwargs.get('required_date')
        self.shipped_date = kwargs.get('shipped_date')
        self.store_id = kwargs.get('store_id')
        self.staff_id = kwargs.get('staff_id')

    def display_order_details(self):
        print("\nOrder Details")
        print(f'Order ID: {self._order_id}')
        print(f'Customer ID: {self.customer._customer_id}')
        print(f'Order Status: {self.order_status}')
        print(f'Order Date: {self.order_date}')
        print(f'Required Date: {self.required_date}')
        print(f'Shipped Date: {self.shipped_date}')
        print(f'Store ID: {self.store_id}')
        print(f'Staff ID: {self.staff_id}')




