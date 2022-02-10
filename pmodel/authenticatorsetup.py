from plibs import *
from pheader import *
from pui import authenticatorsetup
from pmodel.authenticatordownload import AuthenticatorDownloadModel


class GlobalEvents:
    currentTabChanged = None


class AuthenticatorSetupModel(authenticatorsetup.UiForm):
    QObject.authenticatorSetupModel = GlobalEvents()

    def __init__(self, parent):
        super(AuthenticatorSetupModel, self).__init__(parent)

        self.setup()
        self.reset()

        # Events
        QObject.authenticatorSetupModel.currentTabChanged = self.set_current_tab

        # Tabs
        self.authenticatorDownloadModel = AuthenticatorDownloadModel(self)

        self.add_tab(self.authenticatorDownloadModel, Tab.AuthenticatorSetupTab.DOWNLOAD)

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)
