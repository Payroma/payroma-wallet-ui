from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import networkslist
from pmodel import networkitem


class NetworksListModel(networkslist.UiForm):
    def __init__(self, parent):
        super(NetworksListModel, self).__init__(parent)

        self.setup()

        # Test
        networks = {
            'Ethereum': 'ETH',
            'Polygon': 'MATIC',
            'Binance Smart Chain': 'BNB'
        }
        self.networks = []
        for name, symbol in networks.items():
            item = networkitem.NetworkItem(self)
            item.set_name(name)
            item.set_symbol(symbol)
            self.add_item(item)
            self.networks.append(item)

    @pyqtSlot()
    def add_new_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.ADD_NETWORK)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem):
        widget = super(NetworksListModel, self).item_clicked(item)
        for network in self.networks:
            if network is widget:
                network.set_status(True)
            else:
                network.set_status(False)
