from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from krita import *
from time import sleep

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
        self.sprite = QLabel()
        self.sprite.setMovie(self.img)
        self.sprite.mousePressEvent = self.clicked

        # display sprite in widget
        self.layout = QVBoxLayout() 
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.sprite)
        self.setLayout(self.layout)
        self.setFixedSize(w,h)#self.img.width(),self.img.height())
        
        self.move(parent.width()-w,parent.height()-h)
        # animation
        self.localmove(0,parent.height()-h,
                       parent.width()-w,parent.height()-h,30000)
        self.pos.start()
    def clicked(self, event):
        self.hide()
        
    def localmove(self, x,y,dx,dy,dt):
        self.pos = QPropertyAnimation(self, b"pos", self)
        self.pos.setDuration(dt)
        self.pos.setStartValue(QPoint(x, y))
        self.pos.setEndValue(QPoint(dx, dy))

root(Krita.instance().activeWindow().qwindow().centralWidget()).show()
#root().show()