import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('My Awesome App')

        widget = QCheckBox()
        widget.setCheckState(Qt.PartiallyChecked)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
