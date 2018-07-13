import sys

from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        new_action = context_menu.addAction("New")
        open_action = context_menu.addAction("Open")
        quit_action = context_menu.addAction("Quit")
        action = context_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_action:
            qApp.quit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
