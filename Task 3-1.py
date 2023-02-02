# Задание к уроку 23.01, № 3-1
sum = 0
n = 0
while True:
    salary = int(input())
    if salary == 0:
        break
    sum += salary
    n = n + 1
avr = sum / n
print(avr)

