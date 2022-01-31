from plibs import *
from pcontroller import translator
from pui import SetupForm


class UiForm(SetupForm):
    def __init__(self, parent):
        self.__parent = parent

        self.settings = None
        self.exit = None
        self.copy = None
        self.back = None
        self.networkStatus = None

        self.networkSettingsR = None
        self.addNewR = None
        self.networkNameAlert = None
        self.networkRPCAlert = None
        self.networkChainIdAlert = None
        self.networkExplorerAlert = None

    def setup(self):
        self.settings = self.__align_top()
        self.exit = self.__align_top()
        self.copy = self.__align_top()
        self.back = self.__align_top()
        self.networkStatus = self.__align_top()

        self.networkSettingsR = self.__align_right()
        self.addNewR = self.__align_right()
        self.networkNameAlert = self.__align_right()
        self.networkRPCAlert = self.__align_right()
        self.networkChainIdAlert = self.__align_right()
        self.networkExplorerAlert = self.__align_right()

        super(UiForm, self).setup()

    def re_translate(self):
        self.settings.labelText.setText(translator("Settings"))
        self.exit.labelText.setText(translator("Exit"))
        self.copy.labelText.setText(translator("Copy"))
        self.back.labelText.setText(translator("Back"))
        self.networkStatus.labelText.setText(translator("Network Connection Status"))

        self.networkSettingsR.labelText.setText(translator("Network settings to add a new and switching."))
        self.addNewR.labelText.setText(translator("Add New"))
        self.networkNameAlert.labelText.setText(translator("Network name already exists before"))
        self.networkRPCAlert.labelText.setText(translator("This RPC is unable to connect"))
        self.networkChainIdAlert.labelText.setText(translator("Chain id is wrong"))
        self.networkExplorerAlert.labelText.setText(translator("Explorer URL is wrong"))

    def re_font(self):
        font = QFont()

        self.settings.labelText.setFont(font)
        self.exit.labelText.setFont(font)
        self.copy.labelText.setFont(font)
        self.back.labelText.setFont(font)
        self.networkStatus.labelText.setFont(font)

        self.networkSettingsR.labelText.setFont(font)
        self.addNewR.labelText.setFont(font)
        self.networkNameAlert.labelText.setFont(font)
        self.networkRPCAlert.labelText.setFont(font)
        self.networkChainIdAlert.labelText.setFont(font)
        self.networkExplorerAlert.labelText.setFont(font)

    def __align_top(self) -> SPGraphics.QuickToolTip:
        return SPGraphics.QuickToolTip(
            self.__parent, text_align=Qt.AlignCenter, align=Qt.AlignTop
        )

    def __align_right(self) -> SPGraphics.QuickToolTip:
        return SPGraphics.QuickToolTip(
            self.__parent, text_align=Qt.AlignCenter, align=Qt.AlignRight,
            arrow_size=QSize(8, 15), margin=15
        )
