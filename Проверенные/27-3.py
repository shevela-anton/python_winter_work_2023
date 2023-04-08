# Задание 27-3
result = []


def lstlen(lst):
    for i in lst:
        if type(i) == list:
            result.append('lst')
            lstlen(i)
        else:
            result.append(i)
    return len(result)


lst = [1, 2, [11, 22, [111, 222, [1111, 2222]]], 3]
#lst = [1, 2, [3, 4, [5]]]
#lst = [1, 2]
print(lstlen(lst))