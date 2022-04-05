from plibs import *
from pheader import *
from pcontroller import event
from pui import authenticatordownload


class AuthenticatorDownloadModel(authenticatordownload.UiForm):
    def __init__(self, parent):
        super(AuthenticatorDownloadModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def next_clicked(self):
        event.authenticatorSetupTabChanged.notify(tab=Tab.AuthenticatorSetupTab.VERIFICATION)
