from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import addwallet


class AddWalletModel(addwallet.UiForm):
    def __init__(self, parent):
        super(AddWalletModel, self).__init__(parent)

        self.setup()

    @pyqtSlot(str)
    def username_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddWalletModel, self).username_changed(text, valid)

    @pyqtSlot(str)
    def password_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddWalletModel, self).password_changed(text, valid)

    @pyqtSlot(str)
    def confirm_password_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddWalletModel, self).confirm_password_changed(text, valid)

    @pyqtSlot(str)
    def pin_code_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddWalletModel, self).pin_code_changed(text, valid)

    @pyqtSlot(str)
    def address_changed(self, text: str):
        valid = True if len(text) == 42 else False
        super(AddWalletModel, self).address_changed(text, valid)

    @pyqtSlot()
    def add_clicked(self):
        super(AddWalletModel, self).add_clicked()
        QTimer().singleShot(5000, self.add_completed)
