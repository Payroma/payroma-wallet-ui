from plibs import *
from pheader import *
from pui import settings


class SettingsModel(settings.UiForm):
    def __init__(self, parent):
        super(SettingsModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot(bool)
    def switch_clicked(self, state: bool):
        theme_name = 'dark' if state else ''
        QObject.mainModel.themeModeChanged(theme_name)

    @pyqtSlot()
    def network_clicked(self):
        pass

    @pyqtSlot()
    def backup_clicked(self):
        super(SettingsModel, self).backup_clicked()

    @pyqtSlot()
    def import_clicked(self):
        super(SettingsModel, self).import_clicked()
