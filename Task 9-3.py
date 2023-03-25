# Задание 9-3
f = open('text.txt', 'r', encoding = 'utf-8')
fle = f.read()
d = {}
for a in fle:
    if d.get(a, None):
        d[a] += 1
    else:
        d[a] = 1
x = sorted(d.items(), key = lambda x: x[1], reverse = True)
print(sorted(x, key = lambda y: (-y[1], y[0])))
sym_fr = sorted(x, key = lambda y: (-y[1], y[0]))
for i in sym_fr:
    print(i)
f.close()
