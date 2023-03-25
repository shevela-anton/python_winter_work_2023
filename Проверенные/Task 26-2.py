# Задание 26-2 22.03
def dis(self):
    print(self.__dict__)

Par = type('Par', (object,), {'dis': dis})
A = Par()
A.dis()
Par.dis()
