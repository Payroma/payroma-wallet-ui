from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, assetsicons


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignHCenter)
        self.layout().setContentsMargins(11, 11, 11, 11)
        self.layout().setHorizontalSpacing(31)

        self.labelBlock = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelBlock.setObjectName('labelDescription')

        self.__blockValueWidget = QWidget(self, flags=Qt.SubWindow)
        self.__blockValueWidget.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__blockValueWidget.setLayout(QHBoxLayout())
        self.__blockValueWidget.layout().setContentsMargins(0, 0, 0, 0)

        self.labelBlockValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelBlockValue.setWordWrap(False)

        self.pushButtonBlockTime = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.showBlockTime
        )

        self.labelTotalStaked = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelTotalStaked.setObjectName('labelDescription')

        self.__totalStakedValueWidget = QWidget(self, flags=Qt.SubWindow)
        self.__totalStakedValueWidget.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__totalStakedValueWidget.setLayout(QHBoxLayout())
        self.__totalStakedValueWidget.layout().setContentsMargins(0, 0, 0, 0)

        self.labelTotalStakedValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelTotalStakedValue.setWordWrap(False)

        self.pushButtonStakingContract = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.viewExplorer
        )

        self.layout().addWidget(self.labelBlock, 0, 0, 1, 1)
        self.layout().addWidget(self.__blockValueWidget, 1, 0, 1, 1)
        self.layout().addWidget(self.labelTotalStaked, 0, 1, 1, 1)
        self.layout().addWidget(self.__totalStakedValueWidget, 1, 1, 1, 1)
        self.__blockValueWidget.layout().addWidget(self.labelBlockValue)
        self.__blockValueWidget.layout().addWidget(self.pushButtonBlockTime)
        self.__totalStakedValueWidget.layout().addWidget(self.labelTotalStakedValue)
        self.__totalStakedValueWidget.layout().addWidget(self.pushButtonStakingContract)


class PairWidget(QWidget):
    def __init__(self, parent):
        super(PairWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(11)

        self.labelIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41, align=Qt.AlignCenter
        )

        self.labelSymbol = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.labelSymbol.setWordWrap(False)

        self.pushButtonWebsite = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.projectWebsiteB
        )

        self.pushButtonContract = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.viewProjectExplorerB
        )

        self.layout().addWidget(self.labelIcon, 0, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.labelSymbol, 1, 0, 1, 2)
        self.layout().addWidget(self.pushButtonWebsite, 2, 0, 1, 1, Qt.AlignRight)
        self.layout().addWidget(self.pushButtonContract, 2, 1, 1, 1, Qt.AlignLeft)


