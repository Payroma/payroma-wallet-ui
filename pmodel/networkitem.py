from plibs import *
from pheader import *
from pui import networkitem


class NetworkItem(networkitem.UiForm):
    def __init__(self, parent):
        super(NetworkItem, self).__init__(parent)

        self.setup()
