from plibs import *
from pheader import *
from pui import stakelist


class StakeListModel(stakelist.UiForm):
    def __init__(self, parent):
        super(StakeListModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_tvl("4,561,012", "PYA")

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)
