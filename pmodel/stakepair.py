from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import stakepair
from pmodel.stakepairapproval import StakePairApprovalModel
from pmodel.stakepairamount import StakePairAmountModel


class StakePairModel(stakepair.UiForm):
    def __init__(self, parent):
        super(StakePairModel, self).__init__(parent)

        self.setup()

        # Global Methods
        globalmethods.StakePairModel._setData = self.set_data
        globalmethods.StakePairModel._setApproved = self.set_approved

        # Tabs
        self.stakePairApprovalModel = StakePairApprovalModel(self)
        self.stakePairAmountModel = StakePairAmountModel(self)

        self.add_tab(self.stakePairApprovalModel, '')
        self.add_tab(self.stakePairAmountModel, '')

    def set_data(
            self, block_title: str, blocks: int, total_staked: str,
            stake_symbol: str, earn_symbol: str
    ):
        self.reset()
        super(StakePairModel, self).set_data(
            block_title, blocks, total_staked, stake_symbol, earn_symbol
        )
