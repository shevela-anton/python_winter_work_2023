# Задание 28-3
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        # перемещаем все диски, кроме нижнего, с начального стержня на промежуточный
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        # перемещаем башню с промежуточного стержня поверх наибольшего диска
        moveTower(height - 1, withPole, toPole, fromPole)

# печатает, что диск был передвинут с одного стержня на другой
def moveDisk(fp, tp):
    print("Перемещение диска от", fp, "к", tp)
n = 2  # число дисков
moveTower(n, "A", "B", "C")  # Три стрежня: A, B и C