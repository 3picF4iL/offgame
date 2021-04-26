from wx import *
from panels import *


class MainFrame(Frame):
    def __init__(self):
        super().__init__(parent=None, title="Offgame", size=(800, 600))
        panel = MainPanel(self)
        self.Show()


if __name__ == '__main__':
    app = App(False)
    frame = MainFrame()
    app.MainLoop()
del app

