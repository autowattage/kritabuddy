from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from krita import *

class root(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setFixedSize(113,200)

        self.imgidle = QPixmap("/home/bunnyguy/.var/app/org.kde.krita/data/krita/pykrita/kritabuddy/img/idle.png")#.scaledToHeight(200)
        self.labelbutton = QLabel()
        self.labelbutton.setPixmap(self.imgidle)
        self.labelbutton.mousePressEvent = self.clicked

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.labelbutton)

    def clicked(self, event):
        print("owie")
    
class kritabuddy(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def open_window(self):
        root().show()

    def createActions(self, window):
        action = window.createAction("", "Toggle Kritabuddy")
        action.triggered.connect(self.open_window)
