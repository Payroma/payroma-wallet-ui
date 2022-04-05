from plibs import *
from pheader import *
from pcontroller import event
from pui import settings


class SettingsModel(settings.UiForm, event.EventForm):
    def __init__(self, parent):
        super(SettingsModel, self).__init__(parent)

        self.setup()
        self.events_listening()

    def network_changed_event(self, name: str, status: bool):
        self.set_data(status, name)

    @pyqtSlot(bool)
    def switch_clicked(self, state: bool):
        theme_name = 'dark' if state else ''
        event.themeChanged.notify(name=theme_name)

    @pyqtSlot()
    def network_clicked(self):
        event.mainTabChanged.notify(tab=Tab.NETWORKS_LIST)

    @pyqtSlot()
    def backup_clicked(self):
        super(SettingsModel, self).backup_clicked()

    @pyqtSlot()
    def import_clicked(self):
        super(SettingsModel, self).import_clicked()
