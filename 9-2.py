# Задание 9-2
vowels = ['а','у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
word = input('Введите слово для сравнения: ')
lst = []
for i in range(len(word)):
    if word[i] in vowels:
        lst.append(i)
n = int(input('Введите число слов: '))
i = 1
di = {}
diin = {}
si = []
while i <= n:
    di[i] = input(f'Слово {i}: ')
    i += 1
for w in di.values():
    for i in range(len(w)):
        if w[i] in vowels:
            si.append(i)
    diin[w] = si
    si = []
like = []
for key in diin:
    if diin[key] == lst:
        like.append(key)
print('Похожие слова: ' + ', '.join(like))