# Задание к уроку 20.03, 25-3
def Camel(x):
    x.lower()
    l = x.title()
    l = ''.join(l.split())
    return(l)

x = input('Введите строку: ')
print(Camel(x))
