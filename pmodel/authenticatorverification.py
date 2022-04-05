from plibs import *
from pheader import *
from pcontroller import event
from pui import authenticatorverification


class AuthenticatorVerificationModel(authenticatorverification.UiForm, event.EventForm):
    def __init__(self, parent):
        super(AuthenticatorVerificationModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Variables
        self.__username = None

    def wallet_changed_event(self, username: str, address: str):
        self.reset()
        self.set_data(username, address)
        self.__username = username

    @pyqtSlot()
    def back_clicked(self):
        event.authenticatorSetupTabChanged.notify(tab=Tab.AuthenticatorSetupTab.DOWNLOAD)

    @pyqtSlot(str)
    def password_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AuthenticatorVerificationModel, self).password_changed(text, valid)

    @pyqtSlot(str)
    def pin_code_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AuthenticatorVerificationModel, self).pin_code_changed(text, valid)

    @pyqtSlot()
    def verify_clicked(self):
        event.authenticatorSetupVerified.notify(
            username=self.__username, otp_hash='HAZGCNJTMNRWMZLBGM4TANJQMUYTSYRRMYYDOZBZGE2TGNZZGU2Q'
        )
        event.authenticatorSetupTabChanged.notify(tab=Tab.AuthenticatorSetupTab.SCAN)
