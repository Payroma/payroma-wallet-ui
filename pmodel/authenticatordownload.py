from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import authenticatordownload


class AuthenticatorDownloadModel(authenticatordownload.UiForm):
    def __init__(self, parent):
        super(AuthenticatorDownloadModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def next_clicked(self):
        globalmethods.AuthenticatorSetupModel.setCurrentTab(Tab.AuthenticatorSetupTab.VERIFICATION)
