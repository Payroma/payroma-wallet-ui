from plibs import *
from pheader import *
from pcontroller import event
from pui import authenticatorscan


class AuthenticatorScanModel(authenticatorscan.UiForm, event.EventForm):
    def __init__(self, parent):
        super(AuthenticatorScanModel, self).__init__(parent)

        self.setup()
        self.events_listening()

    def authenticator_setup_verified_event(self, username: str, otp_hash: str):
        self.reset()
        self.set_data(username, otp_hash)

    @pyqtSlot()
    def back_clicked(self):
        event.authenticatorSetupTabChanged.notify(tab=Tab.AuthenticatorSetupTab.VERIFICATION)

    @pyqtSlot(str)
    def otp_code_changed(self, text: str):
        valid = False
        if len(text) == 6:
            valid = True
        super(AuthenticatorScanModel, self).otp_code_changed(text, valid)

    @pyqtSlot()
    def confirm_clicked(self):
        event.authenticatorSetupTabChanged.notify(tab=Tab.AuthenticatorSetupTab.FINISHED)
