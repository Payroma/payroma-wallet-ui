import SPGraphics

from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, assetsicons


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelStakeIcon = None
        self.__labelX = None
        self.__labelEarnIcon = None
        self.__labelStakeSymbol = None
        self.__labelEarnSymbol = None
        self.__pushButtonStakeContract = None
        self.__pushButtonEarnContract = None
        self.__pushButtonStakeWebsite = None
        self.__pushButtonEarnWebsite = None
        self.__pushButtonStakingContract = None
        self.__tabWidget = None

        self.__stakeSymbol = ''
        self.__earnSymbol = ''

    def setup(self):
        button_size = QSize(181, 24)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(21, 21, 21, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.STAKE_PAIR)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelStakeIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41, align=Qt.AlignCenter
        )

        self.__labelX = SPGraphics.QuickLabel(
            self, fixed_size=Size.s31
        )

        self.__labelEarnIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41, align=Qt.AlignCenter
        )

        self.__labelStakeSymbol = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.__labelStakeSymbol.setWordWrap(False)

        self.__labelEarnSymbol = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.__labelEarnSymbol.setWordWrap(False)

        self.__pushButtonStakeContract = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size,
            value_changed=QObject.mainModel.textColorAnimated,
            start_value=styles.data.colors.disabled_font, end_value=styles.data.colors.highlight
        )
        self.__pushButtonStakeContract.clicked.connect(self.stake_contract_clicked)

        self.__pushButtonEarnContract = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size,
            value_changed=QObject.mainModel.textColorAnimated,
            start_value=styles.data.colors.disabled_font, end_value=styles.data.colors.highlight
        )
        self.__pushButtonEarnContract.clicked.connect(self.earn_contract_clicked)

        self.__pushButtonStakeWebsite = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size,
            value_changed=QObject.mainModel.textColorAnimated,
            start_value=styles.data.colors.disabled_font, end_value=styles.data.colors.highlight
        )
        self.__pushButtonStakeWebsite.clicked.connect(self.stake_website_clicked)

        self.__pushButtonEarnWebsite = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size,
            value_changed=QObject.mainModel.textColorAnimated,
            start_value=styles.data.colors.disabled_font, end_value=styles.data.colors.highlight
        )
        self.__pushButtonEarnWebsite.clicked.connect(self.earn_website_clicked)

        self.__pushButtonStakingContract = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size,
            value_changed=QObject.mainModel.textColorAnimated,
            start_value=styles.data.colors.disabled_font, end_value=styles.data.colors.highlight
        )
        self.__pushButtonStakingContract.setObjectName('pushButtonStakingContract')
        self.__pushButtonStakingContract.clicked.connect(self.staking_contract_clicked)

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.layout().addWidget(self.__labelStakeIcon, 0, 0, 1, 1, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelX, 0, 1, 1, 1)
        self.layout().addWidget(self.__labelEarnIcon, 0, 2, 1, 1, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelStakeSymbol, 1, 0, 1, 1)
        self.layout().addWidget(self.__labelEarnSymbol, 1, 2, 1, 1)
        self.layout().addWidget(self.__pushButtonStakeContract, 2, 0, 1, 1)
        self.layout().addWidget(self.__pushButtonEarnContract, 2, 2, 1, 1)
        self.layout().addWidget(self.__pushButtonStakeWebsite, 3, 0, 1, 1)
        self.layout().addWidget(self.__pushButtonEarnWebsite, 3, 2, 1, 1)
        self.layout().addWidget(self.__pushButtonStakingContract, 4, 0, 1, 3, Qt.AlignHCenter)
        self.layout().addWidget(self.__tabWidget, 5, 0, 1, 3)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))
        self.__labelX.setPixmap(images.data.icons.changeable.cross31)
        self.__pushButtonStakeContract.setIcon(QIcon(images.data.icons.changeable.external21))
        self.__pushButtonEarnContract.setIcon(QIcon(images.data.icons.changeable.external21))
        self.__pushButtonStakeWebsite.setIcon(QIcon(images.data.icons.changeable.external21))
        self.__pushButtonEarnWebsite.setIcon(QIcon(images.data.icons.changeable.external21))
        self.__pushButtonStakingContract.setIcon(QIcon(images.data.icons.changeable.external21))

    def re_translate(self):
        self.__labelStakeSymbol.setText(f'{translator("Stake")} {self.__stakeSymbol}')
        self.__labelEarnSymbol.setText(f'{translator("Earn")} {self.__earnSymbol}')
        self.__pushButtonStakeContract.setText(translator("Token Contract"))
        self.__pushButtonEarnContract.setText(translator("Token Contract"))
        self.__pushButtonStakeWebsite.setText(translator("Project Website"))
        self.__pushButtonEarnWebsite.setText(translator("Project Website"))
        self.__pushButtonStakingContract.setText(translator("Staking Contract"))

    def re_font(self):
        font = QFont()

        font.setUnderline(True)
        self.__pushButtonStakeContract.setFont(font)
        self.__pushButtonEarnContract.setFont(font)
        self.__pushButtonStakeWebsite.setFont(font)
        self.__pushButtonEarnWebsite.setFont(font)
        self.__pushButtonStakingContract.setFont(font)

        font.setPointSize(fonts.data.size.title)
        font.setUnderline(False)
        font.setBold(True)
        self.__labelStakeSymbol.setFont(font)
        self.__labelEarnSymbol.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def stake_contract_clicked(self):
        pass

    @pyqtSlot()
    def earn_contract_clicked(self):
        pass

    @pyqtSlot()
    def stake_website_clicked(self):
        pass

    @pyqtSlot()
    def earn_website_clicked(self):
        pass

    @pyqtSlot()
    def staking_contract_clicked(self):
        pass

    @pyqtSlot()
    def __tab_changed(self):
        widget = self.__tabWidget.currentWidget()
        self.__tabTransMotion = SPGraphics.OpacityMotion(widget, SPGraphics.Property.OPACITY)
        self.__tabTransMotion.temp_show().start()

    def add_tab(self, model: QObject, name: str):
        self.__tabWidget.addTab(model, name)

    def set_pair(self, stake_symbol: str, earn_symbol: str):
        self.__stakeSymbol = stake_symbol
        self.__earnSymbol = earn_symbol
        self.__labelStakeIcon.setPixmap(assetsicons.get_asset_icon(stake_symbol))
        self.__labelEarnIcon.setPixmap(assetsicons.get_asset_icon(earn_symbol))
        self.re_translate()

    def set_approved(self):
        self.__tabWidget.setCurrentIndex(0)

    def reset(self):
        self.__labelStakeIcon.clear()
        self.__labelEarnIcon.clear()
        self.__labelStakeSymbol.clear()
        self.__labelEarnSymbol.clear()
        self.__tabWidget.setCurrentIndex(1)
