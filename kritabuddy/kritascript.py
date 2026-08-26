from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from krita import *

class kritabuddy(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("kritabuddy")
        # self.setTitleBarWidget(QWidget(self))
        # self.setFloating(True)

        self.imgidle = QPixmap("/home/bunnyguy/.var/app/org.kde.krita/data/krita/pykrita/kritabuddy/img/idle.png").scaledToHeight(200)
        self.labelbutton = QLabel()
        self.labelbutton.setPixmap(self.imgidle)
        self.labelbutton.mousePressEvent = self.clicked
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.labelbutton)

        self.rootwidget = QWidget(self)
        self.rootwidget.setLayout(self.layout)
        self.rootwidget.setFixedSize(113,200)
        self.setWidget(self.rootwidget)
        
    def clicked(self, event):
        print("owie")

    def canvasChanged(self, canvas):
        pass
        
# toggle vis
for docker in Krita.instance().dockers():
    if(docker.objectName() == 'kritabuddy'):
        docker.setVisible(docker.isVisible())
