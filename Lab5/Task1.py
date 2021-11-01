import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QColor, QTransform, QPainter
from PyQt5.QtCore import Qt
from UI1_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.new_img = 'new.jpg'

        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        print(fname)
        self.pixmap = QPixmap(fname[0])
        self.pixmapp = self.pixmap
        self.img_s = fname[0]
        self.label.setPixmap(self.pixmap)
        self.radioButton.clicked.connect(self.red)
        self.radioButton_2.clicked.connect(self.green)
        self.radioButton_3.clicked.connect(self.blue)
        self.radioButton_4.clicked.connect(self.defult)
        self.Left.clicked.connect(self.left_rotate)
        self.right.clicked.connect(self.right_rotate)

    def red(self):
        self.img = Image.open(self.img_s)
        self.pixels = self.img.load()
        x, y = self.img.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = r, 0, 0
        self.img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.label.setPixmap(self.pixmap)

    def green(self):
        print(2)
        self.img = Image.open(self.img_s)
        self.pixels = self.img.load()
        x, y = self.img.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 0, g, 0
        self.img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.label.setPixmap(self.pixmap)

    def blue(self):
        print(3)
        self.img = Image.open(self.img_s)
        self.pixels = self.img.load()
        x, y = self.img.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 0, 0, b
        self.img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.label.setPixmap(self.pixmap)

    def defult(self):
        print(4)
        self.pixmap = self.pixmapp
        self.label.setPixmap(self.pixmap)

    def left_rotate(self):
        t = QTransform().rotate(-90)
        self.pixmap = QPixmap(self.pixmap.transformed(t))
        self.label.setPixmap(self.pixmap)

    def right_rotate(self):
        t = QTransform().rotate(+90)
        self.pixmap = QPixmap(self.pixmap.transformed(t))
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
