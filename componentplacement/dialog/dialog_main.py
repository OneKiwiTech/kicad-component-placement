import wx
import wx.grid

from .dialog_base import ComponentPlacementDialog
from ..data.data import *

class DialogMain(ComponentPlacementDialog):
    def __init__(self, parent, board, version):
        ComponentPlacementDialog.__init__(self, parent)
        self.SetTitle('OnTech GUI')
        self.SetTitle('Component Placement %s' % version)
        self.board = board

    def OnInitDialog(self, event):
        field_list = get_field_data(self.board)
        self.comboDnp.Append(field_list)
        self.comboDnp.SetSelection(0)
        self.textStatus.LabelText = 'Init Done'

    def OnGenerateClick(self, event):
        self.textStatus.LabelText =  "Processing..."
        offset = self.radioOrigin.GetStringSelection()
        unit = self.radioUnit.GetStringSelection()
        dnp = self.comboDnp.GetValue()
        file = create_file(self.board, dnp, unit, offset)
        self.textStatus.LabelText = "Placement file: " + file
    
    def OnOriginChange(self, event):
        text = self.radioOrigin.GetStringSelection()
        self.textStatus.LabelText = "Origin: " + text

    def OnUnitChange(self, event):
        text = self.radioUnit.GetStringSelection()
        self.textStatus.LabelText = "Unit: " + text

    def OnDnpChange(self, event):
        text = self.comboDnp.GetValue()
        self.textStatus.LabelText = "DNP: " + text


