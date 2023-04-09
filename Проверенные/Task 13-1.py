# Задание 13-1
def gen_list(n):
    for x in range(1, n):
        if x % 2 == 1:
            yield x
        else:
            yield -x

n = int(input('Введите число: '))
lst = gen_list(n)
for i in lst:
    print(str(i), end = ' ')
