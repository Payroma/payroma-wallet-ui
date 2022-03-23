from plibs import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, validator, assetsicons


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelBalance = None
        self.__labelBalanceValue = None
        self.__comboBoxToken = None
        self.__lineEditAmount = None
        self.__labelAmountIcon = None
        self.__pushButtonMax = None
        self.__lineWidget = None
        self.__pushButtonContinue = None
        self.__loadingEffectContinue = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
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

        self.__comboBoxToken = SPGraphics.QuickComboBox(
            self, max_visible_items=4, icon_size=Size.s24, fixed_size=Size.default
        )
        self.__comboBoxToken.currentIndexChanged.connect(self.token_changed)

        self.__lineEditAmount = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=42
        )
        self.__lineEditAmount.setProperty('iconable', True)
        self.__lineEditAmount.setProperty('iconableRight', True)
        self.__lineEditAmount.setValidator(validator.balance)
        self.__lineEditAmount.setObjectName('lineEditAmount')
        self.__lineEditAmount.textChanged.connect(self.amount_changed)

        self.__labelAmountIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.__pushButtonMax = SPGraphics.QuickPushButton(
            self, fixed_size=QSize(41, 21), value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonMax.clicked.connect(self.max_clicked)

        self.__lineWidget = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget.setObjectName('lineWidget')

        self.__pushButtonContinue = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonContinue.setLayout(QVBoxLayout())
        self.__pushButtonContinue.setDisabled(True)
        self.__pushButtonContinue.clicked.connect(self.continue_clicked)

        self.__loadingEffectContinue = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.layout().addWidget(self.__labelBalance)
        self.layout().addWidget(self.__labelBalanceValue)
        self.layout().addWidget(self.__comboBoxToken, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__lineEditAmount, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__lineWidget)
        self.layout().addWidget(self.__pushButtonContinue, alignment=Qt.AlignHCenter)
        self.__lineEditAmount.layout().addWidget(self.__labelAmountIcon, alignment=Qt.AlignLeft)
        self.__lineEditAmount.layout().addWidget(self.__pushButtonMax, alignment=Qt.AlignRight)
        self.__pushButtonContinue.layout().addWidget(self.__loadingEffectContinue, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.__labelAmountIcon.setPixmap(images.data.icons.changeable.dollar21)

    def re_translate(self):
        self.__labelBalance.setText(translator("Available Balance"))
        self.__lineEditAmount.setPlaceholderText(translator("Amount"))
        self.__pushButtonMax.setText(translator("Max"))
        self.__pushButtonContinue.setText(translator("Continue"))

    def re_font(self):
        font = QFont()

        self.__labelBalance.setFont(font)
        self.__comboBoxToken.view().setFont(font)

        font.setPointSize(fonts.data.size.small)
        self.__pushButtonMax.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__comboBoxToken.setFont(font)
        self.__lineEditAmount.setFont(font)

        font.setBold(True)
        self.__pushButtonContinue.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelBalanceValue.setFont(font)

    @pyqtSlot()
    def max_clicked(self, text: str = ''):
        self.__lineEditAmount.setText(text)
        self.__pushButtonMax.setDisabled(True)

    @pyqtSlot(int)
    def token_changed(self, index: int, balance: str = '0'):
        self.__labelBalanceValue.setText("{} {}".format(balance, self.__comboBoxToken.currentText()))
        self.__lineEditAmount.clear()

    @pyqtSlot(str)
    def amount_changed(self, text: str, valid: bool = False):
        self.__lineEditAmount.setProperty('isValid', valid)
        self.__pushButtonMax.setEnabled(True)
        self.__inputs_validation()

    @pyqtSlot()
    def continue_clicked(self):
        self.__all_inputs_disabled(True)
        self.__loadingEffectContinue.start()
        self.__pushButtonContinue.setText("")

    def continue_completed(self):
        self.__all_inputs_disabled(False)
        self.__loadingEffectContinue.stop()
        QTimer().singleShot(1000, self.re_translate)

    def add_item(self, symbol: str):
        token_icon = assetsicons.get_asset_icon(symbol)
        icon = QIcon(token_icon)
        icon.addPixmap(token_icon, QIcon.Selected, QIcon.Off)
        self.__comboBoxToken.addItem(icon, symbol)

    def get_amount_text(self) -> str:
        return self.__lineEditAmount.text()

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__labelBalanceValue.setText(translator("Loading"))
        self.__comboBoxToken.clear()
        self.__lineEditAmount.clear()

    def __inputs_validation(self):
        valid = False
        if self.__lineEditAmount.property('isValid'):
            valid = True

        self.__pushButtonContinue.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__comboBoxToken.setDisabled(status)
        self.__lineEditAmount.setDisabled(status)
