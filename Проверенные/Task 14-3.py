# Задание 14-3
def fun(n):
    print('*' * n)
    if n > 1:
        fun(n - 1)
    print('*' * n)

n = int(input('Введите число: '))
print(fun(n))