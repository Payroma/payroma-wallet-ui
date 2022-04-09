from plibs import *
from pui import tokenitem


class TokenItem(tokenitem.UiForm):
    def __init__(self, parent):
        super(TokenItem, self).__init__(parent)

        self.setup()
