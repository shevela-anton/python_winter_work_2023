# Задание 19-1
import itertools
lst = [50, 100, 200, 500, 1000, 5000]
summ = []
for x in (itertools.combinations(lst, 3)):
    summ.append(sum(list(x)))
print(summ)