# Задание 15-3
import re
def phone_finder(x):
    lst = '\+7\(812\)\d{3}-\d{4}|\+7\(921\)\d{3}-\d{4}|\+7\(812\)\d{3}-\d{2}-\d{2}|\+7\(921\)\d{3}-\d{2}-\d{2}'
    result = re.findall(lst, x)
    return result

st = "7(812)123-1111 +7(812)876-11-99 +7(921)111-4356 +7(921)097-55-66 +79213259930 +7(812)4G 921-812-921-332 +79213456534"
print(phone_finder(st))
