# Задание 7-2
def caesar(x, y):
    if x.isalpha():
        n = ord(x) + y % 26
        if n > 122:
            n -= 26
        return chr(n)
    return x


n = int(input('Введите смещение: '))
for i in input("Введите строку: "):
      print(caesar(i, n), end = '')
