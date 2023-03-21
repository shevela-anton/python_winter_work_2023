# Задание к уроку 27.01, 5-1. Треугольник Паскаля
n = int(input())
triangle = {}
for i in range(n + 1):
    y = [1]
    for k in range(1, i):
        y.append(int(triangle[i - 1][k - 1]) + int(triangle[i - 1][k]))
    if i > 0:
        y += [1]
    triangle[i] = y
for k, v in triangle.items():
    print(v)
