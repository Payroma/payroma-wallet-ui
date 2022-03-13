from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import login


class LoginModel(login.UiForm):
    def __init__(self, parent):
        super(LoginModel, self).__init__(parent)

        self.setup()

        # Global Methods
        globalmethods.LoginModel._setData = self.set_data

    @pyqtSlot()
    def skip_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.WALLET)

    @pyqtSlot(str)
    def password_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(LoginModel, self).password_changed(text, valid)

    @pyqtSlot()
    def login_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.AUTHENTICATOR, recordable=False)
