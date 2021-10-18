import sys
import Password_class as ps
import Phone_class as ph
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_T6_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        passs = ps.pas()
        phon = ph.phone()
        flag_p = str(passs.check_password(self.passwo.text()))
        flag_n = str(phon.check_number(self.phone.text()))
        print("Тип пароля : ", type(flag_p))
        print("Тип номера : ", type(flag_n))
        flag_l = self.login.text()
        if flag_p == '1' and flag_n[0] == '+' and flag_l != '':
            self.Result.setText("Успешно")
            self.Result.setStyleSheet('background : #008000;;;;')
        else:
            if flag_p != '1':
                self.Result.setText(f"{flag_p}")
            if flag_n[0] != '+':
                self.Result.setText(f"{flag_n}")
            self.Result.setStyleSheet('background : #FF0000;;;;')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
