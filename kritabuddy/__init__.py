from krita import *
from .kritabuddy import *
Krita.instance().addExtension(kritabuddy(Krita.instance()))

# from .kritascript import *
# Krita.instance().addDockWidgetFactory(DockWidgetFactory("kritabuddy",DockWidgetFactoryBase.DockPosition.DockRight,kritabuddy))
