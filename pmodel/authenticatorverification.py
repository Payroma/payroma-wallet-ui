from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import authenticatorverification


class AuthenticatorVerificationModel(authenticatorverification.UiForm):
    def __init__(self, parent):
        super(AuthenticatorVerificationModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_data("Wallet1", "0x0000000000000000000000000000000000000000")

    @pyqtSlot()
    def back_clicked(self):
        globalmethods.AuthenticatorSetupModel.setCurrentTab(Tab.AuthenticatorSetupTab.DOWNLOAD)

    @pyqtSlot()
    def verify_clicked(self):
        globalmethods.AuthenticatorSetupModel.setCurrentTab(Tab.AuthenticatorSetupTab.SCAN)

    @pyqtSlot(str)
    def password_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AuthenticatorVerificationModel, self).password_changed(text, valid)

    @pyqtSlot(str)
    def pin_code_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AuthenticatorVerificationModel, self).pin_code_changed(text, valid)
