# Задание к уроку 23.01, № 3-3
s = input()
lst = s.split()
count = 0
word = str()
for i in range(len(lst)):
    if len(lst[i]) > count:
        count = len(lst[i])
        word = lst[i]
print(count, word)
