# Задание 17-2
def upper_func(fu):
    def wrapper(*args, **kwargs):
        result = ''
        for x in args:
            if type(x) == str:
                result += x.upper() + ' '
        for x in kwargs:
            if type(kwargs[x]) == str:
                result += kwargs[x].upper() + ' '
        return result.split()
    return wrapper


@upper_func
def fu(*args, **kwargs):
    return
print(fu('jhj', 2, y = 'ae', a = 'zyz', e = 'Gfhj'))
