from PyQt5.QtWidgets import *
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('My Awesome App')
        label = QLabel('THIS IS AWESOME!!!')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
