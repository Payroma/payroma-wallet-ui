from plibs import *
from pheader import *
from pcontroller import event
from pui import walletslist
from pmodel import walletitem


class WalletsListModel(walletslist.UiForm, event.EventForm):
    def __init__(self, parent):
        super(WalletsListModel, self).__init__(parent)

        self.setup()
        self.events_listening()

    def app_started_event(self):
        self.refresh()

    def wallet_edited_event(self):
        self.refresh()

    @pyqtSlot()
    def add_new_clicked(self):
        event.mainTabChanged.notify(tab=Tab.ADD_WALLET)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem):
        widget = super(WalletsListModel, self).item_clicked(item)
        event.walletChanged.notify(username=widget.get_username(), address=widget.get_address())
        event.mainTabChanged.notify(tab=Tab.LOGIN, recordable=False)

    def refresh(self):
        self.reset()

        # Test
        wallets = {
            '0x0000000000000000000000000000000000000000': 'Wallet1',
            '0x0000000000000000000000000000000000000001': 'Wallet2'
        }
        for address, username in wallets.items():

            item = walletitem.WalletItem(self)
            item.set_username(username)
            item.set_address(address)

            self.add_item(item)
