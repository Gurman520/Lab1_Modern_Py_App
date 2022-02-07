import sys
import difflib
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI5_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.hide()
        self.lineEdit.setReadOnly(True)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.lineEdit.show()
        normalized1 = self.plainTextEdit.toPlainText()
        normalized2 = self.plainTextEdit_2.toPlainText()
        matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
        result = matcher.ratio() * 100
        if int(result) < self.doubleSpinBox.value():
            self.lineEdit.setStyleSheet('background : #008000;;;;')
        else:
            self.lineEdit.setStyleSheet('background : #FF0000;;;;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())