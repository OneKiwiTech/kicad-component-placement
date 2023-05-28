from ..model.model import Model
from ..view.view import ComponentPlacementView
from .logtext import LogText
import pcbnew
import wx
import sys
import logging
import logging.config

# https://github.com/weirdgyn/viastitching/blob/master/viastitching_dialog.py
class Controller:
    def __init__(self, board):
        self.view = ComponentPlacementView()
        self.board = board
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)
        self.fields = self.model.get_field_data()
        self.view.choiceDnp.Append(self.fields)
        self.view.choiceDnp.SetSelection(0)
        self.view.choiceDnp.Disable()
        self.InitGridCustom()
        self.logger.info('init done')

        # Connect Events
        self.view.buttonGenerate.Bind(wx.EVT_BUTTON, self.OnGeneratePressed)
        self.view.buttonClear.Bind(wx.EVT_BUTTON, self.OnClearPressed)
        self.view.radioOrigin.Bind(wx.EVT_RADIOBOX, self.OnOriginChange)
        self.view.radioDefault.Bind(wx.EVT_RADIOBUTTON, self.OnDefaultChange)
        self.view.radioOther.Bind(wx.EVT_RADIOBUTTON, self.OnOtherChange)
        self.view.choiceDnp.Bind(wx.EVT_CHOICE, self.OnDnpChange)
        self.view.gridCustom.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnGridCellClicked)

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    def InitGridCustom(self):
        rows = self.view.gridCustom.GetNumberRows()
        #self.view.gridCustom.DeleteRows(0, rows)
        self.fields.remove('<none>')
        self.view.gridCustom.AppendRows(len(self.fields))
        self.view.gridCustom.SetCornerLabelValue('Item')
        for row, field in enumerate(self.fields):
            #self.view.gridCustom.SetColSize(row, 100)
            self.view.gridCustom.SetCellValue(row, 1, field)
            self.view.gridCustom.SetCellAlignment(row, 1, wx.ALIGN_LEFT, wx.ALIGN_TOP)
            self.view.gridCustom.SetReadOnly(row, 1)
            self.view.gridCustom.SetCellValue(row, 0, "0")
            self.view.gridCustom.SetCellRenderer(row, 0, wx.grid.GridCellBoolRenderer())
    
    def GetCheckedFields(self):
        results = []
        for row in range(self.view.gridCustom.NumberRows):
            val = self.view.gridCustom.GetCellValue(row, 0)
            if val == "1":
                temp = self.view.gridCustom.GetCellValue(row, 1)
                results.append(temp)
        return results

    def OnGeneratePressed(self, event):
        self.logger.info('OnGeneratePressed')
        if self.model.default == 0:
            index = self.view.choiceDnp.GetSelection()
            self.model.dnp = str(self.view.choiceDnp.GetString(index))
        fields= self.GetCheckedFields()
        if len(fields) == 0:
            path = self.model.create_file()
            self.logger.info('Placement file: %s' %path)
        else:
            path = self.model.create_file_custom(fields)
            self.logger.info('Placement file custom: %s' %path)

    def OnClearPressed(self, event):
        self.view.textLog.SetValue('')

    def OnOriginChange(self, event):
        text = self.view.radioOrigin.GetStringSelection()
        self.logger.info('Origin: %s' %text)
        if text == 'Gird Origin':
            self.model.offset = 1
        elif text == 'Drill Origin':
            self.model.offset = 2
        elif text == 'Page Origin':
            self.model.offset = 3
        else:
            self.model.offset = 1
    
    def OnDefaultChange(self, event):
        self.logger.info('OnDefaultChange')
        self.model.default = 1
        self.view.choiceDnp.Disable()
    
    def OnOtherChange(self, event):
        self.logger.info('OnOtherChange')
        self.model.default = 0
        self.view.choiceDnp.Enable()
    
    def OnDnpChange(self, event):
        self.logger.info('OnDnpChange')
    
    def OnGridCellClicked(self, event):
        row = event.GetRow()
        col = event.GetCol() # col = -1
        if col == 0:
            val = self.view.gridCustom.GetCellValue(event.Row, event.Col)
            #val = "" if val else "1"
            if val == "" or val == "0":
                self.view.gridCustom.SetCellValue(event.Row, 0, "1")
            if val == "1":
                self.view.gridCustom.SetCellValue(event.Row, 0, "0")
        #value = str(row) + ' ' + str(col)
        #value = str(row) + ' ' + str(col)
        #self.logger.info('click: %s' %value)

    def init_logger(self, texlog):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)
        # and to our GUI
        handler2 = LogText(texlog)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s",
            datefmt="%Y.%m.%d %H:%M:%S",
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)
        return logging.getLogger(__name__)
