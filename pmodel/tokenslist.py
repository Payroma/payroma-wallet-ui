from plibs import *
from pheader import *
from pui import tokenslist


class TokensListModel(tokenslist.UiForm):
    def __init__(self, parent):
        super(TokensListModel, self).__init__(parent)

        self.setup()

    def item_clicked(self, item: QListWidgetItem):
        widget = super(TokensListModel, self).item_clicked(item)
