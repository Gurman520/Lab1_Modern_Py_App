import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QBrush, QPainterPath
from UI3_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.y = 0
        self.x = 0
        self.w = 0

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            print("пробел")
            self.w = 3
            self.do_paint = True
            self.repaint()
            self.do_paint = False

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            print("Левая")
            self.w = 1
            self.y = event.y()
            self.x = event.x()
            self.do_paint = True
            self.repaint()
            self.do_paint = False
        elif (event.button() == Qt.RightButton):
            print("правая")
            self.w = 2
            self.y = event.y()
            self.x = event.x()
            self.do_paint = True
            self.repaint()
            self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp, event)
            qp.end()

    def draw(self, qp, event):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        pr = random.randint(1, 100)
        print(self.x, self.y, 20, pr)
        if self.w == 1:
            qp.drawEllipse(self.x, self.y, pr, pr)
        if self.w == 2:
            qp.drawRect(self.x, self.y, pr, pr)
        if self.w == 3:
            x = random.randint(10, 100)
            y = random.randint(1, 100)
            path = QPainterPath()
            path.moveTo(self.x, self.y)
            path.lineTo(self.x, self.y + y)
            path.lineTo(self.x + x, self.y + (y / 2.0))
            path.lineTo(self.x, self.y)
            qp.setPen(Qt.NoPen)
            qp.fillPath(path, QBrush(QColor(r, g, b)))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
