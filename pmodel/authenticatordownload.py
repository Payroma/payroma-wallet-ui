from plibs import *
from pheader import *
from pui import authenticatordownload


class AuthenticatorDownloadModel(authenticatordownload.UiForm):
    def __init__(self, parent):
        super(AuthenticatorDownloadModel, self).__init__(parent)

        self.setup()

    def next_clicked(self):
        QObject.authenticatorSetupModel.currentTabChanged(Tab.AuthenticatorSetupTab.VERIFICATION)
