from plibs import *
from pheader import *
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
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.SETTINGS)

    def add_new_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.ADD_NETWORK)

    def item_clicked(self, item: QListWidgetItem):
        widget = super(NetworksListModel, self).item_clicked(item)
        for network in self.networks:
            if network is widget:
                network.set_status(True)
            else:
                network.set_status(False)
