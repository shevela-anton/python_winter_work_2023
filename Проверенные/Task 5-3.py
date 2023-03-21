# Задание к уроку 27.01, 5-2.
fib = [1, 1]
n = int(input())
for i in range(2, n + 1):
    f = fib[i - 1] + fib[i - 2]
    fib.append(f)
print(fib[0: n + 1])
