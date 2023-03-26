# Задание 17-3
class Shape:

    def __init__(self, Colour, Square):
        self.Colour = Colour
        self.Square = Square

    def info(self):
        return self.Colour, self.Square

    def set_Colour(self, x):
        self.Colour = x

    def set_Square(self, y):
        self.Square = y




a = Shape('red', 5)
b = Shape('black', 90)
print(a.info(), b.info())
a.set_Colour('green')
b.set_Colour('white')
a.set_Square(35)
b.set_Square(100)
print(a.info(), b.info())
