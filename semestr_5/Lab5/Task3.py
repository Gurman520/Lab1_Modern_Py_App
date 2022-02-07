import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QInputDialog
import random
n = 0
random.seed(1)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global n
        n, ok_pressed = QInputDialog.getInt(
            self, "Введите количество цветов", "Сколько флагов?", 3, 3, 5, 1)
        if ok_pressed:
            self.setGeometry(300, 300, 200, 250)
            self.setWindowTitle('Рисование')

    def paintEvent(self, event):
        global n
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        global n
        # Задаем кисть
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(QColor(g, b, r))
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(QColor(g, r, b))
        qp.drawRect(30, 90, 120, 30)
        if n == 4:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.drawRect(30, 120, 120, 30)
            qp.setBrush(QColor(r, g, b))
        if n == 5:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.drawRect(30, 120, 120, 30)
            qp.setBrush(QColor(r, g, b))
            qp.drawRect(30, 150, 120, 30)
            qp.setBrush(QColor(g, r, b))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())