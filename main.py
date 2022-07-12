import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        self.MoveXY(1500,200)

        statusBar = self.CreateStatusBar(style=wx.BORDER_NONE)
        statusBar.SetStatusStyles([wx.SB_FLAT])
        statusBar.SetStatusText("This is the statusbar")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="DataView")
        self.frame.Show()
        return True


app = MyApp()
app.MainLoop()
