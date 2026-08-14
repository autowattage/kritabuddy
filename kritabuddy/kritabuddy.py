from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from krita import *

class krita_wakatime(Extension):
    def __init__(self, parent):
        super().__init__(parent)

        settings_layout = QVBoxLayout()

        self.settings = QDialog()
        self.settings.setWindowTitle("krita-buddy")
        self.settings.setLayout(settings_layout)
        
    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("", "krita-buddy")
        action.triggered.connect(self.open_settings)
