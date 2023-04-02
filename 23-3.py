# Задание 23-3
import itertools


def max_permut(lst):
    perm = list(itertools.permutations(lst))
    sp = []
    for i in perm:
        s = ''.join(map(str, i))
        sp.append(int(s))
        max_n = max(sp)
    return print(f'Самое большое число: {max_n}')


lst = [3, 11, 138]
max_permut(lst)
lst = [0, 1, 0]
max_permut(lst)