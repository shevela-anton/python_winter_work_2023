# Задание к уроку 25.01, 4-1. Калькулятор
s = input().split(' ')
print(s)
x = float(s[0])
y = float(s[2])
op = s[1]
if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    if y == 0:
        print("Деление на ноль!")
    else:
        print(x / y)
