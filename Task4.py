import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',

                   'C': '-.-.', 'D': '-..', 'E': '.',

                   'F': '..-.', 'G': '--.', 'H': '....',

                   'I': '..', 'J': '.---', 'K': '-.-',

                   'L': '.-..', 'M': '--', 'N': '-.',

                   'O': '---', 'P': '.--.', 'Q': '--.-',

                   'R': '.-.', 'S': '...', 'T': '-',

                   'U': '..-', 'V': '...-', 'W': '.--',

                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.input_1 = QLineEdit(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 540, 300)
        self.setWindowTitle('Morze')
        x = 10
        for abc in range(65, 91):
            self.btn = QPushButton(chr(abc), self)
            self.btn.resize(20, 20)
            self.btn.move(x, 100)
            x += 20
            self.btn.clicked.connect(self.plus)

        self.input_1.resize(250, 20)
        self.input_1.move(20, 50)

    def plus(self):
        self.input_1.setText(self.input_1.text() + MORSE_CODE_DICT[self.sender().text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
