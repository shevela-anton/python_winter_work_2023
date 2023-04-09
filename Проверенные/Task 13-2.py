# Задание 13-2
def polyndrom():
    i = 1
    while True:
        if (str(i) == str(i)[::-1]):
            yield i
            i += 1
        else:
            i+=1


n = int(input('Введите число: '))
p = polyndrom()
for x in range(n):
    print(next(p), end = ", ")
