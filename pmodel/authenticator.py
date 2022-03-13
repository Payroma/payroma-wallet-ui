from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import authenticator


class AuthenticatorModel(authenticator.UiForm):
    def __init__(self, parent):
        super(AuthenticatorModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def confirm_clicked(self):
        super(AuthenticatorModel, self).confirm_clicked()
        globalmethods.MainModel.setCurrentTab(Tab.WALLET)

    @pyqtSlot()
    def forgot_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.AUTHENTICATOR_SETUP, recordable=False)

    def otp_code_changed(self, text: str, valid: bool = False):
        if len(text) == 6:
            valid = True
        super(AuthenticatorModel, self).otp_code_changed(text, valid)
