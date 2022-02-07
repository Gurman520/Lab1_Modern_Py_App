import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser


class Text(QTextBrowser):
    def __init__(self):
        super(Text, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, EnterEvent):
        print('Drag Enter')
        if EnterEvent.mimeData().hasText():
            EnterEvent.acceptProposedAction()

    def dragMoveEvent(self, MoveEvent):
        print('Drag Move')

    def dragLeaveEvent(self, LeaveEvent):
        print('Drag Leave')

    def dropEvent(self, DropEvent):
        print('Drag Drop')
        txt_path = DropEvent.mimeData().text().replace('file:///', '')

        with open(txt_path, 'r') as f:
            self.setText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Text()
    demo.show()
    sys.exit(app.exec_())
