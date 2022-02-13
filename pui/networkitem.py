from plibs import *
from pui import SetupForm, fonts, styles, Size, qnotice, assetsicons


class UiForm(SPGraphics.QuickListWidgetItem, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__labelIcon = None
        self.__labelSymbol = None
        self.__labelName = None
        self.__qnoticeStatus = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(81)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignVCenter)
        self.layout().setContentsMargins(21, 0, 11, 0)
        self.layout().setHorizontalSpacing(11)
        self.layout().setVerticalSpacing(0)
        self.setCursor(Qt.PointingHandCursor)
        self.setGraphicsEffect(SPGraphics.QuickShadow(
            color=styles.data.colors.shadow_a40, radius=40, offset=8
        ))

        self.__labelIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41, align=Qt.AlignCenter
        )

        self.__labelSymbol = SPGraphics.QuickLabel(
            self, fixed_height=31
        )

        self.__labelName = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelName.setObjectName('labelDescription')

        self.__qnoticeStatus = qnotice.QNotice(
            self, fixed_size=Size.s21, tooltip=QObject.toolTip.networkStatusR
        )
        self.__qnoticeStatus.setDisabled(True)

        self.layout().addWidget(self.__labelIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.__labelSymbol, 0, 1, 1, 1)
        self.layout().addWidget(self.__labelName, 1, 1, 1, 1)
        self.layout().addWidget(self.__qnoticeStatus, 0, 2, 1, 1, Qt.AlignRight)

        self.item.setSizeHint(self.size())
        super(UiForm, self).setup()

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.title)
        self.__labelName.setFont(font)

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__labelSymbol.setFont(font)

    def get_symbol(self) -> str:
        return self.__labelSymbol.text()

    def get_name(self) -> str:
        return self.__labelName.text()

    def set_symbol(self, text: str):
        icon = assetsicons.get_asset_icon(text)
        self.__labelIcon.setPixmap(icon)
        self.__labelSymbol.setText(text)

    def set_name(self, text: str):
        self.__labelName.setText(text)

    def set_status(self, enabled: bool):
        self.__qnoticeStatus.setEnabled(enabled)
