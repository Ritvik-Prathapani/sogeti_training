import random
class OrderItems:
    def __init__(self, order, **kwargs):
        self._item_id = random.randint(100000, 999999)  
        self.order = order  
        self.product_id = kwargs.get('product_id')
        self.quantity = kwargs.get('quantity')
        self.list_price = kwargs.get('list_price')
        self.discount = kwargs.get('discount')

    def display_order_item_details(self):
        print("\nOrder Item Details ")
        print(f'Item ID: {self._item_id}')
        print(f'Order ID: {self.order._order_id}')
        print(f'Customer ID: {self.order.customer._customer_id}')
        print(f'Product ID: {self.product_id}')
        print(f'Quantity: {self.quantity}')
        print(f'List Price: {self.list_price}')
        print(f'Discount: {self.discount}')

    def calculate_total(self):
        total_price = self.quantity * self.list_price
        discounted_price = total_price - (total_price * (self.discount / 100))
        return discounted_price

