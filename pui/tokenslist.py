from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__listWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.setObjectName(Tab.WalletTab.TOKENS_LIST)

        self.__listWidget = SPGraphics.QuickListWidget(
            self, spacing=10, empty_illustration=images.data.illustrations.coin
        )
        self.__listWidget.layout().setAlignment(Qt.AlignCenter)
        self.__listWidget.labelIllustration.setAlignment(Qt.AlignHCenter)
        self.__listWidget.labelTitle.setAlignment(Qt.AlignHCenter)
        self.__listWidget.labelDescription.setAlignment(Qt.AlignHCenter)
        self.__listWidget.labelDescription.setSizePolicy(QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Preferred
        ))
        self.__listWidget.itemClicked.connect(self.item_clicked)

        self.layout().addWidget(self.__listWidget)

        super(UiForm, self).setup()

    def re_translate(self):
        self.__listWidget.labelTitle.setText(translator("No tokens has been added yet!"))
        self.__listWidget.labelDescription.setText(translator(
            "Let's add your first token today, click on Menu + \"Add Token\" button."
        ))

    def re_font(self):
        font = QFont()

        self.__listWidget.labelDescription.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setPointSize(fonts.data.size.medium)
        self.__listWidget.labelTitle.setFont(font)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem) -> QWidget:
        return self.__listWidget.itemWidget(item)

    def add_item(self, item: QListWidgetItem):
        self.__listWidget.add_quick_item(item)

    def reset(self):
        self.__listWidget.clear()
