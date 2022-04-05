from plibs import *
from pheader import *
from pui import historyitem


class HistoryItem(historyitem.UiForm):
    def __init__(self, parent):
        super(HistoryItem, self).__init__(parent)

        self.setup()
