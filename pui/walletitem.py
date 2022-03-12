from plibs import *
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress, qnotice


class UiForm(SPGraphics.QuickListWidgetItem, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__labelIcon = None
        self.__labelUsername = None
        self.__labelAddress = None
        self.__checkboxFavorite = None
        self.__qnoticeStatus = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(81)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignVCenter)
        self.layout().setContentsMargins(11, 11, 11, 11)
        self.layout().setVerticalSpacing(0)
        self.setCursor(Qt.PointingHandCursor)
        self.setGraphicsEffect(SPGraphics.QuickShadow(
            color=styles.data.colors.shadow_a40, radius=40, offset=8
        ))

        self.__labelIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s51, pixmap=images.data.icons.wallet51, align=Qt.AlignCenter
        )

        self.__labelUsername = SPGraphics.QuickLabel(
            self, fixed_height=31
        )
        self.__labelUsername.setWordWrap(False)

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, copy_tooltip=QApplication.toolTip.copyR
        )
        self.__labelAddress.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.__checkboxFavorite = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.favoriteR
        )
        self.__checkboxFavorite.setCheckable(True)
        self.__checkboxFavorite.clicked.connect(self.favorite_clicked)

        self.__qnoticeStatus = qnotice.QNotice(
            self, fixed_size=Size.s21, tooltip=QApplication.toolTip.walletStatusR
        )
        self.__qnoticeStatus.setDisabled(True)

        self.layout().addWidget(self.__labelIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.__labelUsername, 0, 1, 1, 1)
        self.layout().addWidget(self.__labelAddress, 1, 1, 1, 1)
        self.layout().addWidget(self.__checkboxFavorite, 0, 2, 1, 1, Qt.AlignRight | Qt.AlignTop)
        self.layout().addWidget(self.__qnoticeStatus, 1, 2, 1, 1, Qt.AlignRight)

        self.item.setSizeHint(self.size())
        super(UiForm, self).setup()

    def re_style(self):
        favorite_icon = QIcon()
        favorite_icon.addPixmap(images.data.icons.changeable.favorite21, QIcon.Normal, QIcon.Off)
        favorite_icon.addPixmap(images.data.icons.favorite_checked21, QIcon.Normal, QIcon.On)
        self.__checkboxFavorite.setIcon(favorite_icon)
        self.__labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_font(self):
        font = QFont()

        self.__labelAddress.setFont(font)

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__labelUsername.setFont(font)

    @pyqtSlot(bool)
    def favorite_clicked(self, state: bool):
        pass

    def get_username(self) -> str:
        return self.__labelUsername.text()

    def get_address(self) -> str:
        return self.__labelAddress.text()

    def set_username(self, text: str):
        self.__labelUsername.setText(text)

    def set_address(self, text: str):
        self.__labelAddress.setText(text)

    def set_favorite(self, state: bool):
        self.__checkboxFavorite.setChecked(state)

    def set_status(self, enabled: bool):
        self.__qnoticeStatus.setEnabled(enabled)
