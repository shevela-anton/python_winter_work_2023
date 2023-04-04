# Задание 12-3
def fun(x):
    s = [[int(c) for c in b.split('-')] for b in x.split(',')]
    return [i for rng in s for i in range(rng[0], rng[1] + 1)]


s = '1-2,4-4,3-6'
print(fun(s))