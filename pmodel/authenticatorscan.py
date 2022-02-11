from plibs import *
from pheader import *
from pui import authenticatorscan


class AuthenticatorScanModel(authenticatorscan.UiForm):
    def __init__(self, parent):
        super(AuthenticatorScanModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_otp_hash("HAZGCNJTMNRWMZLBGM4TANJQMUYTSYRRMYYDOZBZGE2TGNZZGU2Q", "Wallet1")

    @pyqtSlot()
    def back_clicked(self):
        QObject.authenticatorSetupModel.currentTabChanged(Tab.AuthenticatorSetupTab.VERIFICATION)

    def otp_code_changed(self, text: str, valid: bool = False):
        if len(text) == 6:
            valid = True
        super(AuthenticatorScanModel, self).code_changed(text, valid)
