# Задание 19-3
class Person:

    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self):
        return self.patronymic[::-1] + self.name[::-1] + self.surname[::-1]




p = Person('Иванов', 'Михаил', 'Федорович')
print(p)