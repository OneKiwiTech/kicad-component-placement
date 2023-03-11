import wx
import pcbnew
from onekiwi.controller.controller import Controller

filename = '/home/vanson/working/kicad/battery/bms-single-cell/bms-single-cell.kicad_pcb'

class SimplePluginApp(wx.App):
    def OnInit(self):
        try:
            board = pcbnew.LoadBoard(filename)
            controller = Controller(board)
            controller.Show()
            return True
        except OSError:
            print("OSError: Unable to open file for reading.")
            return 0

def main():
    app = SimplePluginApp()
    app.MainLoop()

    print("Done")

if __name__ == "__main__":
    main()