from plibs import *
from pheader import *
from pcontroller import event
from pui import networkslist
from pmodel import networkitem


class NetworksListModel(networkslist.UiForm, event.EventForm):
    def __init__(self, parent):
        super(NetworksListModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Variables
        self.__networkItems = []

    def app_started_event(self):
        self.refresh()

    def network_edited_event(self):
        self.refresh()

    @pyqtSlot()
    def add_new_clicked(self):
        event.mainTabChanged.notify(tab=Tab.ADD_NETWORK)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem):
        widget = super(NetworksListModel, self).item_clicked(item)
        self.set_current_network(widget.get_name())

    def reset(self):
        super(NetworksListModel, self).reset()
        self.__networkItems.clear()

    def refresh(self):
        self.reset()

        # Test
        networks = {
            'Ethereum': 'ETH',
            'Polygon': 'MATIC',
            'Binance Smart Chain': 'BNB'
        }
        for name, symbol in networks.items():
            item = networkitem.NetworkItem(self)
            item.set_name(name)
            item.set_symbol(symbol)

            if item.get_name() == 'Ethereum':
                item.set_master()

            self.add_item(item)
            self.__networkItems.append(item)

        self.set_current_network('Ethereum')

    def set_current_network(self, name: str):
        for item in self.__networkItems:
            item.set_checked(item.get_name() == name)

        event.networkChanged.notify(
            name=name,
            status=True
        )
