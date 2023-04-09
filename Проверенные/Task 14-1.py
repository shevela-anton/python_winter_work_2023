# Задание 14-1
def count(n):
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)

n = int(input('Введите число: '))
print(count(n))
