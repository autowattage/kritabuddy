from krita import *
from .kritabuddy6 import *
# from .kritabuddy5 import *

Krita.instance().addExtension(kritabuddy(Krita.instance()))
