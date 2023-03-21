# Задание к уроку 30.01, 6-2. Пересечения
st1 = input().split(',')
st2 = input().split(',')
st1_set = set(st1)
st2_set = set(st2)
books = st1_set.intersection(st2_set)
print(len(books))
