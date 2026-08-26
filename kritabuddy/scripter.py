from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from krita import *
from time import sleep

class root(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # sprite
        self.img = QPixmap("/home/bunnyguy/.var/app/org.kde.krita/data/krita/pykrita/kritabuddy/img/idle.png").scaledToHeight(200)
        self.sprite = QLabel()
        self.sprite.setPixmap(self.img)
        self.sprite.mousePressEvent = self.clicked

        # display sprite in widget
        self.layout = QVBoxLayout() 
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.sprite)
        self.setLayout(self.layout)
        self.setFixedSize(self.img.width(),self.img.height())
        
        # animation
        self.localmove(0,0,50,50,500)
        self.pos.start()
    def clicked(self, event):
        self.hide()
        
    def localmove(self, x,y,dx,dy,dt):
        self.pos = QPropertyAnimation(self, b"pos", self)
        self.pos.setDuration(dt)
        self.pos.setStartValue(QPoint(x, y))
        self.pos.setEndValue(QPoint(dx, dy))

print(Krita.instance().activeWindow().qwindow().centralWidget())
root(Krita.instance().activeWindow().qwindow().centralWidget()).show()
#root().show()