# Задание 15-2
import re
def gosnomer(x):
    lst = '[А, В, Е, К, М, Н, О, Р, С, Т, У, Х, A, B, E, K, M, H, O, H, C, T, Y, X]\d\d\d[А, В, Е, К, М, Н, О, Р, С, Т, У, Х, A, B, E, K, M, H, O, H, C, T, Y, X]{2}1?78'
    result = re.findall(lst, x)
    return result


s = 'A123BC78 X666XX178 Я123СТ178 ОЛнар 1253 А6245Т5438'
print(gosnomer(s))