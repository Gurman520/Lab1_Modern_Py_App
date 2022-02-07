import sys
from PyQt5.QtCore import QSettings, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI1_ui import Ui_MainWindow

ORGANIZATION_NAME = 'Example App'
ORGANIZATION_DOMAIN = 'example.com'
APPLICATION_NAME = 'QSettings program'
SETT = 'set'
SET2 = 'set2'
SET3 = 'set3'
SET_WINDOW = 'windows'
COUNT = 'count'


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        settings = QSettings("./test.ini", 1)
        windows = settings.value(SET_WINDOW, "0 0 616 581", type=str)
        self._geometry = map(int, windows.strip().split())
        self.setGeometry(*self._geometry)
        count = settings.value(COUNT, 0, type=int)
        count += 1
        if count % 10 == 0:
            QMessageBox.question(self, 'Message', f"Поздравляю, вы запустили приложение: {count} раз!",
                                 QMessageBox.Yes, QMessageBox.Yes)
            print(f"Поздравляю, вы запустили приложение: {count} раз!")
        settings.setValue(COUNT, count)
        check_state = settings.value(SETT, False, type=bool)
        radio_state = settings.value(SET2, -2, type=int)
        line_state = settings.value(SET3, '', type=str)
        self.checkBox.setChecked(check_state)
        self.buttonGroup.button(radio_state).click()
        self.textEdit.setText(line_state)
        print(self.centralwidget.geometry())
        self.checkBox.clicked.connect(self.save_check_box_settings)

    def save_check_box_settings(self):
        settings = QSettings("./test.ini", 1)
        print(self.checkBox.isChecked())
        settings.setValue(SETT, self.checkBox.isChecked())
        settings.sync()

    def closeEvent(self, event):
        settings = QSettings("./test.ini", 1)
        geometry = f"{self.geometry().x()} {self.geometry().y()} {self.geometry().width()} {self.geometry().height()}"
        print(self.buttonGroup.checkedId())
        print(self.textEdit.toPlainText())
        print(geometry)
        settings.setValue(SET3, self.textEdit.toPlainText())
        settings.setValue(SET2, self.buttonGroup.checkedId())
        settings.setValue(SET_WINDOW, geometry)
        settings.sync()


if __name__ == '__main__':
    QCoreApplication.setApplicationName(APPLICATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
