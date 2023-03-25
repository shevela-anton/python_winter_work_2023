# Задание 12-1
def min_max(x):
    return [j for j in range(0, len(x)) if x[j] == min(x)], \
        [i for i in range(0,len(x)) if x[i] == max(x)]
x = list(map(int, input('Введите список: ').split()))
print(min_max(x))
