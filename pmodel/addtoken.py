from plibs import *
from pheader import *
from pcontroller import event
from pui import addtoken


class AddTokenModel(addtoken.UiForm):
    def __init__(self, parent):
        super(AddTokenModel, self).__init__(parent)

        self.setup()

    def showEvent(self, a0: QShowEvent):
        super(AddTokenModel, self).showEvent(a0)
        self.reset()

    @pyqtSlot()
    def back_clicked(self):
        event.walletTabChanged.notify(tab=Tab.WalletTab.TOKENS_LIST)

    @pyqtSlot(str)
    def address_changed(self, text: str):
        valid = True if len(text) == 42 else False
        super(AddTokenModel, self).address_changed(text, valid)

    @pyqtSlot(str)
    def symbol_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddTokenModel, self).symbol_changed(text, valid)

    @pyqtSlot(str)
    def decimals_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddTokenModel, self).decimals_changed(text, valid)

    @pyqtSlot()
    def add_clicked(self):
        super(AddTokenModel, self).add_clicked()
        QTimer().singleShot(5000, self.add_completed)
