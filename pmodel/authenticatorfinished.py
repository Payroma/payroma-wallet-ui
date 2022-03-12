from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import authenticatorfinished


class AuthenticatorFinishedModel(authenticatorfinished.UiForm):
    def __init__(self, parent):
        super(AuthenticatorFinishedModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_data("HAZGCNJTMNRWMZLBGM4TANJQMUYTSYRRMYYDOZBZGE2TGNZZGU2Q")

    @pyqtSlot()
    def done_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.WALLETS_LIST)
