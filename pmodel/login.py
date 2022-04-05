from plibs import *
from pheader import *
from pcontroller import event
from pui import login


class LoginModel(login.UiForm, event.EventForm):
    def __init__(self, parent):
        super(LoginModel, self).__init__(parent)

        self.setup()
        self.events_listening()

    def wallet_changed_event(self, username: str, address: str):
        self.reset()
        self.set_data(username, address)

    @pyqtSlot()
    def skip_clicked(self):
        event.mainTabChanged.notify(tab=Tab.WALLET)

    @pyqtSlot(str)
    def password_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(LoginModel, self).password_changed(text, valid)

    @pyqtSlot()
    def login_clicked(self):
        event.mainTabChanged.notify(tab=Tab.AUTHENTICATOR, recordable=False)
