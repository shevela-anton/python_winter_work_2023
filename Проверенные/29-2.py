# Задание 29-2
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def rotated(matrix, direction):
    if direction == 'left':
        lmatrx = [list(i) for i in zip(*matrix)]
        result = list(reversed(lmatrx))
    elif direction == 'right':
        rmatrx = list(reversed(matrix))
        result = [list(i) for i in zip(*rmatrx)]
    return result

print(rotated(matrix, 'left'))
print(rotated(matrix, 'right'))