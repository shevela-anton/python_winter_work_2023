# Задание 11-3
def roman(n):
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM", "MMMM"]

    th = thousands[n // 1000]
    h = hundreds[n // 100 % 10]
    t = tens[n // 10 % 10]
    u = units[n % 10]

    return th + h + t + u


n = int(input('Введите число: '))
print('Римскими цифрами: ', roman(n))
