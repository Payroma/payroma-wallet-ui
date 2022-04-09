from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignHCenter)
        self.layout().setContentsMargins(16, 16, 16, 16)
        self.layout().setSpacing(11)

        self.lineEditSearch = SPGraphics.QuickLineEdit(
            self, fixed_height=41, layout_support=True, length=42
        )
        self.lineEditSearch.setProperty("iconable", True)
        self.lineEditSearch.setMaximumWidth(501)
        self.lineEditSearch.setFocusPolicy(Qt.ClickFocus)
        self.lineEditSearch.setContextMenuPolicy(Qt.CustomContextMenu)

        self.labelSearchIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.pushButtonSearchClear = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.remove
        )
        self.pushButtonSearchClear.hide()

        self.pushButtonAddNew = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s31, tooltip=QApplication.toolTip.addNewR
        )

        self.layout().addWidget(self.lineEditSearch)
        self.layout().addWidget(self.pushButtonAddNew, alignment=Qt.AlignRight)
        self.lineEditSearch.layout().addWidget(self.labelSearchIcon, alignment=Qt.AlignLeft)
        self.lineEditSearch.layout().addWidget(self.pushButtonSearchClear, alignment=Qt.AlignRight)


class ListWidget(SPGraphics.QuickListWidget):
    def __init__(self, parent):
        super(ListWidget, self).__init__(
            parent, spacing=10, empty_illustration=images.data.illustrations.coin
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
        self.setObjectName(Tab.WALLETS_LIST)

        self.__headerWidget = HeaderWidget(self)
        self.__headerWidget.lineEditSearch.textChanged.connect(self.search_changed)
        self.__headerWidget.pushButtonSearchClear.clicked.connect(self.search_clear_clicked)
        self.__headerWidget.pushButtonAddNew.clicked.connect(self.add_new_clicked)

        self.__listWidget = ListWidget(self)
        self.__listWidget.itemClicked.connect(self.item_clicked)

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__listWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.walletslist)
        self.__headerWidget.labelSearchIcon.setPixmap(images.data.icons.changeable.search21)
        self.__headerWidget.pushButtonSearchClear.setIcon(QIcon(images.data.icons.changeable.broom21))
        self.__headerWidget.pushButtonAddNew.setIcon(QIcon(images.data.icons.changeable.plus21))

    def re_translate(self):
        self.__headerWidget.lineEditSearch.setPlaceholderText(translator("Search"))
        self.__listWidget.labelTitle.setText(translator("No wallets has been added yet!"))
        self.__listWidget.labelDescription.setText(translator(
            "Let's add your first wallet today, click on \"+\" button. It's easy."
        ))

    def re_font(self):
        font = QFont()

        self.__headerWidget.lineEditSearch.setFont(font)
        self.__listWidget.labelDescription.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setPointSize(fonts.data.size.medium)
        self.__listWidget.labelTitle.setFont(font)

    @pyqtSlot(str)
    def search_changed(self, text: str):
        QTimer().singleShot(1000, lambda: self.__search(text))

    @pyqtSlot()
    def search_clear_clicked(self):
        self.__headerWidget.lineEditSearch.clear()

    @pyqtSlot()
    def add_new_clicked(self):
        pass

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem) -> QWidget:
        return self.__listWidget.itemWidget(item)

    def add_item(self, item: SPGraphics.QuickListWidgetItem):
        self.__listWidget.add_quick_item(item)

    def reset(self):
        self.__headerWidget.lineEditSearch.clear()
        self.__listWidget.clear()

    def __search(self, text: str):
        if self.__headerWidget.lineEditSearch.text() != text:
            return

        text = text.lower()
        if text:
            self.__headerWidget.pushButtonSearchClear.show()
            self.__headerWidget.lineEditSearch.setProperty('clearable', True)
        else:
            self.__headerWidget.pushButtonSearchClear.hide()
            self.__headerWidget.lineEditSearch.setProperty('clearable', False)

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

        self.__polish(self.__headerWidget.lineEditSearch)
        self.repaint()

    @staticmethod
    def __polish(widget: QLineEdit):
        widget.style().unpolish(widget)
        widget.style().polish(widget)
