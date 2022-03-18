from plibs import *
from pcontroller import translator
from pui import SetupForm, fonts, styles, Size, assetsicons


class UiForm(SPGraphics.QuickListWidgetItem, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__labelEarnTokenIcon = None
        self.__labelStakeTokenIcon = None
        self.__labelStakeSymbol = None
        self.__labelEarnSymbol = None
        self.__labelAPY = None
        self.__labelAPYValue = None
        self.__labelDuration = None
        self.__labelDurationValue = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(81)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignVCenter)
        self.layout().setContentsMargins(21, 11, 11, 11)
        self.layout().setHorizontalSpacing(16)
        self.layout().setVerticalSpacing(0)
        self.setCursor(Qt.PointingHandCursor)
        self.setGraphicsEffect(SPGraphics.QuickShadow(
            color=styles.data.colors.shadow_a40, radius=40, offset=8
        ))

        self.__labelEarnTokenIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41
        )

        self.__labelStakeTokenIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s24
        )
        self.__labelStakeTokenIcon.setObjectName('labelStakeTokenIcon')

        self.__labelStakeSymbol = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelStakeSymbol.setWordWrap(False)
        self.__labelStakeSymbol.setObjectName('labelDescription')

        self.__labelEarnSymbol = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelEarnSymbol.setWordWrap(False)

        self.__labelAPY = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelAPY.setObjectName('labelDescription')

        self.__labelAPYValue = SPGraphics.QuickLabel(
            self, translator("Loading"), fixed_height=21
        )
        self.__labelAPYValue.setObjectName('labelAPYValue')

        self.__labelDuration = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelDuration.setObjectName('labelDescription')

        self.__labelDurationValue = SPGraphics.QuickLabel(
            self, translator("Loading"), fixed_height=21
        )

        self.layout().addWidget(self.__labelEarnTokenIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.__labelStakeTokenIcon, 0, 0, 2, 1, Qt.AlignRight | Qt.AlignBottom)
        self.layout().addWidget(self.__labelStakeSymbol, 0, 1, 1, 1)
        self.layout().addWidget(self.__labelEarnSymbol, 1, 1, 1, 1)
        self.layout().addWidget(self.__labelAPY, 0, 2, 1, 1)
        self.layout().addWidget(self.__labelAPYValue, 1, 2, 1, 1)
        self.layout().addWidget(self.__labelDuration, 0, 3, 1, 1)
        self.layout().addWidget(self.__labelDurationValue, 1, 3, 1, 1)

        self.item.setSizeHint(self.size())
        super(UiForm, self).setup()

    def re_translate(self):
        self.__labelAPY.setText(translator("APY"))
        self.__labelDuration.setText(translator("Duration"))

    def re_font(self):
        font = QFont()

        self.__labelStakeSymbol.setFont(font)
        self.__labelAPY.setFont(font)
        self.__labelDuration.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__labelAPYValue.setFont(font)
        self.__labelDurationValue.setFont(font)

        font.setBold(True)
        self.__labelEarnSymbol.setFont(font)

    def set_pair_symbols(self, stake: str, earn: str):
        self.__labelStakeTokenIcon.setPixmap(assetsicons.get_asset_icon(stake))
        self.__labelEarnTokenIcon.setPixmap(assetsicons.get_asset_icon(earn))
        self.__labelStakeSymbol.setText("{} {}".format(translator("Stake"), stake))
        self.__labelEarnSymbol.setText("{} {}".format(translator("Earn"), earn))

    def set_apy(self, value: int):
        self.__labelAPYValue.setText("{:,}%".format(value))

    def set_duration_type(self, locked: bool):
        self.__labelDurationValue.setText(translator("Locked" if locked else "Flexible Lock"))
