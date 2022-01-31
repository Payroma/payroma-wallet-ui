from plibs import *
from pheader import *
from pui import networksettings


class NetworkSettingsModel(networksettings.UiForm):
    def __init__(self, parent):
        super(NetworkSettingsModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.SETTINGS)

    def add_new_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.ADD_NETWORK)
