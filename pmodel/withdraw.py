from plibs import *
from pheader import *
from pui import withdraw
from pmodel.addressesbooklist import AddressesBookListModel


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

        self.add_tab(self.addressesBookListModel, '')

        # data
        self.__address = ''

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)
        self.reset()

    @pyqtSlot(str)
    def address_changed(self, text: str):
        valid = True if len(text) == 42 else False
        self.__address = text
        QTimer().singleShot(1000, lambda: self.__search(text))
        super(WithdrawModel, self).address_changed(text, valid, valid is True)

    def __search(self, text: str):
        if self.__address == text:
            QObject.addressesBookListModel.searchChanged(text)
