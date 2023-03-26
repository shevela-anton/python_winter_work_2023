# Задание 16-1
import re
def abbreviation(x):
     lst = re.findall(r'\b[а-яА-Я]', x)
     result = (''.join(lst)).upper()
     return(result)


s = input('Введите строку: ')
print(abbreviation(s))