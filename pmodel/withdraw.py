from plibs import *
from pheader import *
from pcontroller import event
from pui import withdraw
from pmodel.addressesbooklist import AddressesBookListModel
from pmodel.addamount import AddAmountModel


class WithdrawModel(withdraw.UiForm, event.EventForm):
    def __init__(self, parent):
        super(WithdrawModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Tabs
        self.add_tab(AddressesBookListModel(self), '')
        self.add_tab(AddAmountModel(self), '')

    def hideEvent(self, a0: QHideEvent):
        super(WithdrawModel, self).hideEvent(a0)
        self.reset()

    def withdraw_address_changed(self, address: str):
        self.set_address(address)

    @pyqtSlot(str)
    def address_changed(self, text: str):
        QTimer().singleShot(1000, lambda: self.__address_changed(text))

    def __address_changed(self, text: str):
        valid = False
        if text != self.get_address_text():
            return

        if len(text) == 42:
            valid = True

        event.withdrawAddressChanged.notify(address=text)
        super(WithdrawModel, self).address_changed(text, valid, valid)
