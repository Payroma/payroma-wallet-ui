from plibs import *
from pheader import *
from pui import stakepair
from pmodel.stakepairapproval import StakePairApprovalModel
from pmodel.stakepairamount import StakePairAmountModel


class GlobalEvents(QObject):
    pairChanged = None
    approvalChanged = None


class StakePairModel(stakepair.UiForm):
    QObject.stakePairModel = GlobalEvents()

    def __init__(self, parent):
        super(StakePairModel, self).__init__(parent)

        self.setup()

        # Events
        QObject.stakePairModel.pairChanged = self.set_data
        QObject.stakePairModel.approvalChanged = self.set_approved

        # Tabs
        self.stakePairApprovalModel = StakePairApprovalModel(self)
        self.stakePairAmountModel = StakePairAmountModel(self)

        self.add_tab(self.stakePairApprovalModel, '')
        self.add_tab(self.stakePairAmountModel, '')

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.STAKE_LIST)

    def set_data(
            self, block_title: str, blocks: int, total_staked: str,
            stake_symbol: str, earn_symbol: str
    ):
        self.reset()
        super(StakePairModel, self).set_data(
            block_title, blocks, total_staked, stake_symbol, earn_symbol
        )
