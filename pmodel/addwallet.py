from plibs import *
from pheader import *
from pcontroller import event
from pui import addwallet


class AddWalletModel(addwallet.UiForm):
    def __init__(self, parent):
        super(AddWalletModel, self).__init__(parent)

        self.setup()

    def showEvent(self, a0: QShowEvent):
        super(AddWalletModel, self).showEvent(a0)
        self.reset()

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

    @pyqtSlot()
    def add_clicked(self):
        super(AddWalletModel, self).add_clicked()
        QTimer().singleShot(5000, self.add_completed)
