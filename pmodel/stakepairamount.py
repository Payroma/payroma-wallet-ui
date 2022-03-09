from plibs import *
from pheader import *
from pui import stakepairamount


class GlobalEvents(QObject):
    pairChanged = None


class StakePairAmountModel(stakepairamount.UiForm):
    QObject.stakePairAmountModel = GlobalEvents()

    def __init__(self, parent):
        super(StakePairAmountModel, self).__init__(parent)

        self.setup()

        # Events
        QObject.stakePairAmountModel.pairChanged = self.set_data

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
