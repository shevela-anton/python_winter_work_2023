# Задание 24-1
def sorting(lst):
    lst1 = lst
    result = []
    max = lst[0]
    while len(lst1) != 0:
        for k, v in enumerate(lst1):
            if v == min(lst1):
                result.append(v)
                lst.pop(k)

    return result

lst = [2, -5, 6, 1, 4, 7, 0, 78383]
print(sorting(lst))