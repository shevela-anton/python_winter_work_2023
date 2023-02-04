# Задание к уроку 03.02, 8-2. Как второе правило сразу в лямбда засунуть, не догадался
lst = [[1, 5, 3], [2, 44, 1, 4], [3, 3]]
lst_s1 = sorted(lst, key = lambda x: len(x))
lst_s2 = []
for k, v in enumerate(lst_s1):
    lst_s2.append(sorted(v, reverse = True))
print(lst_s2)
