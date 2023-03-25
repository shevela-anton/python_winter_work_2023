# Задание 14-2
def int_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + int_sum(n // 10)

n = int(input('Введите число: '))
print(int_sum(n))
