from plibs import *
from pheader import *
from pui import authenticatorsetup


class GlobalEvents:
    currentTabChanged = None


class AuthenticatorSetupModel(authenticatorsetup.UiForm):
    QObject.walletModel = GlobalEvents()

    def __init__(self, parent):
        super(AuthenticatorSetupModel, self).__init__(parent)

        self.setup()
        self.reset()

        # Events
        QObject.walletModel.currentTabChanged = self.set_current_tab

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)
