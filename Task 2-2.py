# Задание 2-2 к уроку 20.01
lst = [10, 1765, 15, 0, -81]
print(lst)
minimum = lst[0]
for i in range(len(lst)):
    if lst[i] < minimum:
        minimum = lst[i]
print('Наименьшее число', minimum)
