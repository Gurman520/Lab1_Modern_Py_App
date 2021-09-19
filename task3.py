import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Вычислить', self)
        self.input = QLineEdit(self)
        self.label = QLabel(self)
        self.cb1 = QCheckBox('Show button', self)
        self.cb3 = QCheckBox('Show label', self)
        self.cb2 = QCheckBox('Show Line', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Check_box_test')

        self.btn.resize(self.btn.sizeHint())
        self.btn.move(10, 60)

        self.input.move(10, 110)

        self.label.setText("Привет, неопознанный лев")
        self.label.move(10, 160)

        self.cb1.move(200, 60)
        self.cb1.toggle()
        self.cb1.stateChanged.connect(self.changeTitle)

        self.cb2.toggle()
        self.cb2.move(200, 110)
        self.cb2.stateChanged.connect(self.changeTitle)

        self.cb3.move(200, 160)
        self.cb3.toggle()
        self.cb3.stateChanged.connect(self.changeTitle)

    def changeTitle(self, state):
        if self.sender() == self.cb1:
            if self.cb1.isChecked():
                self.btn.show()
            else:
                self.btn.hide()

        if self.sender() == self.cb2:
            if self.cb2.isChecked():
                self.input.show()
            else:
                self.input.hide()
        if self.sender() == self.cb3:
            if self.cb3.isChecked():
                self.label.show()
            else:
                self.label.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
