import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from UI3_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        name = self.lineEdit.text()
        print(name)
        phone = self.lineEdit_2.text()
        print(phone)
        self.listWidget.insertItem(1, name + " --- " + phone)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
