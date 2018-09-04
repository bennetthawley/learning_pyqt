import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Mozarella Ashbadger')

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))

        self.setCentralWidget(self.browser)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
