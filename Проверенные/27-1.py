# Задание 27-1
n = int(input('Введите число от 1 до 18: '))
mat = [[0 for j in range(n)] for i in range(n)]
if n in range(1, 19):
    if n != 1:
        i = 0
        j = 0
        v = 0
        for k in range(n // 2):
            v += 1
            for j in range(k, n -1-k):
                mat[i][j] += v
            j += 1
            for i in range(k, n - 1 - k):
                mat[i][j] += v
            i = i + 1
            for j in range(n - 1 - k, k, -1):
                mat[i][j] += v
            j = j - 1
            for i in range(n - 1 - k, k, -1):
                mat[i][j] += v
        if n % 2 != 0:
            j += 1
            mat[i][j] = v + 1

        for i in range(n):
            for j in range(n):
                print(mat[i][j], ' ', end='')
            print()
    else:
        print(n)
else:
    print('Введено неправильное число!')
