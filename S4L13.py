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

        navtb = QToolBar('Navigation')
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(QIcon(os.path.join('icons', 'arrow-180.png')),
                           'Back', self)
        back_btn.setStatusTip('Back to previous page')
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('icons', 'arrow-000.png')),
                           'Next', self)
        next_btn.setStatusTip('Forward to next page')
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction(
            QIcon(os.path.join('icons', 'arrow-circle-315.png')), 'Reload',
            self)
        reload_btn.setStatusTip('Reload current page')
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction(
            QIcon(os.path.join('icons', 'home.png')), 'Home',
            self)
        home_btn.setStatusTip('Navigate to home url')
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(
            QPixmap(os.path.join('icons', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addSeparator()

        navtb.addWidget(self.urlbar)

        stop_btn = QAction(QIcon(os.path.join('icons', 'cross-circle.png')),
                           'Stop', self)
        stop_btn.setStatusTip('Stop loading current page')
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        self.browser.urlChanged.connect(self.update_urlbar)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)

    def update_urlbar(self, q):

        if q.scheme() == 'https':
            self.httpsicon.setPixmap(
                QPixmap(os.path.join('icons', 'lock-ssl.png')))

        else:
            self.httpsicon.setPixmap(
                QPixmap(os.path.join('icons', 'lock-nossl.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName('Mozarella Ashbandger')
app.setOrganizationName('Mozarella Ashbandger')
app.setOrganizationDomain('Mozarella Ashbandger')

window = MainWindow()
window.show()
app.exec_()
