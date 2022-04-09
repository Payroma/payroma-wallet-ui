from plibs import *
from pheader import *
from pcontroller import event
from pui import stakepair
from pmodel.stakepairapproval import StakePairApprovalModel
from pmodel.stakepairamount import StakePairAmountModel


class StakePairModel(stakepair.UiForm, event.EventForm):
    def __init__(self, parent):
        super(StakePairModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Tabs
        self.add_tab(StakePairApprovalModel(self), '')
        self.add_tab(StakePairAmountModel(self), '')

    def stake_pair_changed_event(
            self, block_title: str, blocks: int, total_staked: str,
            balance: str, staked: str, claim: str, stake_symbol: str, earn_symbol: str
    ):
        self.reset()
        self.set_data(
            block_title=block_title,
            blocks=blocks,
            total_staked=total_staked,
            stake_symbol=stake_symbol,
            earn_symbol=earn_symbol
        )

    def stake_pair_approved_event(self):
        self.set_approved()
