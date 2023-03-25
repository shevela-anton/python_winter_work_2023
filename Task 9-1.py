# Задание 9-1
rnk_val = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}
dnk = input('Введите код ДНК: ')
rnk = []
for i in dnk:
    if i in rnk_val:
        rnk += rnk_val.get(i)
rnk = ''.join(rnk)
print(f'Код РНК - {rnk}')
