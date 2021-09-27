import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from UI1_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.buttonGroup.checkedId() != -1:
            self.label.setText(self.buttonGroup.checkedButton().text())
        if self.buttonGroup_2.checkedId() != -1:
            self.label_2.setText(self.buttonGroup_2.checkedButton().text())
        if self.buttonGroup_3.checkedId() != -1:
            self.label_3.setText(self.buttonGroup_3.checkedButton().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
