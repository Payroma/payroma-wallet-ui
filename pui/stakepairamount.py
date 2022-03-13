from plibs import *
from pcontroller import translator
from pui import SetupForm, fonts, styles, Size, validator, assetsicons


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelBalance = None
        self.__labelBalanceValue = None
        self.__labelStakedBalance = None
        self.__labelStakedBalanceValue = None
        self.__lineEditDeposit = None
        self.__labelDepositIcon = None
        self.__pushButtonDeposit = None
        self.__lineEditWithdraw = None
        self.__labelWithdrawIcon = None
        self.__pushButtonWithdraw = None
        self.__lineEditClaim = None
        self.__labelClaimIcon = None
        self.__pushButtonClaim = None

    def setup(self):
        button_size = QSize(71, 31)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(11)

        self.__labelBalance = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelBalance.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__labelBalance.setObjectName('labelDescription')

        self.__labelBalanceValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelBalanceValue.setWordWrap(False)

        self.__labelStakedBalance = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelStakedBalance.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__labelStakedBalance.setObjectName('labelDescription')

        self.__labelStakedBalanceValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelStakedBalanceValue.setWordWrap(False)

        self.__lineEditDeposit = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=42
        )
        self.__lineEditDeposit.setProperty('iconable', True)
        self.__lineEditDeposit.setValidator(validator.balance)
        self.__lineEditDeposit.setObjectName('lineEditDeposit')
        self.__lineEditDeposit.textChanged.connect(self.deposit_changed)

        self.__labelDepositIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21
        )

        self.__pushButtonDeposit = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonDeposit.setDisabled(True)
        self.__pushButtonDeposit.clicked.connect(self.deposit_clicked)

        self.__lineEditWithdraw = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=42
        )
        self.__lineEditWithdraw.setProperty('iconable', True)
        self.__lineEditWithdraw.setValidator(validator.balance)
        self.__lineEditWithdraw.setObjectName('lineEditWithdraw')
        self.__lineEditWithdraw.textChanged.connect(self.withdraw_changed)

        self.__labelWithdrawIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21
        )

        self.__pushButtonWithdraw = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonWithdraw.setDisabled(True)
        self.__pushButtonWithdraw.clicked.connect(self.withdraw_clicked)

        self.__lineEditClaim = SPGraphics.QuickLineEdit(
            self, writable=False, fixed_size=Size.default, layout_support=True, length=42
        )
        self.__lineEditClaim.setProperty('iconable', True)
        self.__lineEditClaim.setObjectName('lineEditClaim')
        self.__lineEditClaim.textChanged.connect(self.claim_changed)

        self.__labelClaimIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21
        )

        self.__pushButtonClaim = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonClaim.setDisabled(True)
        self.__pushButtonClaim.clicked.connect(self.claim_clicked)

        self.layout().addWidget(self.__labelBalance, 0, 0, 1, 1)
        self.layout().addWidget(self.__labelBalanceValue, 0, 1, 1, 1)
        self.layout().addWidget(self.__labelStakedBalance, 1, 0, 1, 1)
        self.layout().addWidget(self.__labelStakedBalanceValue, 1, 1, 1, 1)
        self.layout().addWidget(self.__lineEditDeposit, 2, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__lineEditWithdraw, 3, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__lineEditClaim, 4, 0, 1, 2, Qt.AlignHCenter)
        self.__lineEditDeposit.layout().addWidget(self.__labelDepositIcon, alignment=Qt.AlignLeft)
        self.__lineEditDeposit.layout().addWidget(self.__pushButtonDeposit, alignment=Qt.AlignRight)
        self.__lineEditWithdraw.layout().addWidget(self.__labelWithdrawIcon, alignment=Qt.AlignLeft)
        self.__lineEditWithdraw.layout().addWidget(self.__pushButtonWithdraw, alignment=Qt.AlignRight)
        self.__lineEditClaim.layout().addWidget(self.__labelClaimIcon, alignment=Qt.AlignLeft)
        self.__lineEditClaim.layout().addWidget(self.__pushButtonClaim, alignment=Qt.AlignRight)

        super(UiForm, self).setup()

    def re_translate(self):
        self.__labelBalance.setText(translator("Available"))
        self.__labelStakedBalance.setText(translator("Staked"))
        self.__lineEditDeposit.setPlaceholderText(translator("Amount"))
        self.__pushButtonDeposit.setText(translator("Deposit"))
        self.__lineEditWithdraw.setPlaceholderText(translator("Amount"))
        self.__pushButtonWithdraw.setText(translator("Withdraw"))
        self.__pushButtonClaim.setText(translator("Claim"))

    def re_font(self):
        font = QFont()

        self.__labelBalance.setFont(font)
        self.__labelStakedBalance.setFont(font)

        font.setPointSize(fonts.data.size.small)
        self.__pushButtonDeposit.setFont(font)
        self.__pushButtonWithdraw.setFont(font)
        self.__pushButtonClaim.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__lineEditDeposit.setFont(font)
        self.__lineEditWithdraw.setFont(font)

        font.setBold(True)
        self.__labelBalanceValue.setFont(font)
        self.__labelStakedBalanceValue.setFont(font)
        self.__lineEditClaim.setFont(font)

    @pyqtSlot()
    def deposit_clicked(self):
        pass

    @pyqtSlot()
    def withdraw_clicked(self):
        pass

    @pyqtSlot()
    def claim_clicked(self):
        pass

    @pyqtSlot(str)
    def deposit_changed(self, text: str, valid: bool = False):
        self.__pushButtonDeposit.setEnabled(valid)

    @pyqtSlot(str)
    def withdraw_changed(self, text: str, valid: bool = False):
        self.__pushButtonWithdraw.setEnabled(valid)

    @pyqtSlot(str)
    def claim_changed(self, text: str, valid: bool = False):
        self.__pushButtonClaim.setEnabled(valid)

    def set_data(self, balance: str, staked: str, claim: str, stake_symbol: str, earn_symbol: str):
        self.__labelBalanceValue.setText("{} {}".format(balance, stake_symbol))
        self.__labelStakedBalanceValue.setText("{} {}".format(staked, stake_symbol))
        self.__labelDepositIcon.setPixmap(assetsicons.get_asset_icon(stake_symbol))
        self.__labelWithdrawIcon.setPixmap(assetsicons.get_asset_icon(stake_symbol))
        self.update_claim(claim, earn_symbol)

    def update_claim(self, text: str, symbol: str):
        self.__labelClaimIcon.setPixmap(assetsicons.get_asset_icon(symbol))
        self.__lineEditClaim.setText(text)

    def reset(self):
        self.__labelBalanceValue.clear()
        self.__labelStakedBalanceValue.clear()
        self.__lineEditDeposit.clear()
        self.__lineEditWithdraw.clear()
        self.__lineEditClaim.clear()
