from plibs import *
from pheader import *
from pui import walletslist
from pmodel import walletitem


class WalletsListModel(walletslist.UiForm):
    def __init__(self, parent):
        super(WalletsListModel, self).__init__(parent)

        self.setup()

    def add_new_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.ADD_WALLET)
