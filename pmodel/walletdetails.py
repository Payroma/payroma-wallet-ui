from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import walletdetails


class WalletDetailsModel(walletdetails.UiForm):
    def __init__(self, parent):
        super(WalletDetailsModel, self).__init__(parent)

        self.setup()
        self.reset()

        # Global Methods
        globalmethods.WalletDetailsModel._setData = self.set_data
        globalmethods.WalletDetailsModel._setPrivateKey = self.set_private_key

    @pyqtSlot()
    def back_clicked(self):
        globalmethods.WalletModel.setCurrentTab(Tab.WalletTab.TOKENS_LIST)
