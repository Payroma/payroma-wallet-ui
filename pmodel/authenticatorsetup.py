from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import authenticatorsetup
from pmodel.authenticatordownload import AuthenticatorDownloadModel
from pmodel.authenticatorverification import AuthenticatorVerificationModel
from pmodel.authenticatorscan import AuthenticatorScanModel
from pmodel.authenticatorfinished import AuthenticatorFinishedModel


class AuthenticatorSetupModel(authenticatorsetup.UiForm):
    def __init__(self, parent):
        super(AuthenticatorSetupModel, self).__init__(parent)

        self.setup()
        self.reset()

        # Global Methods
        globalmethods.AuthenticatorSetupModel._setCurrentTab = self.set_current_tab

        # Tabs
        self.authenticatorDownloadModel = AuthenticatorDownloadModel(self)
        self.authenticatorVerificationModel = AuthenticatorVerificationModel(self)
        self.authenticatorScanModel = AuthenticatorScanModel(self)
        self.authenticatorFinishedModel = AuthenticatorFinishedModel(self)

        self.add_tab(self.authenticatorDownloadModel, Tab.AuthenticatorSetupTab.DOWNLOAD)
        self.add_tab(self.authenticatorVerificationModel, Tab.AuthenticatorSetupTab.VERIFICATION)
        self.add_tab(self.authenticatorScanModel, Tab.AuthenticatorSetupTab.SCAN)
        self.add_tab(self.authenticatorFinishedModel, Tab.AuthenticatorSetupTab.FINISHED)
