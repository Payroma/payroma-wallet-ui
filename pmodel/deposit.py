from plibs import *
from pheader import *
from pui import deposit


class DepositModel(deposit.UiForm):
    def __init__(self, parent):
        super(DepositModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_data('0x0000000000000000000000000000000000000000', 'Binance Smart Chain')

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)

    @pyqtSlot()
    def network_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.NETWORKS_LIST)
