from cgitb import text
import wx
from .dialog import *
from ..kicad.board import get_current_unit
from ..version import version

class ComponentPlacementView(ComponentPlacementDialog):
    def __init__(self):
        ComponentPlacementDialog.__init__(self, None)
        self.SetTitle('Component Placement %s' % version)
        self.window = wx.GetTopLevelParent(self)

    def HighResWxSize(self, window, size):
        """Workaround if wxWidgets Version does not support FromDIP"""
        if hasattr(window, "FromDIP"):
            return window.FromDIP(size)
        else:
            return size
