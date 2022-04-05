from plibs import *
from pheader import *
from pcontroller import event
from pui import walletdetails


class WalletDetailsModel(walletdetails.UiForm, event.EventForm):
    def __init__(self, parent):
        super(WalletDetailsModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Variables
        self.__address = None

    def hideEvent(self, a0: QHideEvent):
        super(WalletDetailsModel, self).hideEvent(a0)
        self.reset()
        self.set_data(self.__address, time.ctime())

    def wallet_changed_event(self, username: str, address: str):
        self.reset()
        self.set_data(address, time.ctime())
        self.__address = address

    @pyqtSlot()
    def back_clicked(self):
        event.walletTabChanged.notify(tab=Tab.WalletTab.TOKENS_LIST)

    @pyqtSlot()
    def private_key_clicked(self):
        super(WalletDetailsModel, self).private_key_clicked()
        self.set_private_key("0" * 66)
