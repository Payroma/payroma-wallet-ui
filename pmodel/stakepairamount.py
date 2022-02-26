from plibs import *
from pheader import *
from pui import stakepairamount


class StakePairAmountModel(stakepairamount.UiForm):
    def __init__(self, parent):
        super(StakePairAmountModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_balance('547,544', 'USDT')
        self.set_staked_balance('20,000', 'USDT')
        self.set_claim_balance('1000', 'BUSD')

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
        valid = True if float(text or 0) > 0 else False
        super(StakePairAmountModel, self).claim_changed(text, valid)
