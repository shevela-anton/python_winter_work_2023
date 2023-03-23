# Задание 26-1 22.03
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Описание')

        menubar1 = self.menuBar()
        fileMenu1 = menubar.addMenu('&Инструкция')

        menubar2 = self.menuBar()
        fileMenu1 = menubar.addMenu('&Помощь')

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Графическое приложение')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

