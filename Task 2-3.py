print('Введите целое число:')
n = int(input())
k = 1
for i in range(1, n + 1):
    k = i * k
    print(i, k) # Для проверки значений, не обязательно
print(f'Факториал числа {n} = {k}')
