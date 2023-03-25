# Задание 8-1
s = input("Введите код ДНК: ")
dna_changed = s.replace('АГ','ГА')
dna_changed = dna_changed.replace('ЦТ','ЦАГТ')
print(dna_changed)
