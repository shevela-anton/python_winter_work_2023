# Задание 25-2
def fun(lst):
    result = []
    for i in range(len(lst)):
        try:
            if lst[i + 1] - lst[i] != 1:
                result.append(lst[i + 1])
        except IndexError:
            break
    return result

# Проверки:
lst1 = [1,5,6,7,9,10]
print(fun(lst1))
lst = [1, 2, 3, 5, 6, 8, 9, 0, -9, -3, -2, -1, 6]
print(fun(lst))