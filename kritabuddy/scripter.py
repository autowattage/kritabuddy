from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from krita import *
from time import sleep
import math
import random

speed = 3
h = 150
w = 85
class root(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # sprite
        #self.img = QPixmap("/home/bunnyguy/.var/app/org.kde.krita/data/krita/pykrita/kritabuddy/img/idle.png").scaledToHeight(200)
        self.img = QMovie("/home/bunnyguy/.var/app/org.kde.krita/data/krita/pykrita/kritabuddy/img/idle.gif")
        self.img.setScaledSize(QSize(w,h))
        self.img.start()
        self.walkimg = QMovie("/home/bunnyguy/.var/app/org.kde.krita/data/krita/pykrita/kritabuddy/img/walk.gif")
        self.walkimg.setScaledSize(QSize(w,h))
        self.walkimg.start()
        self.sprite = QLabel()
        self.sprite.setMovie(self.img)
        self.sprite.mousePressEvent = self.clicked

        # display sprite in widget
        self.layout = QVBoxLayout() 
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.sprite)
        self.setLayout(self.layout)
        self.setFixedSize(w,h)#self.img.width(),self.img.height())
        self.move(0,parent.height()-h)
        
    def clicked(self, event):
        self.hide()
        
    def localmove_end(self):
        self.sprite.setMovie(self.img)
        
    def localmove(self,dx,dy,dt):
        self.tween = QPropertyAnimation(self, b"pos", self)
        self.tween.finished.connect(self.localmove_end)
        self.tween.setDuration(dt)
        self.tween.setStartValue(QPoint(self.pos().x(), self.pos().y()))
        self.tween.setEndValue(QPoint(dx, dy))
        self.sprite.setMovie(self.walkimg)
        self.tween.start()
        

widget = root(Krita.instance().activeWindow().qwindow().centralWidget())
widget.show()
def scoot():
    dx=random.randrange(0,widget.parent().width()-w)
    dy=random.randrange(0,widget.parent().height()-h)
    dt=round(math.hypot(dx,dy)/speed*20)
    widget.localmove(dx,dy,dt)
    QTimer.singleShot(dt+500, scoot)

scoot()