from plibs import *
from pheader import *
from pui import login


class GlobalEvents:
    loginChanged = None


class LoginItem(login.UiForm):
    QObject.loginModel = GlobalEvents()

    def __init__(self, parent):
        super(LoginItem, self).__init__(parent)

        self.setup()

        # Events
        QObject.loginModel.loginChanged = self.login_changed

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)

    def login_changed(self, username: str, address: str):
        self.set_username(username)
        self.set_address(address)
