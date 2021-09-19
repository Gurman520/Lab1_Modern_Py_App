import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit
from PyQt5.QtWidgets import QLabel

count = []
price = []
index = 0
indSuch = 0
indSup = 0
indSte = 0

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.btn3 = QPushButton('Добавить Суп', self)
        self.btn2 = QPushButton('Добавить стейк', self)
        self.label = QLabel(self)
        self.sum = QLabel(self)
        self.btn1 = QPushButton('Добавить Суши', self)
        self.initUI()

        self.name = QPlainTextEdit(self)
        self.name.move(170, 20)
        self.name.resize(100, 80)

        self.prisee = QPlainTextEdit(self)
        self.prisee.move(320, 20)
        self.prisee.resize(50, 80)

        self.countt = QPlainTextEdit(self)
        self.countt.move(280, 20)
        self.countt.resize(30, 80)

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Menu')

        self.label.setText("Итог: ")
        self.label.move(180, 150)
        self.sum.setText(" 0 ")
        self.sum.resize(50, 20)
        self.sum.move(220, 150)

        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.hello)

        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(20, 50)
        self.btn2.clicked.connect(self.hello)

        self.btn3.resize(self.btn3.sizeHint())
        self.btn3.move(20, 80)
        self.btn3.clicked.connect(self.hello)


    def hello(self):
        global count, indSuch, index, indSte, indSup, price
        if self.sender() == self.btn1:
            if "Суши" in self.name.toPlainText():
                count[indSuch] += 1
                price[indSuch] += 1200
                self.print_count()
                self.print_price()
            else:
                indSuch = index
                index += 1
                count.append(1)
                price.append(1200)
                self.name.setPlainText(self.name.toPlainText() + "Суши\n")
                self.print_count()
                self.print_price()
        if self.sender() == self.btn2:
            if "Стейк" in self.name.toPlainText():
                count[indSte] += 1
                price[indSte] += 2000
                self.print_count()
                self.print_price()
            else:
                indSte = index
                index += 1
                count.append(1)
                price.append(2000)
                self.name.setPlainText(self.name.toPlainText() + "Стейк\n")
                self.print_count()
                self.print_price()
        if self.sender() == self.btn3:
            if "Суп" in self.name.toPlainText():
                count[indSup] += 1
                price[indSup] += 300
                self.print_count()
                self.print_price()
            else:
                indSup = index
                index += 1
                count.append(1)
                price.append(300)
                self.name.setPlainText(self.name.toPlainText() + "Суп\n")
                self.print_count()
                self.print_price()
        self.sum.setText(f"{sum(price)}")


    def print_count(self):
        self.countt.setPlainText("")
        for i in range(len(count)):
            self.countt.appendPlainText(f"{count[i]}")

    def print_price(self):
        self.prisee.setPlainText("")
        for i in range(len(price)):
            self.prisee.appendPlainText(f"{price[i]}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())