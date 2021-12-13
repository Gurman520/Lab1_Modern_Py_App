from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, \
    QListView
import sys


class MyListWidget(QListWidget):
    def __init__(self, parent, max_items=float("inf")):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.max_items = max_items

    def dragEnterEvent(self, e):
        if e.source() != self and self.count() < self.max_items:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        temp = e.source().currentItem()
        self.addItem(temp.text())
        e.source().takeItem(e.source().row(e.source().currentItem()))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.appLayout = QVBoxLayout()
        self.myListWidget2 = MyListWidget(self, 4)
        self.myListWidget1 = MyListWidget(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 300)

        self.myListWidget1.setViewMode(QListView.IconMode)
        self.myListWidget2.setViewMode(QListView.ListMode)

        self.myListWidget1.setAcceptDrops(False)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(False)

        self.appLayout.setSpacing(10)

        self.appLayout.addWidget(self.myListWidget1)
        self.appLayout.addWidget(self.myListWidget2)

        for i in range(8):
            self.myListWidget1.addItem(QListWidgetItem("Item %d" % (i + 1)))

        self.setWindowTitle('Grouping App - Drag and Drop Example Application');
        self.setLayout(self.appLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())

