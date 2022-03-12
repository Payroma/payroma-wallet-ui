from plibs import *
from pui import SetupForm, fonts, styles, images, Size, assetsicons


class UiForm(SPGraphics.QuickListWidgetItem, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__labelIcon = None
        self.__labelName = None
        self.__labelBalance = None
        self.__labelSymbol = None
        self.__pushButtonRemove = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(81)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignVCenter)
        self.layout().setContentsMargins(21, 0, 11, 0)
        self.layout().setHorizontalSpacing(11)
        self.layout().setVerticalSpacing(0)
        self.setGraphicsEffect(SPGraphics.QuickShadow(
            color=styles.data.colors.shadow_a40, radius=40, offset=8
        ))

        self.__labelIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41, align=Qt.AlignCenter
        )

        self.__labelName = SPGraphics.QuickLabel(
            self, fixed_height=31
        )
        self.__labelName.setWordWrap(False)

        self.__labelBalance = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelBalance.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__labelBalance.setWordWrap(False)
        self.__labelBalance.setObjectName('labelDescription')

        self.__labelSymbol = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelSymbol.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__labelSymbol.setObjectName('labelDescription')

        self.__pushButtonRemove = SPGraphics.QuickPushButton(
            self, icon_size=Size.s16, fixed_size=Size.s21, tooltip=QApplication.toolTip.remove
        )
        self.__pushButtonRemove.clicked.connect(self.remove_clicked)

        self.layout().addWidget(self.__labelIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.__labelName, 0, 1, 1, 2)
        self.layout().addWidget(self.__labelBalance, 1, 1, 1, 1)
        self.layout().addWidget(self.__labelSymbol, 1, 2, 1, 1, Qt.AlignLeft)
        self.layout().addWidget(self.__pushButtonRemove, 0, 3, 1, 1, Qt.AlignRight)

        self.item.setSizeHint(self.size())
        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonRemove.setIcon(QIcon(images.data.icons.changeable.close21))

    def re_font(self):
        font = QFont()

        self.__labelSymbol.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__labelBalance.setFont(font)

        font.setBold(True)
        self.__labelName.setFont(font)

    @pyqtSlot()
    def remove_clicked(self):
        pass

    def get_name(self) -> str:
        return self.__labelName.text()

    def get_balance(self) -> str:
        return self.__labelBalance.text()

    def get_symbol(self) -> str:
        return self.__labelSymbol.text()

    def set_name(self, text: str):
        self.__labelName.setText(text)

    def set_balance(self, text: str):
        self.__labelBalance.setText(text)

    def set_symbol(self, text: str):
        icon = assetsicons.get_asset_icon(text)
        self.__labelIcon.setPixmap(icon)
        self.__labelSymbol.setText(text)

    def set_master(self):
        self.__pushButtonRemove.deleteLater()
