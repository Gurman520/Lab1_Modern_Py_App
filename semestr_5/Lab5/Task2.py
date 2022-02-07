import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from UI2_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_img = 'new.png'
        self.setupUi(self)

        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        print(fname)
        self.img_s = fname[0]
        self.pixmap = QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)
        self.horizontalSlider.setValue(100)
        self.horizontalSlider.valueChanged[int].connect(self.val)

    def val(self, value):
        print(value)
        img = Image.open(self.img_s)
        img_s = img.copy()
        img_s.putalpha(value * 2)
        img_s.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
