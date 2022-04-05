from plibs import *
from pheader import *
from pcontroller import event
from pui import authenticatorfinished


class AuthenticatorFinishedModel(authenticatorfinished.UiForm, event.EventForm):
    def __init__(self, parent):
        super(AuthenticatorFinishedModel, self).__init__(parent)

        self.setup()
        self.events_listening()

    def authenticator_setup_verified_event(self, username: str, otp_hash: str):
        self.reset()
        self.set_data(otp_hash)

    @pyqtSlot()
    def done_clicked(self):
        event.mainTabChanged.notify(tab=Tab.WALLETS_LIST)
