from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import wallet
from pmodel.tokenslist import TokensListModel
from pmodel.walletdetails import WalletDetailsModel
from pmodel.addtoken import AddTokenModel


class WalletModel(wallet.UiForm):
    def __init__(self, parent):
        super(WalletModel, self).__init__(parent)

        self.setup()

        # Global Methods
        globalmethods.WalletModel._setData = self.set_data
        globalmethods.WalletModel._setCurrentTab = self.set_current_tab

        # Tabs
        self.tokensListModel = TokensListModel(self)
        self.walletDetailsModel = WalletDetailsModel(self)
        self.addTokenModel = AddTokenModel(self)

        self.add_tab(self.tokensListModel, Tab.WalletTab.TOKENS_LIST)
        self.add_tab(self.walletDetailsModel, Tab.WalletTab.WALLET_DETAILS)
        self.add_tab(self.addTokenModel, Tab.WalletTab.ADD_TOKEN)

    @pyqtSlot()
    def deposit_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.DEPOSIT)

    @pyqtSlot()
    def withdraw_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.WITHDRAW, recordable=False)

    @pyqtSlot()
    def stake_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.STAKE_LIST)

    @pyqtSlot()
    def history_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.HISTORY_LIST)

    @pyqtSlot()
    def swap_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.SWAP)

    @pyqtSlot()
    def details_clicked(self):
        super(WalletModel, self).details_clicked()
        globalmethods.WalletModel.setCurrentTab(Tab.WalletTab.WALLET_DETAILS)

    @pyqtSlot()
    def add_token_clicked(self):
        super(WalletModel, self).add_token_clicked()
        globalmethods.WalletModel.setCurrentTab(Tab.WalletTab.ADD_TOKEN)
