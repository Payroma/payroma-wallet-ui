from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignHCenter)
        self.layout().setContentsMargins(11, 21, 11, 21)
        self.layout().setSpacing(11)

        self.labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.layout().addWidget(self.labelTitle)


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

        self.__headerWidget = None
        self.__listWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.HISTORY_LIST)

        self.__headerWidget = HeaderWidget(self)

        self.__listWidget = ListWidget(self)
        self.__listWidget.itemClicked.connect(self.item_clicked)

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__listWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.historylist)

    def re_translate(self):
        self.__headerWidget.labelTitle.setText(translator("Transactions History"))
        self.__listWidget.labelTitle.setText(translator("No transactions has been sent yet!"))
        self.__listWidget.labelDescription.setText(translator("Let's send your first transaction today."))

    def re_font(self):
        font = QFont()

        self.__listWidget.labelDescription.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        font.setBold(True)
        self.__headerWidget.labelTitle.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setBold(False)
        self.__listWidget.labelTitle.setFont(font)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem) -> QWidget:
        return self.__listWidget.itemWidget(item)

    def add_item(self, item: SPGraphics.QuickListWidgetItem):
        self.__listWidget.add_quick_item(item)

    def reset(self):
        self.__listWidget.clear()
