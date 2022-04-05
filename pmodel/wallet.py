from plibs import *
from pheader import *
from pcontroller import event
from pui import wallet
from pmodel.tokenslist import TokensListModel
from pmodel.walletdetails import WalletDetailsModel
from pmodel.addtoken import AddTokenModel


class WalletModel(wallet.UiForm, event.EventForm):
    def __init__(self, parent):
        super(WalletModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Tabs
        self.add_tab(TokensListModel(self), Tab.WalletTab.TOKENS_LIST)
        self.add_tab(WalletDetailsModel(self), Tab.WalletTab.WALLET_DETAILS)
        self.add_tab(AddTokenModel(self), Tab.WalletTab.ADD_TOKEN)

    def wallet_changed_event(self, username: str, address: str):
        self.reset()
        self.set_data(username, address)

    def wallet_tab_changed_event(self, tab: str):
        self.set_current_tab(tab)

    @pyqtSlot()
    def deposit_clicked(self):
        event.mainTabChanged.notify(tab=Tab.DEPOSIT)

    @pyqtSlot()
    def withdraw_clicked(self):
        event.mainTabChanged.notify(tab=Tab.WITHDRAW, recordable=False)

    @pyqtSlot()
    def stake_clicked(self):
        event.mainTabChanged.notify(tab=Tab.STAKE_LIST)

    @pyqtSlot()
    def history_clicked(self):
        event.mainTabChanged.notify(tab=Tab.HISTORY_LIST)

    @pyqtSlot()
    def swap_clicked(self):
        event.mainTabChanged.notify(tab=Tab.SWAP)

    @pyqtSlot()
    def details_clicked(self):
        super(WalletModel, self).details_clicked()
        event.walletTabChanged.notify(tab=Tab.WalletTab.WALLET_DETAILS)

    @pyqtSlot()
    def add_token_clicked(self):
        super(WalletModel, self).add_token_clicked()
        event.walletTabChanged.notify(tab=Tab.WalletTab.ADD_TOKEN)
