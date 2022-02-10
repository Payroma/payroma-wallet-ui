from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images


class UiForm(SPGraphics.QuickListWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(
            parent, spacing=10, empty_illustration=images.data.illustrations.coin
        )

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName(Tab.WalletTab.TOKENS_LIST)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setAlignment(Qt.AlignCenter)
        self.labelIllustration.setAlignment(Qt.AlignHCenter)
        self.labelTitle.setAlignment(Qt.AlignHCenter)
        self.labelDescription.setAlignment(Qt.AlignHCenter)
        self.labelDescription.setSizePolicy(QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Preferred
        ))
        self.itemClicked.connect(self.item_clicked)

        super(UiForm, self).setup()

    def re_translate(self):
        self.labelTitle.setText(translator("No tokens has been added yet!"))
        self.labelDescription.setText(translator(
            "Let's add your first token today, click on Menu + \"Add Token\" button."
        ))

    def re_font(self):
        font = QFont()

        self.labelDescription.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setPointSize(fonts.data.size.medium)
        self.labelTitle.setFont(font)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem) -> QWidget:
        return self.itemWidget(item)

    def add_item(self, item: QListWidgetItem):
        self.add_quick_item(item)

    def reset(self):
        self.clear()
