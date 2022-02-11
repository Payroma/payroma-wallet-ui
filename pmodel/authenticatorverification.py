from plibs import *
from pheader import *
from pui import authenticatorverification


class AuthenticatorVerificationModel(authenticatorverification.UiForm):
    def __init__(self, parent):
        super(AuthenticatorVerificationModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_username("Wallet1")
        self.set_address("0x0000000000000000000000000000000000000000")

    @pyqtSlot()
    def back_clicked(self):
        QObject.authenticatorSetupModel.currentTabChanged(Tab.AuthenticatorSetupTab.DOWNLOAD)

    @pyqtSlot(str)
    def password_changed(self, text: str):
        valid = True if text else False
        super(AuthenticatorVerificationModel, self).password_changed(text, valid)

    @pyqtSlot(str)
    def pin_code_changed(self, text: str):
        valid = True if text else False
        super(AuthenticatorVerificationModel, self).pin_code_changed(text, valid)