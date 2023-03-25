# Задание к уроку 20.03, 25-1
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle('Месячный отчёт')
        self.setWindowOpacity(0.9)
        self.resize(400, 400)
        self.move(100, 100)
        widget = QLabel("Выберите отчётный период")
        font = widget.font()
        font.setPointSize(10)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        widget1 = QComboBox()
        widget1.addItems(["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                         "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])
        font = widget1.font()
        font.setPointSize(10)
        widget1.setFont(font)
        widget1.activated.connect(self.activated)
        widget1.currentTextChanged.connect(self.text_changed)

        button = QPushButton('Показать результат')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        layout = QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(widget1)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def activated(self, index):
        print("Номер месяца:", index + 1)

    def the_button_was_clicked(self):
        print(f'Результат за месяц')

    def text_changed(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
