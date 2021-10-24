import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI2_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        with open('myfile.txt', 'r') as file:
            lines = file.readlines()
        self.textBrowser.append("Не четный строки: \n")
        for i in range(0, len(lines), 2):
            self.textBrowser.append(lines[i])
        self.textBrowser.append("Четный строки: \n")
        for i in range(1, len(lines), 2):
            self.textBrowser.append(lines[i])
        self.pushButton.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
