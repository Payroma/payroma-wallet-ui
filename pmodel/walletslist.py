from plibs import *
from pheader import *
from pui import walletslist


class WalletsListModel(walletslist.UiForm):
    def __init__(self, parent):
        super(WalletsListModel, self).__init__(parent)

        self.setup()
