from plibs import *
from pheader import *
from pui import wallet
from pmodel.tokenslist import TokensListModel
from pmodel.walletdetails import WalletDetailsModel
from pmodel.addtoken import AddTokenModel


class GlobalEvents:
    walletChanged = None
    currentTabChanged = None


class WalletModel(wallet.UiForm):
    QObject.walletModel = GlobalEvents()

    def __init__(self, parent):
        super(WalletModel, self).__init__(parent)

        self.setup()

        # Events
        QObject.walletModel.walletChanged = self.wallet_changed
        QObject.walletModel.currentTabChanged = self.set_current_tab

        # Tabs
        self.tokensListModel = TokensListModel(self)
        self.walletDetailsModel = WalletDetailsModel(self)
        self.addTokenModel = AddTokenModel(self)

        self.add_tab(self.tokensListModel, Tab.WalletTab.TOKENS_LIST)
        self.add_tab(self.walletDetailsModel, Tab.WalletTab.WALLET_DETAILS)
        self.add_tab(self.addTokenModel, Tab.WalletTab.ADD_TOKEN)

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)

    @pyqtSlot()
    def deposit_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.DEPOSIT)

    @pyqtSlot()
    def withdraw_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WITHDRAW)

    @pyqtSlot()
    def stake_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.STAKE_LIST)

    @pyqtSlot()
    def details_clicked(self):
        super(WalletModel, self).details_clicked()
        self.set_current_tab(Tab.WalletTab.WALLET_DETAILS)

    @pyqtSlot()
    def add_token_clicked(self):
        super(WalletModel, self).add_token_clicked()
        self.set_current_tab(Tab.WalletTab.ADD_TOKEN)

    def wallet_changed(self, username: str, address: str):
        self.set_username(username)
        self.set_address(address)
        self.walletDetailsModel.set_address(address)
