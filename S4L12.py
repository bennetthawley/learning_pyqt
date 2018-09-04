import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Mozarella Ashbadger')
        self.setWindowIcon(QIcon(os.path.join('icons', 'ma-icon-64.png')))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))

        self.setCentralWidget(self.browser)


app = QApplication(sys.argv)
app.setApplicationName('Mozarella Ashbandger')
app.setOrganizationName('Mozarella Ashbandger')
app.setOrganizationDomain('Mozarella Ashbandger')

window = MainWindow()
window.show()
app.exec_()
