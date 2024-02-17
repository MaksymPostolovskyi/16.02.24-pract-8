
class Product:
    def __init__(self, name, priceindollars, quantity):
        self.name = name
        self.price = priceindollars
        self.quantity = quantity

    
        
Аспірин = Product("Аспірин", 5, 30)
Білевугілля = Product("Біле вугілля", 0.50 , 50)
Лізак = Product("Лізак", 2, 40)






class Аптека():
    def __init__(self, name, location):
        self.location = location
        self.name = name
        self.inventory = {}
    
        
    
    

Аптека1 = Аптека("Подорожник", "Івано-Франківськ")
Аптека2 = Аптека("Сімейна аптека", "Тисмениця")


