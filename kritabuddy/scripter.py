from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from krita import *
from time import sleep
from pathlib import Path
import os
import random

speed = 0.025
class root(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # sprite
        self.sprite = QLabel()
        self.setdimensions()
        self.loadgif(Path(__file__).parent / "img" / "idle.gif")
        self.sprite.mousePressEvent = self.clicked

        # display sprite in widget
        self.layout = QVBoxLayout() 
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.sprite)
        self.setLayout(self.layout)
        self.setFixedSize(self.width, self.height)
        self.move(random.randrange(0,parent.width()-self.width),parent.height()-self.height)

    def setdimensions(self):
        self.img = QMovie(str(Path(__file__).parent / "img" / "idle.gif"))
        self.img.start()
        self.width = round(self.img.frameRect().width()/10)
        self.height = round(self.img.frameRect().height()/10)

    def loadgif(self, url):
        self.img = QMovie(str(url))
        self.img.setScaledSize(QSize(self.width, self.height))
        self.img.start()
        self.sprite.setMovie(self.img)
    
    def clicked(self, event):     
        self.setParent(None)
        
    def localmove_end(self):
        self.loadgif(Path(__file__).parent / "img" / "idle.gif")
        
    def localmove(self,dx,dy,dt):
        self.tween = QPropertyAnimation(self, b"pos", self)
        self.tween.finished.connect(self.localmove_end)
        self.tween.setDuration(dt)
        self.tween.setStartValue(QPoint(self.pos().x(), self.pos().y()))
        self.tween.setEndValue(QPoint(dx, dy))
        if self.pos().x() > dx:
            self.loadgif(Path(__file__).parent / "img" / "walk.gif")
        else:
            self.loadgif(Path(__file__).parent / "img" / "walk-flipped.gif")
        self.tween.start()

widget = root(Krita.instance().activeWindow().qwindow().centralWidget())
widget.show()

# move, sit, or stand
def loop():
    if widget.parent():
        match random.randint(0,2):
            case 0: # move to random position
                dx=random.randrange(0,widget.parent().width()-widget.width)
                dy=widget.parent().height()-widget.height
                dt=round(abs(dx-widget.pos().x())/speed)
                widget.localmove(dx,dy,dt)
                QTimer.singleShot(dt+random.randrange(500,3000), loop)
            case 1: # sit
                widget.loadgif(Path(__file__).parent / "img" / "sit.gif")
                QTimer.singleShot(random.randrange(3000,10000), loop)
            case 2: # idle
                QTimer.singleShot(random.randrange(500,10000), loop)

QTimer.singleShot(random.randrange(500,5000), loop)
