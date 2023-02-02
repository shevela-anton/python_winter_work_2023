# Задание к уроку 23.01, № 3-2
num = int(input())
num_s = str(num)
lst = []
for i in range(len(num_s)):
    x = int(num_s[i])
    lst.append(x)
print(lst)
for i in range(0, 10):
    print(f"{i} - {lst.count(i)}")
