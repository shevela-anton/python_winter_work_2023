# Задание к уроку 25.01, 4-3
s = input().split('.')  # Разбиваем на два предложения построчно. Не догадался, как поступить в случае ! или ?
s1 = ''.join(s[0].split())  # Убираем пробелы
s2 = ''.join(s[1].split())  # Убираем пробелы
abc = list(s1.lower())
cba = list(s2.lower())
marks = '!-[)]{};%:,.(?/^&;*_""'  # Для удаления знаков препинания
for k, v in enumerate(abc):  # Цикл для удаления лишних символов
    if abc[k] in marks:
        abc.pop(k)
for k, v in enumerate(cba):
    if cba[k] in marks:
        cba.pop(k)
print(abc, cba)
if len(abc) == len(cba):
    if sorted(abc) != sorted(cba):  # Анаграмма будет в случае совпадения отсортированных букв.
        print(False)
    else:
        print(True)
else:
    print(False)
