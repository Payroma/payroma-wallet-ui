from plibs import *
from pheader import *
from pui import walletslist
from pmodel import walletitem


class WalletsListModel(walletslist.UiForm):
    def __init__(self, parent):
        super(WalletsListModel, self).__init__(parent)

        self.setup()

        # Test
        wallets = {
            '0x0000000000000000000000000000000000000000': 'Wallet1',
            '0x0000000000000000000000000000000000000001': 'Wallet2'
        }
        for address, username in wallets.items():
            item = walletitem.WalletItem(self)
            item.set_username(username)
            item.set_address(address)
            self.add_item(item)

    def add_new_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.ADD_WALLET)

    def item_clicked(self, item: QListWidgetItem):
        widget = super(WalletsListModel, self).item_clicked(item)
        QObject.loginModel.loginChanged(
            widget.get_username(), widget.get_address()
        )
        QObject.mainModel.currentTabChanged(Tab.LOGIN)
