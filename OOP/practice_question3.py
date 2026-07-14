class Order:
    def __init__(self, item, price):
        self.item = item 
        self.price = price
    
    def __gt__(self, order2):
        if self.price > order2.price:
            return True
        else:
            return False
        
    

order1 = Order("pizza", 300)
order2 = Order("Burger", 500)

LargeOrder = order1.__gt__(order2) 

print(order1 > order2)
