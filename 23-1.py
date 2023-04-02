# Задание 23-1
import itertools
s = 'aabbccddcc'
substr = set()
pol = []
for r in range(1, len(s) + 1):
    x = itertools.combinations(s, r)
    for i in x:
        substr.add(i)
for i in substr:
    if i == i[::-1]:
        pol.append(i)
mdl = max([len(i) for i in pol])
for i in pol:
    if len(i) == mdl:
        print(f'Палиндром с максимальной длиной = {mdl}: {i} ')