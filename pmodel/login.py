from plibs import *
from pheader import *
from pui import login


class GlobalEvents:
    loginChanged = None


class LoginModel(login.UiForm):
    QObject.loginModel = GlobalEvents()

    def __init__(self, parent):
        super(LoginModel, self).__init__(parent)

        self.setup()

        # Events
        QObject.loginModel.loginChanged = self.login_changed

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)

    @pyqtSlot()
    def skip_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)

    @pyqtSlot(str)
    def password_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(LoginModel, self).password_changed(text, valid)

    @pyqtSlot()
    def login_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.AUTHENTICATOR)

    def login_changed(self, username: str, address: str):
        self.set_data(username, address)
        QObject.walletModel.walletChanged(username, address)
