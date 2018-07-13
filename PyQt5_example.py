import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        view_menu = menubar.addMenu('View')

        view_status_action = QAction('View statusbar', self, checkable=True)
        view_status_action.setStatusTip('View statusbar')
        view_status_action.setChecked(True)
        view_status_action.triggered.connect(self.toggleMenu)

        view_menu.addAction(view_status_action)

        import_menu = QMenu('Import', self)
        import_action = QAction('Import mail', self)
        import_menu.addAction(import_action)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.setWindowIcon(QIcon('web.png'))

        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
