import sys

from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('My Awesome App')

        widget = QLineEdit()
        widget.setPlaceholderText('Enter your text')
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        self.setCentralWidget(widget)

    def return_pressed(self):
        print('Return Pressed')

    def selection_changed(self):
        print('Selection changed')
        print(self.centralWidget().selectedText())

    def text_changed(self, t):
        print('Text changed....')
        print(t)

    def text_edited(self, s):
        print('Text edited....')
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
