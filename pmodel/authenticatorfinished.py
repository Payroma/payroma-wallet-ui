from plibs import *
from pheader import *
from pui import authenticatorfinished


class AuthenticatorFinishedModel(authenticatorfinished.UiForm):
    def __init__(self, parent):
        super(AuthenticatorFinishedModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_key("HAZGCNJTMNRWMZLBGM4TANJQMUYTSYRRMYYDOZBZGE2TGNZZGU2Q")

    @pyqtSlot()
    def done_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)
