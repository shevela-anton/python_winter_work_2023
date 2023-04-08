# Задание 28-1
def inversion(a):
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if i < j and a[i] > a[j]:
                count += 1
    return count


a = [5, 4, 3, 2, 1]
#a = [1, 2, 3, 4, 5]
print(inversion(a))