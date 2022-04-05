from plibs import *
from pheader import *
from pcontroller import event
from pui import authenticator


class AuthenticatorModel(authenticator.UiForm, event.EventForm):
    def __init__(self, parent):
        super(AuthenticatorModel, self).__init__(parent)

        self.setup()
        self.events_listening()

    @pyqtSlot()
    def forgot_clicked(self):
        event.mainTabChanged.notify(tab=Tab.AUTHENTICATOR_SETUP, recordable=False)

    def otp_code_changed(self, text: str, valid: bool = False):
        if len(text) == 6:
            valid = True
        super(AuthenticatorModel, self).otp_code_changed(text, valid)

    @pyqtSlot()
    def confirm_clicked(self):
        super(AuthenticatorModel, self).confirm_clicked()
        event.mainTabChanged.notify(tab=Tab.WALLET)
