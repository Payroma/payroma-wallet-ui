from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, validator


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__lineEditSearch = None
        self.__labelSearchIcon = None
        self.__pushButtonSearchClear = None
        self.__pushButtonAddNew = None
        self.__listWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(11, 11, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.WALLETS_LIST)

        self.__lineEditSearch = SPGraphics.QuickLineEdit(
            self, fixed_height=41, layout_support=True, length=40
        )
        self.__lineEditSearch.setMaximumWidth(501)
        self.__lineEditSearch.setFocusPolicy(Qt.ClickFocus)
        self.__lineEditSearch.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__lineEditSearch.setValidator(validator.username)
        self.__lineEditSearch.setObjectName('lineEditSearch')
        self.__lineEditSearch.textChanged.connect(self.search_changed)

        self.__labelSearchIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.__pushButtonSearchClear = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QObject.toolTip.remove
        )
        self.__pushButtonSearchClear.hide()
        self.__pushButtonSearchClear.clicked.connect(self.search_clear_clicked)

        self.__pushButtonAddNew = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.addNewR
        )
        self.__pushButtonAddNew.clicked.connect(self.add_new_clicked)

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

        self.layout().addWidget(self.__lineEditSearch, 0, 0, 1, 1)
        self.layout().addWidget(self.__pushButtonAddNew, 0, 1, 1, 1, Qt.AlignRight)
        self.layout().addWidget(self.__listWidget, 1, 0, 1, 2)
        self.__lineEditSearch.layout().addWidget(self.__labelSearchIcon, alignment=Qt.AlignLeft)
        self.__lineEditSearch.layout().addWidget(self.__pushButtonSearchClear, alignment=Qt.AlignRight)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.walletslist)
        self.__labelSearchIcon.setPixmap(images.data.icons.changeable.search21)
        self.__pushButtonSearchClear.setIcon(QIcon(images.data.icons.changeable.broom21))
        self.__pushButtonAddNew.setIcon(QIcon(images.data.icons.changeable.plus21))

    def re_translate(self):
        self.__lineEditSearch.setPlaceholderText(translator("Search"))
        self.__listWidget.labelTitle.setText(translator("No wallet has been added yet!"))
        self.__listWidget.labelDescription.setText(translator(
            "Let's add your first wallet today, click on \"+\" button. It's easy."
        ))

    def re_font(self):
        font = QFont()

        self.__lineEditSearch.setFont(font)
        self.__listWidget.labelDescription.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setPointSize(fonts.data.size.medium)
        self.__listWidget.labelTitle.setFont(font)

    @pyqtSlot(str)
    def search_changed(self, text: str):
        QTimer().singleShot(1000, lambda: self.__search(text))

    @pyqtSlot()
    def search_clear_clicked(self):
        self.__lineEditSearch.clear()

    @pyqtSlot()
    def add_new_clicked(self):
        pass

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem) -> QWidget:
        return self.__listWidget.itemWidget(item)

    def add_item(self, item: QListWidgetItem):
        self.__listWidget.add_quick_item(item)

    def reset(self):
        self.__lineEditSearch.clear()
        self.__listWidget.clear()

    def __search(self, text: str):
        if self.__lineEditSearch.text() != text:
            return

        text = text.lower()
        if text:
            self.__pushButtonSearchClear.show()
        else:
            self.__pushButtonSearchClear.hide()

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