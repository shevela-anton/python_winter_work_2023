# Задание к уроку 25.01, 4-0
s = input().split()
abc = list(s[0])
cba = list(s[1])
cba = cba[::-1]
log = False
if len(abc) == len(cba):
   for i in range(len(abc)):
       if abc[i] != cba[i]:
           print(False)
           break
       else:
           log = True
else:
    print(False)
if log:
    print(log)
