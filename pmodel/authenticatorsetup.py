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
        self.add_tab(AuthenticatorDownloadModel(self), Tab.AuthenticatorSetupTab.DOWNLOAD)
        self.add_tab(AuthenticatorVerificationModel(self), Tab.AuthenticatorSetupTab.VERIFICATION)
        self.add_tab(AuthenticatorScanModel(self), Tab.AuthenticatorSetupTab.SCAN)
        self.add_tab(AuthenticatorFinishedModel(self), Tab.AuthenticatorSetupTab.FINISHED)
