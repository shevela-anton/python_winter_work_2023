# Задание 22-3
import keyword
kw = keyword.kwlist
s = input().split()
result = []
for i in s:
    if i in kw:
        result.append('<kw>')
    else:
        result.append(i)
print(' '.join(result))