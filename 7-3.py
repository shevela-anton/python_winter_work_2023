# Задание 7-3
def max3(x):
    res =[]
    for i in range(len(x)):
        for j in range(len(x[i])):
            res.append(x[i][j])
    res1 = set(res)
    result = sorted(list(res1))[len(res1) - 3:]
    return result

matrix = [[1, 6, 3], [4, 5, 4]]
print(max3(matrix))