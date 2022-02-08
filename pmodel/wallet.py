from plibs import *
from pheader import *
from pui import wallet
from pmodel.tokenslist import TokensListModel


class GlobalEvents:
    walletChanged = None


class WalletModel(wallet.UiForm):
    QObject.walletModel = GlobalEvents()

    def __init__(self, parent):
        super(WalletModel, self).__init__(parent)

        self.setup()

        # Events
        QObject.walletModel.walletChanged = self.wallet_changed

        # Tabs
        self.add_tab(TokensListModel(self), Tab.WalletTab.TOKENS_LIST)

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)

    def wallet_changed(self, username: str, address: str):
        self.set_username(username)
        self.set_address(address)
