from plibs import *
from pheader import *
from pui import walletdetails


class WalletDetailsModel(walletdetails.UiForm):
    def __init__(self, parent):
        super(WalletDetailsModel, self).__init__(parent)

        self.setup()
        self.reset()

        # Test
        self.set_data('0x0000000000000000000000000000000000000000', time.ctime())
        self.set_private_key('0000000000000000000000000000000000000000000000000000000000000000')

    @pyqtSlot()
    def back_clicked(self):
        QObject.walletModel.currentTabChanged(Tab.WalletTab.TOKENS_LIST)
