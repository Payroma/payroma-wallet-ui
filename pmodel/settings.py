from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import settings


class SettingsModel(settings.UiForm):
    def __init__(self, parent):
        super(SettingsModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_data(network_connected=True, network_name="Binance Smart Chain")

    @pyqtSlot(bool)
    def switch_clicked(self, state: bool):
        theme_name = 'dark' if state else ''
        globalmethods.MainModel.setThemeMode(theme_name)

    @pyqtSlot()
    def network_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.NETWORKS_LIST)

    @pyqtSlot()
    def backup_clicked(self):
        super(SettingsModel, self).backup_clicked()

    @pyqtSlot()
    def import_clicked(self):
        super(SettingsModel, self).import_clicked()
