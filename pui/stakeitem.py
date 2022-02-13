from plibs import *
from pcontroller import translator
from pui import SetupForm, fonts, styles, images, Size, assetsicons


class UiForm(SPGraphics.QuickListWidgetItem, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__labelEarnTokenIcon = None
        self.__labelStakeTokenIcon = None
        self.__labelStakeCoin = None
        self.__labelEarnCoin = None
        self.__labelAPY = None
        self.__labelAPYValue = None
        self.__labelBlock = None
        self.__pushButtonBlockTime = None
        self.__labelBlockValue = None
        self.__labelDuration = None
        self.__labelDurationValue = None
        self.__labelTotalStaked = None
        self.__labelTotalStakedValue = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setMinimumWidth(701)
        self.setFixedHeight(81)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignVCenter)
        self.layout().setContentsMargins(21, 11, 21, 11)
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

        self.__labelStakeCoin = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelStakeCoin.setWordWrap(False)
        self.__labelStakeCoin.setObjectName('labelDescription')

        self.__labelEarnCoin = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelEarnCoin.setWordWrap(False)

        self.__labelAPY = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelAPY.setObjectName('labelDescription')

        self.__labelAPYValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelAPYValue.setObjectName('labelAPYValue')

        self.__labelBlock = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelBlock.setObjectName('labelDescription')

        self.__pushButtonBlockTime = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QObject.toolTip.ShowBlockTime
        )
        self.__pushButtonBlockTime.clicked.connect(self.block_time_clicked)

        self.__labelBlockValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__labelDuration = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelDuration.setObjectName('labelDescription')

        self.__labelDurationValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__labelTotalStaked = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelTotalStaked.setObjectName('labelDescription')

        self.__labelTotalStakedValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.layout().addWidget(self.__labelEarnTokenIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.__labelStakeTokenIcon, 0, 0, 2, 1, Qt.AlignRight | Qt.AlignBottom)
        self.layout().addWidget(self.__labelStakeCoin, 0, 1, 1, 1)
        self.layout().addWidget(self.__labelEarnCoin, 1, 1, 1, 1)
        self.layout().addWidget(self.__labelAPY, 0, 2, 1, 1)
        self.layout().addWidget(self.__labelAPYValue, 1, 2, 1, 1)
        self.layout().addWidget(self.__pushButtonBlockTime, 1, 2, 1, 1, Qt.AlignRight)
        self.layout().addWidget(self.__labelBlock, 0, 3, 1, 1)
        self.layout().addWidget(self.__labelBlockValue, 1, 3, 1, 1)
        self.layout().addWidget(self.__labelDuration, 0, 4, 1, 1)
        self.layout().addWidget(self.__labelDurationValue, 1, 4, 1, 1)
        self.layout().addWidget(self.__labelTotalStaked, 0, 5, 1, 1)
        self.layout().addWidget(self.__labelTotalStakedValue, 1, 5, 1, 1)

        self.item.setSizeHint(self.size())
        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBlockTime.setIcon(QIcon(images.data.icons.changeable.time21))

    def re_translate(self):
        self.__labelAPY.setText(translator("APY"))
        self.__labelDuration.setText(translator("Duration"))
        self.__labelTotalStaked.setText(translator("Total Staked"))

    def re_font(self):
        font = QFont()

        self.__labelStakeCoin.setFont(font)
        self.__labelAPY.setFont(font)
        self.__labelBlock.setFont(font)
        self.__labelDuration.setFont(font)
        self.__labelTotalStaked.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__labelAPYValue.setFont(font)
        self.__labelBlockValue.setFont(font)
        self.__labelDurationValue.setFont(font)
        self.__labelTotalStakedValue.setFont(font)

        font.setBold(True)
        self.__labelEarnCoin.setFont(font)

    @pyqtSlot()
    def block_time_clicked(self):
        pass

    def set_pair_symbols(self, stake: str, earn: str):
        self.__labelEarnTokenIcon.setPixmap(assetsicons.get_asset_icon(earn))
        self.__labelStakeTokenIcon.setPixmap(assetsicons.get_asset_icon(stake))
        self.__labelStakeCoin.setText(translator("Stake") + f' {stake}')
        self.__labelEarnCoin.setText(translator("Earn") + f' {earn}')

    def set_apy(self, text: str):
        self.__labelAPYValue.setText(text)

    def set_block_number(self, text: str, title: str = 'Ends in'):
        self.__labelBlock.setText(translator(title))
        self.__labelBlockValue.setText(f'{text} ' + translator("Blocks"))

    def set_duration_type(self, locked: bool):
        if locked:
            self.__labelDurationValue.setText(translator("Locked"))
        else:
            self.__labelDurationValue.setText(translator("Flexible Lock"))

    def set_total_staked(self, text: str, symbol: str):
        self.__labelTotalStakedValue.setText(f'{text} {symbol}')
