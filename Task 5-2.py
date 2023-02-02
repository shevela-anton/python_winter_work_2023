# # Задание к уроку 27.01, 5-2.
n = int(input())
dv = []
for i in range(1, (n // 2) + 1):  # Для ускорения работы делаем проверку до n / 2
    if n % i == 0:
        dv.append(i)
dv.append(n)  # Добавляем в список само число n
print(dv)
