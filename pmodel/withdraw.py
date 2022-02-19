from plibs import *
from pheader import *
from pui import withdraw
from pmodel.addressesbooklist import AddressesBookListModel


class WithdrawModel(withdraw.UiForm):
    def __init__(self, parent):
        super(WithdrawModel, self).__init__(parent)

        self.setup()

        # Tabs
        self.addressesBookListModel = AddressesBookListModel(self)

        self.add_tab(self.addressesBookListModel, '')

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)
        self.reset()

    @pyqtSlot(str)
    def address_changed(self, text: str):
        valid = True if len(text) == 42 else False
        super(WithdrawModel, self).address_changed(text, valid, valid is True)
