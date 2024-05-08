# __init__ method is a magic method , it's the constractor that the attribute take everything in it automatically

class math :
    def __init__(self, name , price , quantity):
        
        assert price >= 0, f"price {price} is not >= zero , it's not avillable "
        assert quantity >= 0, f"price {quantity} is not >= zero , it's not avillable "
    
        self.name = name
        self.price = price
        self.quantity = quantity
        
            
            
    def calculate_total_price(self):
        return self.price * self.quantity
    

item1 = math("phone", -6, 1000)

print(item1.calculate_total_price())