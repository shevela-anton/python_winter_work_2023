# Задание 16-3
def title_dec(fu):
    def wrapper():
        s1 = fu()
        s2 = s1.title()
        return s2
    return wrapper()
@title_dec
def fun():
    return input('Введите текст: ')
print(fun)