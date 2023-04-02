# Задание 27-2
class Item:

    def __init__(self, name, price, quantity):
        self.name = name.capitalize()
        self.price = price
        self.quantity = quantity
        self.total = self.price * self.quantity




x = Item('cup', 4, 2)
print(x.name)
print(x.price, x.quantity)
print(x.total)