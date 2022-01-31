from plibs import *
from pheader import *
from pui import settings


class SettingsModel(settings.UiForm):
    def __init__(self, parent):
        super(SettingsModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLETS_LIST)

    @pyqtSlot(bool)
    def switch_clicked(self, state: bool):
        theme_name = 'dark' if state else ''
        QObject.mainModel.themeModeChanged(theme_name)

    @pyqtSlot()
    def network_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.NETWORKS_LIST)

    @pyqtSlot()
    def backup_clicked(self):
        super(SettingsModel, self).backup_clicked()

    @pyqtSlot()
    def import_clicked(self):
        super(SettingsModel, self).import_clicked()
