# Задание 29-3
def isomorph(x, y):
    dct1 = {}
    dct2 = {}
    if len(x) != len(y):
        return False
    for i, j in enumerate(x):
        if j in dct1:
            if y[i] != dct1[j]:
                return False
        else:
            dct1[j] = y[i]
        if y[i] in dct2:
            if j != dct2[y[i]]:
                return False
        else:
            dct2[y[i]] = j
    return True

print(isomorph('cosas', 'asdrd'))
print(isomorph('RAMBUNCTIOUSLY', 'THERMODYNAMICS'))
print(isomorph('AB', 'CC'))
print(isomorph('ABAB', 'CD'))