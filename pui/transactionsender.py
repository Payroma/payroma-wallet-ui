from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress, assetsicons


class NetworkWidget(QWidget):
    def __init__(self, parent):
        super(NetworkWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignLeft)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setHorizontalSpacing(11)
        self.layout().setVerticalSpacing(0)

        self.labelIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s41, pixmap=images.data.icons.info41, align=Qt.AlignCenter
        )

        self.labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelTitle.setWordWrap(False)

        self.pushButton = SPGraphics.QuickPushButton(
            fixed_height=21, value_changed=QApplication.textColorAnimate,
            start_value=styles.data.colors.font_description, end_value=styles.data.colors.highlight
        )
        self.pushButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.layout().addWidget(self.labelIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.labelTitle, 0, 1, 1, 1)
        self.layout().addWidget(self.pushButton, 1, 1, 1, 1)


class GasWidget(QWidget):
    def __init__(self, parent):
        super(GasWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(21, 21, 21, 21)
        self.layout().setSpacing(11)

        self.labelEstimatedFee = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelEstimatedFee.setWordWrap(False)

        self.labelEstimatedFeeValue = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignRight
        )
        self.labelEstimatedFeeValue.setWordWrap(False)

        self.labelMaxFee = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelMaxFee.setWordWrap(False)
        self.labelMaxFee.setObjectName('labelDescription')

        self.labelMaxFeeValue = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignRight
        )
        self.labelMaxFeeValue.setWordWrap(False)
        self.labelMaxFeeValue.setObjectName('labelDescription')

        self.labelTotal = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelTotal.setWordWrap(False)

        self.labelTotalValue = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignRight
        )
        self.labelTotalValue.setWordWrap(False)

        self.labelMaxAmount = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelMaxAmount.setWordWrap(False)
        self.labelMaxAmount.setObjectName('labelDescription')

        self.labelMaxAmountValue = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignRight
        )
        self.labelMaxAmountValue.setWordWrap(False)
        self.labelMaxAmountValue.setObjectName('labelDescription')

        self.layout().addWidget(self.labelEstimatedFee, 0, 0, 1, 1)
        self.layout().addWidget(self.labelEstimatedFeeValue, 0, 1, 1, 1)
        self.layout().addWidget(self.labelMaxFee, 1, 0, 1, 1)
        self.layout().addWidget(self.labelMaxFeeValue, 1, 1, 1, 1)
        self.layout().addWidget(self.labelTotal, 2, 0, 1, 1)
        self.layout().addWidget(self.labelTotalValue, 2, 1, 1, 1)
        self.layout().addWidget(self.labelMaxAmount, 3, 0, 1, 1)
        self.layout().addWidget(self.labelMaxAmountValue, 3, 1, 1, 1)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__networkWidget = None
        self.__lineWidget = None
        self.__labelAddress = None
        self.__labelFunctionName = None
        self.__labelIcon = None
        self.__labelAmount = None
        self.__lineWidget2 = None
        self.__gasWidget = None
        self.__pushButtonConfirm = None
        self.__loadingEffectConfirm = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(16)
        self.setObjectName(Tab.TRANSACTION_SENDER)

        self.__networkWidget = NetworkWidget(self)
        self.__networkWidget.pushButton.clicked.connect(self.network_clicked)

        self.__lineWidget = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget.setObjectName('lineWidget')

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, tooltip=QApplication.toolTip.transactionSendTo, copy_tooltip=QApplication.toolTip.copyR
        )
        self.__labelAddress.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__labelAddress.setCursor(Qt.PointingHandCursor)

        self.__labelFunctionName = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__labelIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41, align=Qt.AlignCenter
        )

        self.__labelAmount = SPGraphics.QuickLabel(
            self, fixed_height=41
        )

        self.__lineWidget2 = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget2.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget2.setObjectName('lineWidget')

        self.__gasWidget = GasWidget(self)

        self.__pushButtonConfirm = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonConfirm.setLayout(QVBoxLayout())
        self.__pushButtonConfirm.clicked.connect(self.confirm_clicked)

        self.__loadingEffectConfirm = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.layout().addWidget(self.__networkWidget, 0, 0, 1, 2)
        self.layout().addWidget(self.__lineWidget, 1, 0, 1, 2)
        self.layout().addWidget(self.__labelAddress, 2, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelFunctionName, 3, 0, 1, 2)
        self.layout().addWidget(self.__labelIcon, 4, 0, 1, 1)
        self.layout().addWidget(self.__labelAmount, 4, 1, 1, 1, Qt.AlignLeft)
        self.layout().addWidget(self.__lineWidget2, 5, 0, 1, 2)
        self.layout().addWidget(self.__gasWidget, 6, 0, 1, 2)
        self.layout().addWidget(self.__pushButtonConfirm, 7, 0, 1, 2, Qt.AlignHCenter)
        self.__pushButtonConfirm.layout().addWidget(self.__loadingEffectConfirm, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.transactionsender)
        self.__labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__networkWidget.labelTitle.setText(translator("Current Network"))
        self.__gasWidget.labelEstimatedFee.setText(translator("Estimated Gas Fee"))
        self.__gasWidget.labelMaxFee.setText(translator("Max Fee"))
        self.__gasWidget.labelTotal.setText(translator("Total"))
        self.__gasWidget.labelMaxAmount.setText(translator("Max Amount"))
        self.__pushButtonConfirm.setText(translator("Confirm"))

    def re_font(self):
        font = QFont()

        self.__labelAddress.setFont(font)
        self.__gasWidget.labelMaxFee.setFont(font)
        self.__gasWidget.labelMaxFeeValue.setFont(font)
        self.__gasWidget.labelMaxAmount.setFont(font)
        self.__gasWidget.labelMaxAmountValue.setFont(font)

        font.setPointSize(fonts.data.size.title)
        font.setUnderline(True)
        self.__networkWidget.pushButton.setFont(font)

        font.setUnderline(False)
        self.__gasWidget.labelEstimatedFeeValue.setFont(font)
        self.__gasWidget.labelTotalValue.setFont(font)

        font.setBold(True)
        self.__networkWidget.labelTitle.setFont(font)
        self.__gasWidget.labelEstimatedFee.setFont(font)
        self.__gasWidget.labelTotal.setFont(font)
        self.__pushButtonConfirm.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelFunctionName.setFont(font)
        self.__labelAmount.setFont(font)

    @pyqtSlot()
    def network_clicked(self):
        pass

    @pyqtSlot()
    def gas_edit_clicked(self):
        pass

    @pyqtSlot()
    def confirm_clicked(self):
        self.__loadingEffectConfirm.start()
        self.__networkWidget.pushButton.setDisabled(True)
        self.__pushButtonConfirm.setText("")

    def confirm_completed(self):
        self.__loadingEffectConfirm.stop()
        self.__networkWidget.pushButton.setEnabled(True)
        QTimer().singleShot(1000, self.re_translate)

    def set_data(
            self, network: str, address: str, function: str, amount: str, symbol: str,
            estimated_gas: str, max_fee: str, total: str, max_amount: str
    ):
        self.__networkWidget.pushButton.setText(network)
        self.__labelAddress.setText(address, False)
        self.__labelFunctionName.setText(function)
        self.__labelIcon.setPixmap(assetsicons.get_asset_icon(symbol))
        self.__labelAmount.setText("{} {}".format(amount, symbol))
        self.__gasWidget.labelEstimatedFeeValue.setText(estimated_gas)
        self.__gasWidget.labelMaxFeeValue.setText("{} {}".format(max_fee, symbol))
        self.__gasWidget.labelTotalValue.setText(total)
        self.__gasWidget.labelMaxAmountValue.setText("{} {}".format(max_amount, symbol))

    def update_gas(self, estimated_gas: str, max_fee: str, total: str, max_amount: str, symbol: str):
        self.__gasWidget.labelEstimatedFeeValue.setText(estimated_gas)
        self.__gasWidget.labelMaxFeeValue.setText("{} {}".format(max_fee, symbol))
        self.__gasWidget.labelTotalValue.setText(total)
        self.__gasWidget.labelMaxAmountValue.setText("{} {}".format(max_amount, symbol))
        self.__refresh_effect()

    def reset(self):
        self.__networkWidget.pushButton.setText("")
        self.__labelAddress.clear()
        self.__labelFunctionName.clear()
        self.__labelIcon.clear()
        self.__labelAmount.clear()
        self.__gasWidget.labelEstimatedFeeValue.clear()
        self.__gasWidget.labelMaxFeeValue.clear()
        self.__gasWidget.labelTotalValue.clear()
        self.__gasWidget.labelMaxAmountValue.clear()

    def __refresh_effect(self):
        self.__pushButtonConfirm.setDisabled(True)
        self.__gasRefreshMotion = SPGraphics.OpacityMotion(self.__gasWidget)
        self.__gasRefreshMotion.temp_hide(1000, finished=self.__refresh_effect_complete).start()

    def __refresh_effect_complete(self):
        self.__gasRefreshMotion = SPGraphics.OpacityMotion(self.__gasWidget)
        self.__gasRefreshMotion.temp_show(
            500, finished=lambda: self.__pushButtonConfirm.setEnabled(True)
        ).start()
