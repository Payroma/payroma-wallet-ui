from plibs import *
from pheader import *
from pcontroller import globalmethods
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

    @pyqtSlot()
    def add_new_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.ADD_WALLET)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem):
        widget = super(WalletsListModel, self).item_clicked(item)
        globalmethods.LoginModel.setData(widget.get_username(), widget.get_address())
        globalmethods.WalletModel.setData(widget.get_username(), widget.get_address())
        globalmethods.WalletDetailsModel.setData(widget.get_address(), time.ctime())
        globalmethods.WalletDetailsModel.setPrivateKey('0' * 64)
        globalmethods.DepositModel.setData(widget.get_address(), 'Binance Smart Chain')
        globalmethods.MainModel.setCurrentTab(Tab.LOGIN, recordable=False)
