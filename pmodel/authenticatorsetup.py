from plibs import *
from pheader import *
from pcontroller import event
from pui import authenticatorsetup
from pmodel.authenticatordownload import AuthenticatorDownloadModel
from pmodel.authenticatorverification import AuthenticatorVerificationModel
from pmodel.authenticatorscan import AuthenticatorScanModel
from pmodel.authenticatorfinished import AuthenticatorFinishedModel


class AuthenticatorSetupModel(authenticatorsetup.UiForm, event.EventForm):
    def __init__(self, parent):
        super(AuthenticatorSetupModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Tabs
        self.add_tab(AuthenticatorDownloadModel(self), Tab.AuthenticatorSetupTab.DOWNLOAD)
        self.add_tab(AuthenticatorVerificationModel(self), Tab.AuthenticatorSetupTab.VERIFICATION)
        self.add_tab(AuthenticatorScanModel(self), Tab.AuthenticatorSetupTab.SCAN)
        self.add_tab(AuthenticatorFinishedModel(self), Tab.AuthenticatorSetupTab.FINISHED)

    def showEvent(self, a0: QShowEvent):
        super(AuthenticatorSetupModel, self).showEvent(a0)
        self.reset()

    def authenticator_setup_tab_changed_event(self, tab: str):
        self.set_current_tab(tab)
