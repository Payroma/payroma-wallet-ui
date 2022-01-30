from plibs import *
from pheader import *
from pcontroller import url_open
from pui import main
from pmodel.settings import SettingsModel
from pmodel.networksettings import NetworkSettingsModel


class GlobalEvents:
    currentTabChanged = None
    themeModeChanged = None
    backgroundColorAnimated = None


class MainModel(main.UiForm):
    QObject.mainModel = GlobalEvents()

    def __init__(self, parent):
        super(MainModel, self).__init__(parent)

        self.setup()

        # Events
        QObject.mainModel.currentTabChanged = self.set_current_tab
        QObject.mainModel.themeModeChanged = self.set_theme_mode
        QObject.mainModel.backgroundColorAnimated = self.background_color_animate

        # Tabs
        self.add_tab(SettingsModel(self), Tab.SETTINGS)
        self.add_tab(NetworkSettingsModel(self), Tab.NETWORK_SETTINGS)

    @pyqtSlot()
    def settings_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.SETTINGS)

    @pyqtSlot()
    def exit_clicked(self):
        self.close()

    @pyqtSlot()
    def invest_clicked(self):
        url_open(Website.PAYROMA)

    def default_theme(self):
        pass
