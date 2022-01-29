from plibs import *
from pcontroller import translator
from pui import SetupForm


class UiForm(SetupForm):
    def __init__(self, parent):
        self.__parent = parent

        self.settings = None
        self.exit = None
        self.copy = None

    def setup(self):
        self.settings = self.__align_top()
        self.exit = self.__align_top()
        self.copy = self.__align_top()

        super(UiForm, self).setup()

    def re_translate(self):
        self.settings.labelText.setText(translator("Settings"))
        self.exit.labelText.setText(translator("Exit"))
        self.copy.labelText.setText(translator("Copy"))

    def re_font(self):
        font = QFont()

        self.settings.labelText.setFont(font)
        self.exit.labelText.setFont(font)
        self.copy.labelText.setFont(font)

    def __align_top(self) -> SPGraphics.QuickToolTip:
        return SPGraphics.QuickToolTip(
            self.__parent, text_align=Qt.AlignCenter, align=Qt.AlignTop
        )

    def __align_right(self) -> SPGraphics.QuickToolTip:
        return SPGraphics.QuickToolTip(
            self.__parent, text_align=Qt.AlignCenter, align=Qt.AlignRight,
            arrow_size=QSize(8, 15), margin=15
        )
