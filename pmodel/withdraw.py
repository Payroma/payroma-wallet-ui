from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import withdraw
from pmodel.addressesbooklist import AddressesBookListModel
from pmodel.addamount import AddAmountModel


class WithdrawModel(withdraw.UiForm):
    def __init__(self, parent):
        super(WithdrawModel, self).__init__(parent)

        self.setup()

        # Global Methods
        globalmethods.WithdrawModel._setAddress = self.set_address

        # Tabs
        self.add_tab(AddressesBookListModel(self), '')
        self.add_tab(AddAmountModel(self), '')

        # data
        self.__address = ''

    def hideEvent(self, event: QHideEvent):
        super(WithdrawModel, self).hideEvent(event)
        self.reset()

    @pyqtSlot(str)
    def address_changed(self, text: str):
        valid = True if len(text) == 42 else False
        self.__address = text
        QTimer().singleShot(1000, lambda: self.__search(text))
        super(WithdrawModel, self).address_changed(text, valid, valid is True)

    def __search(self, text: str):
        if self.__address == text:
            globalmethods.AddressesBookListModel.search(text)
