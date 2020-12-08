from wx import *
from variables import *


class MainPanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)

        v_sizer = BoxSizer(VERTICAL)
        v_sizer.Add(ResPanel(self), 1, EXPAND)
        v_sizer.Add(QueuePanel(self), 1, EXPAND)
        v_sizer.Add(MenuBar(self), 1, EXPAND)

        self.SetSizer(v_sizer)


class ResPanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)


class QueuePanel(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)


class tab_Buildings(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)
        text = StaticText(self, -1, building_message, size=(EXPAND, 30), style=ALIGN_LEFT)
        listing_h = BoxSizer(VERTICAL)
        listing = BoxSizer(HORIZONTAL)
        listing_h.Add(text)

        for item in buildings:
            button = Button(self,
                            label=f'{item["Name"]}\n\n'
                                  f'Metal: {item["met_req"]}\n'
                                  f'Cristal: {item["crist_req"]}\n'
                                  f'Deuter: {item["deu_req"]}',
                            size=(100, 100),
                            style=ALIGN_LEFT)
            listing.Add(button)

        listing_h.Add(listing)
        self.SetSizer(listing_h)


class tab_Technology(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)
        text = StaticText(self, -1, technologies_message, size=(EXPAND, 30), style=ALIGN_LEFT)
        listing_h = BoxSizer(VERTICAL)
        listing = BoxSizer(HORIZONTAL)
        listing_h.Add(text)

        for item in technologies:
            button = Button(self,
                            label=f'{item["Name"]}\n\n'
                                  f'Metal: {item["met_req"]}\n'
                                  f'Cristal: {item["crist_req"]}\n'
                                  f'Deuter: {item["deu_req"]}',
                            size=(100, 100),
                            style=ALIGN_LEFT)
            listing.Add(button)

        listing_h.Add(listing)
        self.SetSizer(listing_h)

class tab_Ships(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)
        t = StaticText(self, -1, "Ships", (20, 20))


class tab_Defence(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)
        t = StaticText(self, -1, "Defence", (20, 20))


class MenuBar(Panel):
    def __init__(self, parent):
        Panel.__init__(self, parent)
        nb = Notebook(self)

        tab1 = tab_Buildings(nb)
        tab2 = tab_Technology(nb)
        tab3 = tab_Ships(nb)
        tab4 = tab_Defence(nb)

        nb.AddPage(tab1, "Buildings", )
        nb.AddPage(tab2, "Technology")
        nb.AddPage(tab3, "Ships")
        nb.AddPage(tab4, "Defence")

        h_sizer = BoxSizer()
        h_sizer.Add(nb, 1, EXPAND)
        self.SetSizer(h_sizer)