class PairsWidget(QWidget):
    def __init__(self, parent):
        super(PairsWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignHCenter)
        self.layout().setContentsMargins(11, 21, 11, 0)
        self.layout().setSpacing(51)

        self.labelStakeWidget = PairWidget(self)

        self.labelX = SPGraphics.QuickLabel(
            self, fixed_size=Size.s31
        )

        self.labelEarnWidget = PairWidget(self)

        self.layout().addWidget(self.labelStakeWidget)
        self.layout().addWidget(self.labelX, alignment=Qt.AlignTop)
        self.layout().addWidget(self.labelEarnWidget)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__headerWidget = None
        self.__parisWidget = None
        self.__tabWidget = None

        self.__stakeSymbol = ''
        self.__earnSymbol = ''

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.STAKE_PAIR)

        self.__headerWidget = HeaderWidget(self)
        self.__headerWidget.pushButtonBlockTime.clicked.connect(self.block_time_clicked)
        self.__headerWidget.pushButtonStakingContract.clicked.connect(self.staking_contract_clicked)

        self.__parisWidget = PairsWidget(self)
        self.__parisWidget.labelStakeWidget.pushButtonWebsite.clicked.connect(self.stake_website_clicked)
        self.__parisWidget.labelStakeWidget.pushButtonContract.clicked.connect(self.stake_contract_clicked)
        self.__parisWidget.labelEarnWidget.pushButtonWebsite.clicked.connect(self.earn_website_clicked)
        self.__parisWidget.labelEarnWidget.pushButtonContract.clicked.connect(self.earn_contract_clicked)

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__parisWidget)
        self.layout().addWidget(self.__tabWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.stakepair)
        self.__headerWidget.pushButtonBlockTime.setIcon(QIcon(images.data.icons.changeable.time21))
        self.__headerWidget.pushButtonStakingContract.setIcon(
            QIcon(images.data.icons.changeable.external21)
        )
        self.__parisWidget.labelStakeWidget.pushButtonWebsite.setIcon(
            QIcon(images.data.icons.changeable.web21)
        )
        self.__parisWidget.labelStakeWidget.pushButtonContract.setIcon(
            QIcon(images.data.icons.changeable.external21)
        )
        self.__parisWidget.labelX.setPixmap(images.data.icons.changeable.cross31)
        self.__parisWidget.labelEarnWidget.pushButtonWebsite.setIcon(
            QIcon(images.data.icons.changeable.web21)
        )
        self.__parisWidget.labelEarnWidget.pushButtonContract.setIcon(
            QIcon(images.data.icons.changeable.external21)
        )

    def re_translate(self):
        self.__headerWidget.labelTotalStaked.setText(translator("Total Staked"))
        self.__parisWidget.labelStakeWidget.labelSymbol.setText(
            "{} {}".format(translator("Stake"), self.__stakeSymbol)
        )
        self.__parisWidget.labelEarnWidget.labelSymbol.setText(
            "{} {}".format(translator("Earn"), self.__earnSymbol)
        )

    def re_font(self):
        font = QFont()

        self.__headerWidget.labelBlock.setFont(font)
        self.__headerWidget.labelTotalStaked.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__headerWidget.labelBlockValue.setFont(font)
        self.__headerWidget.labelTotalStakedValue.setFont(font)

        font.setBold(True)
        self.__parisWidget.labelStakeWidget.labelSymbol.setFont(font)
        self.__parisWidget.labelEarnWidget.labelSymbol.setFont(font)

    @pyqtSlot()
    def block_time_clicked(self):
        pass

    @pyqtSlot()
    def staking_contract_clicked(self):
        pass

    @pyqtSlot()
    def stake_website_clicked(self):
        pass

    @pyqtSlot()
    def stake_contract_clicked(self):
        pass

    @pyqtSlot()
    def earn_website_clicked(self):
        pass

    @pyqtSlot()
    def earn_contract_clicked(self):
        pass

    def add_tab(self, model: QObject, name: str):
        self.__tabWidget.addTab(model, name)

    def set_data(
            self, block_title: str, blocks: int, total_staked: str, stake_symbol: str, earn_symbol: str
    ):
        self.__stakeSymbol = stake_symbol
        self.__earnSymbol = earn_symbol
        self.__headerWidget.labelBlock.setText(translator(block_title))
        self.__parisWidget.labelStakeWidget.labelIcon.setPixmap(assetsicons.get_asset_icon(stake_symbol))
        self.__parisWidget.labelEarnWidget.labelIcon.setPixmap(assetsicons.get_asset_icon(earn_symbol))
        self.update_blocks(blocks)
        self.update_total_staked(total_staked, stake_symbol)
        self.re_translate()

    def update_blocks(self, blocks: int):
        self.__headerWidget.labelBlockValue.setText('{:,} {}'.format(blocks, translator("Blocks")))

    def update_total_staked(self, text: str, symbol: str):
        self.__headerWidget.labelTotalStakedValue.setText("{} {}".format(text, symbol))

    def set_approved(self):
        self.__tabWidget.setCurrentIndex(1)
        self.__tab_changed()

    def reset(self):
        self.__headerWidget.labelBlock.clear()
        self.__headerWidget.labelBlockValue.clear()
        self.__headerWidget.labelTotalStakedValue.clear()
        self.__parisWidget.labelStakeWidget.labelIcon.clear()
        self.__parisWidget.labelStakeWidget.labelSymbol.clear()
        self.__parisWidget.labelEarnWidget.labelIcon.clear()
        self.__parisWidget.labelEarnWidget.labelSymbol.clear()
        self.__tabWidget.setCurrentIndex(0)

    def __tab_changed(self):
        widget = self.__tabWidget.currentWidget()
        self.__tabTransMotion = SPGraphics.OpacityMotion(widget, SPGraphics.Property.OPACITY)
        self.__tabTransMotion.temp_show().start()
