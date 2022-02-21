from plibs import *
from pheader import *
from pui import withdraw
from pmodel.addressesbooklist import AddressesBookListModel
from pmodel.addamount import AddAmountModel


class GlobalEvents:
    addressChanged = None


class WithdrawModel(withdraw.UiForm):
    QObject.withdrawModel = GlobalEvents()

    def __init__(self, parent):
        super(WithdrawModel, self).__init__(parent)

        self.setup()

        # Events
        QObject.withdrawModel.addressChanged = self.set_address

        # Tabs
        self.addressesBookListModel = AddressesBookListModel(self)
        self.addAmountModel = AddAmountModel(self)

        self.add_tab(self.addressesBookListModel, '')
        self.add_tab(self.addAmountModel, '')

        # data
        self.__address = ''

    def hideEvent(self, event: QHideEvent):
        super(WithdrawModel, self).hideEvent(event)
        self.reset()

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)

    @pyqtSlot(str)
    def address_changed(self, text: str):
        valid = True if len(text) == 42 else False
        self.__address = text
        QTimer().singleShot(1000, lambda: self.__search(text))
        super(WithdrawModel, self).address_changed(text, valid, valid is True)

    def __search(self, text: str):
        if self.__address == text:
            QObject.addressesBookListModel.searchChanged(text)
