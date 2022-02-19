from plibs import *
from pheader import *
from pui import addressesbooklist
from pmodel import addressbookitem


class AddressesBookListModel(addressesbooklist.UiForm):
    def __init__(self, parent):
        super(AddressesBookListModel, self).__init__(parent)

        self.setup()

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

    def item_clicked(self, item: QListWidgetItem):
        widget = super(AddressesBookListModel, self).item_clicked(item)
