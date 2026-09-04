from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from krita import *
from pathlib import Path
import random

# "the rig"
class character(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.speed = 0.025 # walk speed

        # sprite
        self.sprite = QLabel()
        self.setdimensions()
        self.setanim(Path(__file__).parent / "img" / "idle.gif")
        self.sprite.mousePressEvent = self.clicked

        # display sprite in widget
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0) # hide top bar
        self.layout.addWidget(self.sprite)
        self.setLayout(self.layout)
        self.setFixedSize(self.width, self.height)
        self.move(random.randrange(0,parent.width()-self.width),parent.height()-self.height)

    def setdimensions(self):
        self.img = QMovie(str(Path(__file__).parent / "img" / "idle.gif"))
        self.img.start()
        self.width = round(self.img.frameRect().width()/10)
        self.height = round(self.img.frameRect().height()/10)

    def setanim(self, url):
        self.img = QMovie(str(url))
        self.img.setScaledSize(QSize(self.width, self.height))
        self.img.start()
        self.sprite.setMovie(self.img)

    def clicked(self, event):
        self.hide()

    def walkdone(self):
        self.setanim(Path(__file__).parent / "img" / "idle.gif")

    def walkto(self,dx,dy,dt):
        self.tween = QPropertyAnimation(self, b"pos", self)
        self.tween.finished.connect(self.walkdone)
        self.tween.setDuration(dt)
        self.tween.setStartValue(QPoint(self.pos().x(), self.pos().y()))
        self.tween.setEndValue(QPoint(dx, dy))
        # flipping gif based on direction
        if self.pos().x() > dx:
            self.setanim(Path(__file__).parent / "img" / "walk.gif")
        else:
            self.setanim(Path(__file__).parent / "img" / "walk-flipped.gif")
        self.tween.start()

# "the controller"
class kritabuddy(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self): # impatiently wait for krita's gui to load
        try:
            self.widget = character(Krita.instance().activeWindow().qwindow().centralWidget())
        except:
            QTimer.singleShot(100, self.setup)
            
    # main function loop, runs while alive
    def loop(self):
        if self.widget.isVisible():
            match random.randint(0,2):
                case 0: # move to random position
                    self.dx = random.randrange(0, self.widget.parent().width()-self.widget.width)
                    self.dy = self.widget.parent().height() - self.widget.height
                    self.dt = round(abs(self.dx-self.widget.pos().x()) / self.widget.speed)
                    self.widget.walkto(self.dx, self.dy, self.dt)
                    QTimer.singleShot(self.dt+random.randrange(500,3000), self.loop)
                case 1: # sit
                    self.widget.setanim(Path(__file__).parent / "img" / "sit.gif")
                    QTimer.singleShot(random.randrange(3000,10000), self.loop)
                case 2: # idle
                    self.widget.setanim(Path(__file__).parent / "img" / "idle.gif")
                    QTimer.singleShot(random.randrange(500,10000), self.loop)

    def toggle_vis(self):
        if self.widget.isVisible():
            self.widget.hide()
        else:
            self.widget.show()
            QTimer.singleShot(random.randrange(500,5000), self.loop)
            
    # add extension to menu
    def createActions(self, window):
        self.action = window.createAction("", "Toggle Kritabuddy")
        self.action.triggered.connect(self.toggle_vis)
