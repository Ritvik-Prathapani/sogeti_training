import random
class Customer:
    def __init__(self, **kwargs):
        self._customer_id = random.randint(1000, 9999)  
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.phone = kwargs.get('phone')
        self.email = kwargs.get('email')
        self.street = kwargs.get('street')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.zip_code = kwargs.get('zip_code')

    def display_details(self):
        print("\n")
        print("Customer Details")
        print(f'Customer ID: {self._customer_id}')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')
        print(f'Street: {self.street}')
        print(f'City: {self.city}')
        print(f'State: {self.state}')
        print(f'Zip Code: {self.zip_code}')




