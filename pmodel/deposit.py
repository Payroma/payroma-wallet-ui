from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import deposit


class DepositModel(deposit.UiForm):
    def __init__(self, parent):
        super(DepositModel, self).__init__(parent)

        self.setup()

        # Global Methods
        globalmethods.DepositModel._setData = self.set_data

    @pyqtSlot()
    def network_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.NETWORKS_LIST)
