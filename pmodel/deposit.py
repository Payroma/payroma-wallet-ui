from plibs import *
from pheader import *
from pcontroller import event
from pui import deposit


class DepositModel(deposit.UiForm, event.EventForm):
    def __init__(self, parent):
        super(DepositModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Variables
        self.__address = None
        self.__networkName = None

    def wallet_changed_event(self, username: str, address: str):
        self.reset()
        self.set_data(address, self.__networkName)
        self.__address = address

    def network_changed_event(self, name: str, status: bool):
        self.reset()

        address = ''
        if self.__address:
            address = self.__address

        self.set_data(address, name)
        self.__networkName = name

    @pyqtSlot()
    def network_clicked(self):
        event.mainTabChanged.notify(tab=Tab.NETWORKS_LIST)
