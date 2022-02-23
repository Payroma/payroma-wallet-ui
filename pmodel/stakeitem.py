from plibs import *
from pheader import *
from pui import stakeitem


class StakeItem(stakeitem.UiForm):
    def __init__(self, parent):
        super(StakeItem, self).__init__(parent)

        self.setup()

        # Data
        self.interface = None
