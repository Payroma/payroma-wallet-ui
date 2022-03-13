from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, validator, assetsicons


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelTitle = None
        self.__labelIcon = None
        self.__lineEditAddress = None
        self.__labelAddressAlert = None
        self.__lineEditSymbol = None
        self.__lineEditDecimals = None
        self.__pushButtonAdd = None
        self.__loadingEffectAdd = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.WalletTab.ADD_TOKEN)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QApplication.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.__labelIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s51, pixmap=assetsicons.get_asset_icon(''),
            align=Qt.AlignCenter
        )

        self.__lineEditAddress = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=42
        )
        self.__lineEditAddress.setValidator(validator.address)
        self.__lineEditAddress.textChanged.connect(self.address_changed)

        self.__labelAddressAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QApplication.toolTip.addressAlert
        )
        self.__labelAddressAlert.setCursor(Qt.PointingHandCursor)
        self.__labelAddressAlert.hide()

        self.__lineEditSymbol = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, length=20
        )
        self.__lineEditSymbol.setValidator(validator.symbol)
        self.__lineEditSymbol.textChanged.connect(self.symbol_changed)

        self.__lineEditDecimals = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=2
        )
        self.__lineEditDecimals.setValidator(validator.number)
        self.__lineEditDecimals.textChanged.connect(self.decimals_changed)

        self.__pushButtonAdd = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonAdd.setLayout(QVBoxLayout())
        self.__pushButtonAdd.setDisabled(True)
        self.__pushButtonAdd.clicked.connect(self.add_clicked)

        self.__loadingEffectAdd = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.layout().addWidget(self.__labelTitle)
        self.layout().addWidget(self.__labelIcon, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__lineEditAddress)
        self.layout().addWidget(self.__lineEditSymbol)
        self.layout().addWidget(self.__lineEditDecimals)
        self.layout().addWidget(self.__pushButtonAdd)
        self.__lineEditAddress.layout().addWidget(self.__labelAddressAlert, alignment=Qt.AlignRight)
        self.__pushButtonAdd.layout().addWidget(self.__loadingEffectAdd, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_less_left21))

    def re_translate(self):
        self.__labelTitle.setText(translator("Add Token / Custom Token"))
        self.__lineEditAddress.setPlaceholderText(translator("Contract Address (0x)"))
        self.__lineEditSymbol.setPlaceholderText(translator("Symbol"))
        self.__lineEditDecimals.setPlaceholderText(translator("Decimals"))
        self.__pushButtonAdd.setText(translator("Add Token"))

    def re_font(self):
        font = QFont()

        self.__lineEditAddress.setFont(font)
        self.__lineEditSymbol.setFont(font)
        self.__lineEditDecimals.setFont(font)

        font.setPointSize(fonts.data.size.title)
        font.setBold(True)
        self.__pushButtonAdd.setFont(font)

        font.setPointSize(fonts.data.size.average)
        self.__labelTitle.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot(str)
    def address_changed(self, text: str, valid: bool = False):
        self.__lineEditAddress.setProperty('isValid', valid)
        self.__labelAddressAlert.setHidden(valid or not text)
        self.__polish(self.__lineEditAddress)
        self.__inputs_validation()

    @pyqtSlot(str)
    def symbol_changed(self, text: str, valid: bool = False):
        icon = assetsicons.get_asset_icon(text)
        self.__labelIcon.setPixmap(icon)
        self.__lineEditSymbol.setProperty('isValid', valid)
        self.__inputs_validation()

    @pyqtSlot(str)
    def decimals_changed(self, text: str, valid: bool = False):
        self.__lineEditDecimals.setProperty('isValid', valid)
        self.__inputs_validation()

    @pyqtSlot()
    def add_clicked(self):
        self.__all_inputs_disabled(True)
        self.__loadingEffectAdd.start()
        self.__pushButtonBack.hide()
        self.__pushButtonAdd.setText("")

    def add_completed(self):
        self.__all_inputs_disabled(False)
        self.__loadingEffectAdd.stop()
        self.__pushButtonBack.show()
        QTimer().singleShot(1000, self.re_translate)

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__lineEditAddress.clear()
        self.__lineEditSymbol.clear()
        self.__lineEditDecimals.clear()

    def __inputs_validation(self):
        valid = False
        if (
            self.__lineEditAddress.property('isValid') and
            self.__lineEditSymbol.property('isValid') and
            self.__lineEditDecimals.property('isValid')
        ):
            valid = True

        self.__pushButtonAdd.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__lineEditAddress.setDisabled(status)
        self.__lineEditSymbol.setDisabled(status)
        self.__lineEditDecimals.setDisabled(status)

    @staticmethod
    def __polish(widget: QLineEdit):
        widget.style().unpolish(widget)
        widget.style().polish(widget)
