from plibs import *
from pheader import *
from pcontroller import event
from pui import stakepairapproval


class StakePairApprovalModel(stakepairapproval.UiForm):
    def __init__(self, parent):
        super(StakePairApprovalModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def approval_clicked(self):
        event.stakePairApproved.notify()
