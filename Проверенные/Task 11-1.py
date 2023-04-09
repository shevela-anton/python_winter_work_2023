# Задание 11-1
import calendar
year = 2023
hermitage = []
for month in range(1, 13):
    count = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        c = calendar.weekday(year, month, day)
        if c == 3:
            count += 1
            if count == 3:
                hermitage.append((year,month,day))
print(hermitage)
