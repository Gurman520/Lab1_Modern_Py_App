import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Вычислить', self)
        self.input_1 = QLineEdit(self)
        self.input_2 = QLineEdit(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Calculate_lite')

        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 90)
        self.btn.clicked.connect(self.hello)

        self.input_1.move(20, 90)

        self.input_2.move(20, 150)

    def hello(self):
        if "/ 0" in self.input_1.text():
            self.input_1.setText("error")
        elif self.input_1.text() != '':
            self.input_2.setText(f"{eval(self.input_1.text())}")
            self.input_1.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
