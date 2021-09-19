import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.input_2 = QLineEdit(self)
        self.btn = QPushButton('->', self)
        self.input_1 = QLineEdit(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Transfer word')

        self.btn.resize(self.btn.sizeHint())
        self.btn.move(155, 120)
        self.btn.clicked.connect(self.hello)

        self.input_1.move(20, 90)

        self.input_2.move(250, 90)

    def hello(self):
        if self.btn.text() == '->':
            self.input_2.setText(self.input_1.text())
            self.input_1.setText('')
            self.btn.setText('<-')
        else:
            self.input_1.setText(self.input_2.text())
            self.input_2.setText('')
            self.btn.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())