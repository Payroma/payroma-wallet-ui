from plibs import *
from pheader import *
from pui import deposit


class DepositModel(deposit.UiForm):
    def __init__(self, parent):
        super(DepositModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_address('0x0000000000000000000000000000000000000000')
        self.set_network_name('Binance Smart Chain')

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)
