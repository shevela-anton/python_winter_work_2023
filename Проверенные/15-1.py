# Задание 15-1
result = []
def key_finder(dct, n):
    for k,v in dct.items():
        if k == n:
            result.append(v)
        if type(v) == dict:
            key_finder(v, n)
    return result


dct = {1: 1, 2: 2, 3: {2: {22:{1:3,3:{15:2,2:15}}}, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11, 6: 22}}
n = int(input('Введите число: '))
print(key_finder(dct, n))