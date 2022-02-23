from plibs import *
from pheader import *
from pui import stakepair
from pmodel.stakepairapproval import StakePairApprovalModel


class GlobalEvents(QObject):
    pairChanged = None


class StakePairModel(stakepair.UiForm):
    QObject.stakePairModel = GlobalEvents()

    def __init__(self, parent):
        super(StakePairModel, self).__init__(parent)

        self.setup()

        # Events
        QObject.stakePairModel.pairChanged = self.set_pair

        # Tabs
        self.stakePairApprovalModel = StakePairApprovalModel(self)

        self.add_tab(self.stakePairApprovalModel, '')

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.STAKE_LIST)

    def set_pair(self, stake_symbol: str, earn_symbol: str):
        self.reset()
        super(StakePairModel, self).set_pair(stake_symbol, earn_symbol)
