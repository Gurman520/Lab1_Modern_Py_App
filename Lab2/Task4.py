import sys

import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI4_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.StartButton.clicked.connect(self.start)
        self.pushButton.clicked.connect(self.run)
        self.pushButton.hide()

    def run(self):
        flag = 0
        count_r = int(self.after.text()) - int(self.buttonGroup.checkedButton().text())
        self.after.setText(f"{count_r}")
        if count_r == 0:
            flag = 1
        if flag != 1:
            step_r = count_r % 4
            time.sleep(2)
            if step_r == 0:
                count_r -= 1
                self.after.setText(f"{count_r}")
                self.robot.setText("1")
            else:
                count_r -= step_r
                self.after.setText(f"{count_r}")
                self.robot.setText(f"{step_r}")
                if count_r == 0:
                    flag = 2
        if flag != 0:
            time.sleep(0.3)
            self.pushButton.hide()
            self.radioButton.hide()
            self.radioButton_2.hide()
            self.radioButton_3.hide()
            self.label_2.hide()
            self.label.hide()
            self.label_3.hide()
            self.label_4.hide()
            self.Start_line.hide()
            self.robot.hide()
            if flag == 2:
                self.after.setText("Winner robot")
            if flag == 1:
                self.after.setText("Winner user")

    def start(self):
        global count
        count = self.Start_line.text()
        if count != "":
            self.after.setText(count)
            self.pushButton.show()
            self.StartButton.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
