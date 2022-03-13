from plibs import *
from pheader import *
from pcontroller import url_open, globalmethods
from pui import main
from pmodel.walletslist import WalletsListModel
from pmodel.addwallet import AddWalletModel
from pmodel.settings import SettingsModel
from pmodel.networkslist import NetworksListModel
from pmodel.addnetwork import AddNetworkModel
from pmodel.login import LoginModel
from pmodel.authenticator import AuthenticatorModel
from pmodel.wallet import WalletModel
from pmodel.stakelist import StakeListModel
from pmodel.stakepair import StakePairModel
from pmodel.authenticatorsetup import AuthenticatorSetupModel
from pmodel.deposit import DepositModel
from pmodel.withdraw import WithdrawModel
from pmodel.swap import SwapModel
from pmodel.historylist import HistoryListModel
from pmodel.transactionsender import TransactionSenderModel


class MainModel(main.UiForm):
    def __init__(self, parent):
        super(MainModel, self).__init__(parent)

        self.setup()

        # Global Methods
        globalmethods.MainModel._setCurrentTab = self.set_current_tab
        globalmethods.MainModel._setThemeMode = self.set_theme_mode

        # Tabs
        self.add_tab(WalletsListModel(self), Tab.WALLETS_LIST)
        self.add_tab(AddWalletModel(self), Tab.ADD_WALLET)
        self.add_tab(SettingsModel(self), Tab.SETTINGS)
        self.add_tab(NetworksListModel(self), Tab.NETWORKS_LIST)
        self.add_tab(AddNetworkModel(self), Tab.ADD_NETWORK)
        self.add_tab(LoginModel(self), Tab.LOGIN)
        self.add_tab(AuthenticatorModel(self), Tab.AUTHENTICATOR)
        self.add_tab(WalletModel(self), Tab.WALLET)
        self.add_tab(StakeListModel(self), Tab.STAKE_LIST)
        self.add_tab(StakePairModel(self), Tab.STAKE_PAIR)
        self.add_tab(AuthenticatorSetupModel(self), Tab.AUTHENTICATOR_SETUP)
        self.add_tab(DepositModel(self), Tab.DEPOSIT)
        self.add_tab(WithdrawModel(self), Tab.WITHDRAW)
        self.add_tab(SwapModel(self), Tab.SWAP)
        self.add_tab(HistoryListModel(self), Tab.HISTORY_LIST)
        self.add_tab(TransactionSenderModel(self), Tab.TRANSACTION_SENDER)

        self.__previousTabs = []
        self.__latestTab = None

    @pyqtSlot()
    def back_clicked(self):
        self.__latestTab = self.__previousTabs.pop()
        super(MainModel, self).set_current_tab(self.__latestTab)

    @pyqtSlot()
    def home_clicked(self):
        self.__previousTabs.clear()
        super(MainModel, self).set_current_tab(Tab.WALLETS_LIST)

    @pyqtSlot()
    def settings_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.SETTINGS)

    @pyqtSlot()
    def minimize_clicked(self):
        self.showMinimized()

    @pyqtSlot()
    def exit_clicked(self):
        self.close()

    @pyqtSlot()
    def invest_clicked(self):
        url_open(Website.PAYROMA)

    def default_theme(self):
        pass

    def set_current_tab(self, name: str, recordable: bool = True):
        super(MainModel, self).set_current_tab(name)

        if not self.__previousTabs:
            self.__latestTab = Tab.WALLETS_LIST

        if not self.__previousTabs or self.__previousTabs[-1] != self.__latestTab:
            self.__previousTabs.append(self.__latestTab)

        if recordable:
            self.__latestTab = name
