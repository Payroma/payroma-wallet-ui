from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import addressesbooklist
from pmodel import addressbookitem


class AddressesBookListModel(addressesbooklist.UiForm):
    def __init__(self, parent):
        super(AddressesBookListModel, self).__init__(parent)

        self.setup()

        # Global Methods
        globalmethods.AddressesBookListModel._search = self.search

        # Test
        wallets = {
            '0x0000000000000000000000000000000000000000': 'Wallet1',
            '0x0000000000000000000000000000000000000001': 'Wallet2'
        }
        for address, username in wallets.items():
            item = addressbookitem.AddressBookItem(self)
            item.set_username(username)
            item.set_address(address)
            self.add_item(item)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem):
        widget = super(AddressesBookListModel, self).item_clicked(item)
        globalmethods.WithdrawModel.setAddress(widget.get_address())
