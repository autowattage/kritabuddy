from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from krita import *

class kritabuddy(Extension):
    def __init__(self, parent):
        super().__init__(parent)
      
    def setup(self):
        pass

    def open_window(self):
        pass
    
    def createActions(self, window):
        action = window.createAction("", "kritabuddy")
        action.triggered.connect(self.open_window)
