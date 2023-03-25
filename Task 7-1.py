# Задание 7-1
import math
lst = list(map(int, input('Введите числf через пробел: ').split()))
nok = math.lcm(*lst)
print('Наименьшее общее кратное = ', nok)
