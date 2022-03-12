from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import authenticatorscan


class AuthenticatorScanModel(authenticatorscan.UiForm):
    def __init__(self, parent):
        super(AuthenticatorScanModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_data("HAZGCNJTMNRWMZLBGM4TANJQMUYTSYRRMYYDOZBZGE2TGNZZGU2Q", "Wallet1")

    @pyqtSlot()
    def back_clicked(self):
        globalmethods.AuthenticatorSetupModel.setCurrentTab(Tab.AuthenticatorSetupTab.VERIFICATION)

    @pyqtSlot()
    def confirm_clicked(self):
        globalmethods.AuthenticatorSetupModel.setCurrentTab(Tab.AuthenticatorSetupTab.FINISHED)

    def otp_code_changed(self, text: str, valid: bool = False):
        if len(text) == 6:
            valid = True
        super(AuthenticatorScanModel, self).otp_code_changed(text, valid)
