import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from UI5_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.y = 0
        self.x = 0
        self.pixmap = QPixmap('нло.jpg')
        self.label.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        pix = self.label.pos()
        self.x = pix.x()
        self.y = pix.y()
        if event.key() == Qt.Key_Up:
            print("Кнопка вверх", self.x, self.y - 20)
            self.label.move(self.x, self.y - 20)
        if event.key() == Qt.Key_Down:
            print("Кнопка вниз", self.x, self.y + 20)
            self.label.move(self.x, self.y + 20)
        if event.key() == Qt.Key_Left:
            print("Кнопка влево", self.x - 20, self.y)
            self.label.move(self.x - 20, self.y)
        if event.key() == Qt.Key_Right:
            print("Кнопка вправо", self.x + 20, self.y)
            self.label.move(self.x + 20, self.y)
        pix = self.label.pos()
        self.x = pix.x()
        self.y = pix.y()
        if self.x + self.label.width() / 2 < 0:
            self.label.move(int(self.width() - self.label.width() / 2), self.y)
        if self.x + self.label.width() / 2 > self.width():
            self.label.move(0, self.y)
        if self.y + self.label.height() / 2 < 0:
            self.label.move(self.x, int(self.height() - self.label.height() / 2))
        if self.y + self.label.height() / 2 > self.height():
            self.label.move(self.x, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
