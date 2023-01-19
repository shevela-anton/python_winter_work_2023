# Задача 1-5
x = int(input())
s = int(input())
q = x+s
w = x-s
e = x*s
r = x/s
t = x//s
print(q, w, e, r, t)
list_val = [q, w, e, r, t]
list_val.sort()
print(list_val[-2])
