from plibs import *
from pheader import *
from pui import authenticator


class AuthenticatorModel(authenticator.UiForm):
    def __init__(self, parent):
        super(AuthenticatorModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)

    @pyqtSlot()
    def confirm_clicked(self):
        super(AuthenticatorModel, self).confirm_clicked()
        QObject.mainModel.currentTabChanged(Tab.WALLET)

    @pyqtSlot()
    def forgot_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.AUTHENTICATOR_SETUP)

    def otp_code_changed(self, text: str, valid: bool = False):
        if len(text) == 6:
            valid = True
        super(AuthenticatorModel, self).otp_code_changed(text, valid)
