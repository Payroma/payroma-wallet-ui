from plibs import *
from pheader import *
from pui import walletdetails


class WalletDetailsModel(walletdetails.UiForm):
    def __init__(self, parent):
        super(WalletDetailsModel, self).__init__(parent)

        self.setup()
        self.reset()

        # Test
        self.set_private_key('0000000000000000000000000000000000000000000000000000000000000000')
        self.set_date_created(time.ctime())

    @pyqtSlot()
    def back_clicked(self):
        QObject.walletModel.currentTabChanged(Tab.WalletTab.TOKENS_LIST)
