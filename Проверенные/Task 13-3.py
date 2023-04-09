# Задание 13-3
lst = list(map(int, input().split()))
def odds(lst):
    for i in lst:
        if i % 2 == 1:
            yield i
g = odds(lst)
for s in g:
    print(s, end = " ")
