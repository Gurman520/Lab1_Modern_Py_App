import sys
import os
import statistics as st
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from UI4_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textBrowser.setReadOnly(False)
        self.OpenF.clicked.connect(self.getFileName)
        self.SaveF.clicked.connect(self.saveFile)
        self.CreateF.clicked.connect(self.createNewFile)

    def createNewFile(self):
        self.textBrowser.clear()

    def getFileName(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Выбрать файл", ".", "Text Files(*.txt)")
        print(filename)
        self.textBrowser.clear()
        with open(filename, 'r') as file:
            lines = file.readlines()
        for i in range(len(lines)):
            self.textBrowser.append(lines[i][:-1])

    def saveFile(self):
        filename, filetype = QFileDialog.getSaveFileName(self, "Сохранить файл", ".", "Text Files(*.txt)")
        print(filename)
        print(filetype)
        with open(filename, "w") as f:
            z = self.textBrowser.toPlainText()
            f.writelines(z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
