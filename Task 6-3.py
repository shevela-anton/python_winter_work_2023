# Задание к уроку 30.01, 6-3.
# Сортировка символов. Алгоритм получился немного тяжеловесный, не докрутил до оптимизации, однако работает.
# Тут работа только с латиницей, на кириллицу и т.д. принцип будет тот же с кодировкой.
string = input()
s = list(string)  # Перевод строки в список
alph = []  # Пустые списки для записи сортировки
Alph_B = []
num = []
sym = []
for i, v in enumerate(s):  # Сортировка по коду символа
    if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
        alph.append(v)
    elif ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        Alph_B.append(v)
    elif ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
        num.append(v)
    else:
        sym.append(s[i])
alph_s = sorted(list(set(alph)))  # Получение уникального набора символов по порядку
Alph_B_s = sorted(list(set(Alph_B)))
num_s = sorted(list(set(num)))
sym_s = sorted(list(set(sym)))
alph_pr = ' '.join(alph_s)  # Получение финальной строки для печати
Alph_B_pr = ' '.join(Alph_B_s)
num_pr = ' '.join(num_s)
sym_pr = ' '.join(sym_s)
print(alph_pr)
print(Alph_B_pr)
print(num_pr)
print(sym_pr)
