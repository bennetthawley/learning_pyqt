import sys

from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('My Awesome App')

        button = QPushButton("Hello")
        button.pressed.connect(self.pushed_my_button)

        self.setCentralWidget(button)

    def contextMenuEvent(self, QContextMenuEvent):
        print('Context menu requested!')

    def pushed_my_button(self):
        print('Pressed it!')


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
