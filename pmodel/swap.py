from plibs import *
from pheader import *
from pui import swap


class SwapModel(swap.UiForm):
    def __init__(self, parent):
        super(SwapModel, self).__init__(parent)

        self.setup()
