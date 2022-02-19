from plibs import *
from pheader import *
from pui import addressesbooklist


class AddressesBookListModel(addressesbooklist.UiForm):
    def __init__(self, parent):
        super(AddressesBookListModel, self).__init__(parent)

        self.setup()

    def item_clicked(self, item: QListWidgetItem):
        widget = super(AddressesBookListModel, self).item_clicked(item)
