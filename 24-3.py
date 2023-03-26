# Задание 24-3
def bracket(s):
    if s.count('(') != s.count(')'):
        return False
    else:
        if s.find('(') > s.find(')'):
            return False
        else:
            return True

# Проверки - работают:
st = '()'
print(bracket(st))
st = ')(()))'
print(bracket(st))
st = '(())((()())())'
print(bracket(st))
st = '('
print(bracket(st))
st = '(()()('
print(bracket(st))
st = ')('
print(bracket(st))
st3 = ')'
print(bracket(st3))