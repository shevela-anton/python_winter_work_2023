# Задание 1-4 к уроку 18.01
x = int(input())
s = int(input())
q = x + s
w = x - s
e = x * s
r = x / s
t = x // s
print(q, w, e, r, t)
if q > w and q > e and q > r and q > t:
    print("Самое большое число - ", q)
elif w > q and w > e and w > r and w > t:
    print("Самое большое число - ", w)
elif e > q and e > w and e > r and e > t:
    print("Самое большое число - ", e)
elif r > q and r > w and r > e and r > t:
    print("Самое большое число - ", r)
elif t > q and t > w and t > r and t > e:
    print("Самое большое число - ", t)
