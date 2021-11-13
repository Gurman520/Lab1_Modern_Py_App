import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor, QBrush, QPainterPath
from UI4_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        poi = self.centralwidget.size()
        self.We = poi.width()
        self.Hi = poi.height()
        print(self.We, " ", self.Hi)
        self.y = 0
        self.x = 0

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        poi = self.pushButton.pos()
        if abs(self.x - poi.x()) < 25 or abs(self.y - poi.y()) < 25:
            a = random.randint(30, 70)
            b = random.randint(30, 70)
            znak = random.randint(0, 1)
            if znak == 1:
                a *= -1
                b *= -1
            if self.We < poi.x() + a or poi.x() + a < 0:
                a = -a
            if self.Hi < poi.y() + b or poi.y() + b < 0:
                b = -b
            self.pushButton.move(poi.x() + a, poi.y() + b)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
