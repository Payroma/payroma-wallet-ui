from plibs import *
from pheader import *
from pcontroller import event
from pui import stakepairamount


class StakePairAmountModel(stakepairamount.UiForm, event.EventForm):
    def __init__(self, parent):
        super(StakePairAmountModel, self).__init__(parent)

        self.setup()
        self.events_listening()

    def stake_pair_changed_event(
            self, block_title: str, blocks: int, total_staked: str,
            balance: str, staked: str, claim: str, stake_symbol: str, earn_symbol: str
    ):
        self.reset()
        self.set_data(
            balance=balance,
            staked=staked,
            claim=claim,
            stake_symbol=stake_symbol,
            earn_symbol=earn_symbol
        )

    @pyqtSlot(str)
    def deposit_changed(self, text: str):
        valid = True if float(text or 0) > 0 else False
        super(StakePairAmountModel, self).deposit_changed(text, valid)

    @pyqtSlot(str)
    def withdraw_changed(self, text: str):
        valid = True if float(text or 0) > 0 else False
        super(StakePairAmountModel, self).withdraw_changed(text, valid)

    @pyqtSlot(str)
    def claim_changed(self, text: str):
        valid = True if text else False
        super(StakePairAmountModel, self).claim_changed(text, valid)
