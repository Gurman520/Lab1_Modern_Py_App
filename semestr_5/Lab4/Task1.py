import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI1_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if os.path.getsize('myfile.txt') != 0:
            with open('myfile.txt', 'r') as file:
                lines = file.readlines()
                z = random.choice(lines)
                self.textBrowser.setText(z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
