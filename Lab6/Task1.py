import csv
import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from Task1_ui_ui import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.school = []
        self.clas = []
        self.loadTable('rez.csv')
        self.pushButton.clicked.connect(self.sort)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(4)
            title1 = []
            title1.append(title[0])
            title1.append(title[1])
            title1.append(title[2])
            title1.append(title[7])
            self.tableWidget.setHorizontalHeaderLabels(title1)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    if j == 0 or j == 1 or j == 2 or j == 7:
                        if j == 7:
                            j = 3
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnHidden(0, True)
        self.load_num()

    def load_num(self):
        for row in range(self.tableWidget.rowCount()):
            str = self.tableWidget.item(row, 2).text()
            self.school.append(str[12] + str[13])
            self.clas.append(str[15] + str[16])
        self.school = list(set(self.school))
        self.clas = list(set(self.clas))
        self.school.sort()
        self.clas.sort()
        self.comboBox.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox.addItems(self.school)
        self.comboBox_2.addItems(self.clas)

    def sort(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHidden(i, False)
        s = []
        c = []
        print("sort")
        for row in range(self.tableWidget.rowCount()):
            str = self.tableWidget.item(row, 2).text()
            s.append(str[12] + str[13])
            c.append(str[15] + str[16])
        num_school = self.comboBox.currentText()
        num_class = self.comboBox_2.currentText()
        if num_school != "":
            for i in range(len(s)):
                if int(s[i]) != int(num_school):
                    self.tableWidget.setRowHidden(i, True)
                else:
                    rang = self.tableWidget.item(i, 0).text()
                    if rang == "1-4":
                        for z in range(1, 4, 1):
                            self.tableWidget.item(i, z).setBackground(QColor(255, 0, 0))
        if num_class != "":
            for i in range(len(c)):
                if int(c[i]) != int(num_class):
                    self.tableWidget.setRowHidden(i, True)
                else:
                    rang = self.tableWidget.item(i, 0).text()
                    if rang == "1-4":
                        for z in range(1, 4, 1):
                            self.tableWidget.item(i, z).setBackground(QColor(255, 0, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())