import sys
import os
import statistics as st
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI3_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.pushButton.isDefault()
        name = self.FileName.text()
        if os.path.exists(name):
            if os.path.getsize(name) != 0:
                self.pushButton.setStyleSheet('background: green;')
                with open(name, 'r') as file:
                    lines = file.readlines()
                z = 0
                mass = []
                for li in lines:
                    for i in range(len(li)):
                        if li[i].isdigit():
                            z = z * 10 + int(li[i])
                            if not li[i+1].isdigit():
                                mass.append(z)
                                z = 0
            ma = max(mass)
            mi = min(mass)
            sr = st.mean(mass)
            self.MaxL.setText(f"{ma}")
            self.MinL.setText(f"{mi}")
            self.SrL.setText(f"{sr}")
            with open("output.txt", 'w') as f:
                z = str(ma) + " " + str(mi) + " " + str(sr)
                f.write(z)


        else:
            self.FileName.clear()
            self.pushButton.setStyleSheet('background: red;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
