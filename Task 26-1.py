# Задание 26-1 22.03
def strcompare(a, b):

    count = 0  # счетчик различий
    a = list(a)
    b = list(b)
    if abs(len(a) - len(b)) <= 1:  # проверка на длину
        for i in range(len(a)):
            try:
                if a[i] == b[i]:
                    pass
                else:
                    count += 1
            except IndexError:  # если вышли out of range
                count += 1
                break
        if count <= 1:
            return True
        else:
            return False
    else:
        return False


a = 'abc'
b = 'abc'
print(strcompare(b, a))
