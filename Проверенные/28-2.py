# Задание 28-2
def hem_len(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count


a = 'abc'
b = 'xyz'
print(hem_len(a, b))