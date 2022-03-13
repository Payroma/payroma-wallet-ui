from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import addnetwork


class AddNetworkModel(addnetwork.UiForm):
    def __init__(self, parent):
        super(AddNetworkModel, self).__init__(parent)

        self.setup()

    @pyqtSlot(str)
    def name_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddNetworkModel, self).name_changed(text, valid)

    @pyqtSlot(str)
    def rpc_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddNetworkModel, self).rpc_changed(text, valid)

    @pyqtSlot(str)
    def symbol_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddNetworkModel, self).symbol_changed(text, valid)

    @pyqtSlot(str)
    def chain_id_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddNetworkModel, self).chain_id_changed(text, valid)

    @pyqtSlot(str)
    def explorer_changed(self, text: str):
        valid = True if len(text) > 5 else False
        super(AddNetworkModel, self).explorer_changed(text, valid)

    @pyqtSlot()
    def add_clicked(self):
        super(AddNetworkModel, self).add_clicked()
        QTimer().singleShot(5000, self.add_completed)
