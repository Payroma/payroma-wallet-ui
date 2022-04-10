from plibs import *
from pui import addressbookitem


class AddressBookItem(addressbookitem.UiForm):
    def __init__(self, parent):
        super(AddressBookItem, self).__init__(parent)

        self.setup()
