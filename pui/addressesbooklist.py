from plibs import *
from pcontroller import translator
from pui import SetupForm, fonts, images


class ListWidget(SPGraphics.QuickListWidget):
    def __init__(self, parent):
        super(ListWidget, self).__init__(
            parent, spacing=10, empty_illustration=images.data.illustrations.no_data
        )

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout().setContentsMargins(21, 0, 21, 0)
        self.layout().setAlignment(Qt.AlignVCenter)
        self.labelIllustration.setAlignment(Qt.AlignHCenter)
        self.labelTitle.setAlignment(Qt.AlignHCenter)
        self.labelDescription.setAlignment(Qt.AlignHCenter)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__listWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.__listWidget = ListWidget(self)
        self.__listWidget.itemClicked.connect(self.item_clicked)

        self.layout().addWidget(self.__listWidget)

        super(UiForm, self).setup()

    def re_translate(self):
        self.__listWidget.labelTitle.setText(translator("No wallets has been added yet!"))
        self.__listWidget.labelDescription.setText(translator(
            "Let's add your first wallet today, click on \"+\" button. It's easy."
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

    def add_item(self, item: SPGraphics.QuickListWidgetItem):
        self.__listWidget.add_quick_item(item)

    def reset(self):
        self.__listWidget.clear()

    def search(self, text: str):
        text = text.lower()

        for index in range(self.__listWidget.count()):
            item = self.__listWidget.item(index)
            if not text:
                item.setHidden(False)
                continue

            widget = self.__listWidget.itemWidget(item)
            if text in widget.get_username().lower() or text in widget.get_address().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

        self.repaint()
