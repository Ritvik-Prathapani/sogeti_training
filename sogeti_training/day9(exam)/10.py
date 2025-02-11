class electronics:
    def __init__(self,brand):
        self.brand=brand

class mobiledevice(electronics):
    def __init__(self,brand,generation):
        super().__init__(brand)
        self.generation=generation
    
    def print_info(self):
        print(f"brand: {self.brand} generation: {self.generation}")
    
class smartphone(mobiledevice):
    def __init__(self,brand,generation):
        super().__init__(brand,generation)
    def print_info(self):
        return super().print_info()

newphone=smartphone('iphone',5)
newphone.print_info()