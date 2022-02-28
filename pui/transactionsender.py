from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress, assetsicons


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__networkWidget = None
        self.__labelNoteIcon = None
        self.__labelNetwork = None
        self.__pushButtonNetwork = None
        self.__lineWidget = None
        self.__labelToAddress = None
        self.__labelFunctionName = None
        self.__labelTokenIcon = None
        self.__labelTokenValue = None
        self.__lineWidget2 = None
        self.__gasWidget = None
        self.__labelEstimatedFee = None
        self.__labelEstimatedFeeValue = None
        self.__labelMaxFee = None
        self.__labelMaxFeeValue = None
        self.__labelTotal = None
        self.__labelTotalValue = None
        self.__labelMaxAmount = None
        self.__labelMaxAmountValue = None
        self.__pushButtonConfirm = None
        self.__loadingEffectConfirm = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(16)
        self.setObjectName(Tab.TRANSACTION_SENDER)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__networkWidget = QWidget(self, flags=Qt.SubWindow)
        self.__networkWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.__networkWidget.setLayout(QGridLayout())
        self.__networkWidget.layout().setAlignment(Qt.AlignCenter)
        self.__networkWidget.layout().setContentsMargins(0, 0, 0, 0)
        self.__networkWidget.layout().setHorizontalSpacing(11)
        self.__networkWidget.layout().setVerticalSpacing(0)

        self.__labelNoteIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s41, pixmap=images.data.icons.info41, align=Qt.AlignCenter
        )

        self.__labelNetwork = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__pushButtonNetwork = SPGraphics.QuickPushButton(
            fixed_height=21, value_changed=QObject.mainModel.textColorAnimated,
            start_value=styles.data.colors.font_description, end_value=styles.data.colors.highlight
        )
        self.__pushButtonNetwork.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__pushButtonNetwork.clicked.connect(self.network_clicked)

        self.__lineWidget = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget.setObjectName('lineWidget')

        self.__labelToAddress = qlabeladdress.QLabelAddress(
            self, tooltip=QObject.toolTip.transactionSendTo, copy_tooltip=QObject.toolTip.copyR
        )
        self.__labelToAddress.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.__labelToAddress.setCursor(Qt.PointingHandCursor)

        self.__labelFunctionName = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__labelTokenIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41, align=Qt.AlignCenter
        )

        self.__labelTokenValue = SPGraphics.QuickLabel(
            self, fixed_height=41
        )

        self.__lineWidget2 = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget2.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget2.setObjectName('lineWidget')

        self.__gasWidget = QWidget(self, flags=Qt.SubWindow)
        self.__gasWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.__gasWidget.setLayout(QGridLayout())
        self.__gasWidget.layout().setContentsMargins(21, 21, 21, 21)
        self.__gasWidget.layout().setSpacing(11)
        self.__gasWidget.setObjectName('gasWidget')

        self.__labelEstimatedFee = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelEstimatedFee.setWordWrap(False)

        self.__labelEstimatedFeeValue = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignRight
        )
        self.__labelEstimatedFeeValue.setWordWrap(False)

        self.__labelMaxFee = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelMaxFee.setWordWrap(False)
        self.__labelMaxFee.setObjectName('labelDescription')

        self.__labelMaxFeeValue = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignRight
        )
        self.__labelMaxFeeValue.setWordWrap(False)
        self.__labelMaxFeeValue.setObjectName('labelDescription')

        self.__labelTotal = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelTotal.setWordWrap(False)

        self.__labelTotalValue = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignRight
        )
        self.__labelTotalValue.setWordWrap(False)

        self.__labelMaxAmount = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelMaxAmount.setWordWrap(False)
        self.__labelMaxAmount.setObjectName('labelDescription')

        self.__labelMaxAmountValue = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignRight
        )
        self.__labelMaxAmountValue.setWordWrap(False)
        self.__labelMaxAmountValue.setObjectName('labelDescription')

        self.__pushButtonConfirm = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QObject.mainModel.backgroundColorAnimated,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonConfirm.setLayout(QVBoxLayout())
        self.__pushButtonConfirm.clicked.connect(self.confirm_clicked)

        self.__loadingEffectConfirm = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.__pushButtonBack.raise_()

        self.layout().addWidget(self.__networkWidget, 0, 0, 1, 2)
        self.layout().addWidget(self.__lineWidget, 1, 0, 1, 2)
        self.layout().addWidget(self.__labelToAddress, 2, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelFunctionName, 3, 0, 1, 2)
        self.layout().addWidget(self.__labelTokenIcon, 4, 0, 1, 1)
        self.layout().addWidget(self.__labelTokenValue, 4, 1, 1, 1, Qt.AlignLeft)
        self.layout().addWidget(self.__lineWidget2, 5, 0, 1, 2)
        self.layout().addWidget(self.__gasWidget, 6, 0, 1, 2)
        self.layout().addWidget(self.__pushButtonConfirm, 7, 0, 1, 2, Qt.AlignHCenter)
        self.__networkWidget.layout().addWidget(self.__labelNoteIcon, 0, 0, 2, 1)
        self.__networkWidget.layout().addWidget(self.__labelNetwork, 0, 1, 1, 1)
        self.__networkWidget.layout().addWidget(self.__pushButtonNetwork, 1, 1, 1, 1)
        self.__gasWidget.layout().addWidget(self.__labelEstimatedFee, 0, 0, 1, 1)
        self.__gasWidget.layout().addWidget(self.__labelEstimatedFeeValue, 0, 1, 1, 1)
        self.__gasWidget.layout().addWidget(self.__labelMaxFee, 1, 0, 1, 1)
        self.__gasWidget.layout().addWidget(self.__labelMaxFeeValue, 1, 1, 1, 1)
        self.__gasWidget.layout().addWidget(self.__labelTotal, 2, 0, 1, 1)
        self.__gasWidget.layout().addWidget(self.__labelTotalValue, 2, 1, 1, 1)
        self.__gasWidget.layout().addWidget(self.__labelMaxAmount, 3, 0, 1, 1)
        self.__gasWidget.layout().addWidget(self.__labelMaxAmountValue, 3, 1, 1, 1)
        self.__pushButtonConfirm.layout().addWidget(self.__loadingEffectConfirm, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.transactionsender)
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))
        self.__labelToAddress.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__labelNetwork.setText(translator("Current Network"))
        self.__labelEstimatedFee.setText(translator("Estimated Gas Fee"))
        self.__labelMaxFee.setText(translator("Max Fee"))
        self.__labelTotal.setText(translator("Total"))
        self.__labelMaxAmount.setText(translator("Max Amount"))
        self.__pushButtonConfirm.setText(translator("Confirm"))

    def re_font(self):
        font = QFont()

        self.__labelToAddress.setFont(font)
        self.__labelMaxFee.setFont(font)
        self.__labelMaxFeeValue.setFont(font)
        self.__labelMaxAmount.setFont(font)
        self.__labelMaxAmountValue.setFont(font)

        font.setPointSize(fonts.data.size.title)
        font.setUnderline(True)
        self.__pushButtonNetwork.setFont(font)

        font.setUnderline(False)
        self.__labelEstimatedFeeValue.setFont(font)
        self.__labelTotalValue.setFont(font)

        font.setBold(True)
        self.__labelNetwork.setFont(font)
        self.__labelEstimatedFee.setFont(font)
        self.__labelTotal.setFont(font)
        self.__pushButtonConfirm.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelFunctionName.setFont(font)
        self.__labelTokenValue.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def network_clicked(self):
        pass

    @pyqtSlot()
    def gas_edit_clicked(self):
        pass

    @pyqtSlot()
    def confirm_clicked(self):
        self.__loadingEffectConfirm.start()
        self.__pushButtonBack.hide()
        self.__pushButtonNetwork.setDisabled(True)
        self.__pushButtonConfirm.setText("")

    def confirm_completed(self):
        self.__loadingEffectConfirm.stop()
        self.__pushButtonBack.show()
        self.__pushButtonNetwork.setEnabled(True)
        QTimer().singleShot(1000, self.re_translate)

    def set_data(
            self, network: str, address: str, function: str, amount: str, symbol: str,
            estimated_gas: str, max_fee: str, total: str, max_amount: str
    ):
        self.__pushButtonNetwork.setText(network)
        self.__labelToAddress.setText(address, False)
        self.__labelFunctionName.setText(function)
        self.__labelTokenIcon.setPixmap(assetsicons.get_asset_icon(symbol))
        self.__labelTokenValue.setText(f'{amount} {symbol}')
        self.__labelEstimatedFeeValue.setText(estimated_gas)
        self.__labelMaxFeeValue.setText(f'{max_fee} {symbol}')
        self.__labelTotalValue.setText(total)
        self.__labelMaxAmountValue.setText(f'{max_amount} {symbol}')
        self.__refresh_effect()

    def reset(self):
        self.__pushButtonNetwork.setText("")
        self.__labelToAddress.clear()
        self.__labelFunctionName.clear()
        self.__labelTokenIcon.clear()
        self.__labelTokenValue.clear()
        self.__labelEstimatedFeeValue.clear()
        self.__labelMaxFeeValue.clear()
        self.__labelTotalValue.clear()
        self.__labelMaxAmountValue.clear()

    def __refresh_effect(self):
        self.__pushButtonConfirm.setDisabled(True)
        self.__gasRefreshMotion = SPGraphics.OpacityMotion(self.__gasWidget)
        self.__gasRefreshMotion.temp_hide(1000, finished=self.__refresh_effect_complete).start()

    def __refresh_effect_complete(self):
        self.__gasRefreshMotion = SPGraphics.OpacityMotion(self.__gasWidget)
        self.__gasRefreshMotion.temp_show(
            500, finished=lambda: self.__pushButtonConfirm.setEnabled(True)
        ).start()
