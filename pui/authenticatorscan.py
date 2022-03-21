from plibs import *
from pheader import *
from pcontroller import translator, to_qr_code
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress


class CodeInputWidget(QWidget):
    def __init__(self, parent, text_changed):
        super(CodeInputWidget, self).__init__(parent, flags=Qt.SubWindow)

        font = QFont('Roboto', 18)
        line_edit_size = QSize(41, 51)
        self.textChanged = text_changed

        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.__lineEdit1 = SPGraphics.QuickLineEdit(
            self, placeholder_text='-', numeric=True, align=Qt.AlignHCenter,
            fixed_size=line_edit_size, length=1
        )
        self.__lineEdit1.setFont(font)
        self.__lineEdit1.textChanged.connect(self.__auto_cursor_move)

        self.__lineEdit2 = SPGraphics.QuickLineEdit(
            self, placeholder_text='-', numeric=True, align=Qt.AlignHCenter,
            fixed_size=line_edit_size, length=1
        )
        self.__lineEdit2.setFont(font)
        self.__lineEdit2.textChanged.connect(self.__auto_cursor_move)

        self.__lineEdit3 = SPGraphics.QuickLineEdit(
            self, placeholder_text='-', numeric=True, align=Qt.AlignHCenter,
            fixed_size=line_edit_size, length=1
        )
        self.__lineEdit3.setFont(font)
        self.__lineEdit3.textChanged.connect(self.__auto_cursor_move)

        self.__spaceWidget = SPGraphics.QuickWidget(
            self, fixed_width=11
        )

        self.__lineEdit4 = SPGraphics.QuickLineEdit(
            self, placeholder_text='-', numeric=True, align=Qt.AlignHCenter,
            fixed_size=line_edit_size, length=1
        )
        self.__lineEdit4.setFont(font)
        self.__lineEdit4.textChanged.connect(self.__auto_cursor_move)

        self.__lineEdit5 = SPGraphics.QuickLineEdit(
            self, placeholder_text='-', numeric=True, align=Qt.AlignHCenter,
            fixed_size=line_edit_size, length=1
        )
        self.__lineEdit5.setFont(font)
        self.__lineEdit5.textChanged.connect(self.__auto_cursor_move)

        self.__lineEdit6 = SPGraphics.QuickLineEdit(
            self, placeholder_text='-', numeric=True, align=Qt.AlignHCenter,
            fixed_size=line_edit_size, length=1
        )
        self.__lineEdit6.setFont(font)
        self.__lineEdit6.textChanged.connect(self.__auto_cursor_move)

        self.layout().addWidget(self.__lineEdit1)
        self.layout().addWidget(self.__lineEdit2)
        self.layout().addWidget(self.__lineEdit3)
        self.layout().addWidget(self.__spaceWidget)
        self.layout().addWidget(self.__lineEdit4)
        self.layout().addWidget(self.__lineEdit5)
        self.layout().addWidget(self.__lineEdit6)

    def clear(self):
        self.__lineEdit1.clear()
        self.__lineEdit2.clear()
        self.__lineEdit3.clear()
        self.__lineEdit4.clear()
        self.__lineEdit5.clear()
        self.__lineEdit6.clear()

    @pyqtSlot(str)
    def __auto_cursor_move(self, text: str):
        inputs = [
            self.__lineEdit1, self.__lineEdit2, self.__lineEdit3,
            self.__lineEdit4, self.__lineEdit5, self.__lineEdit6
        ]
        line_edit = self.sender()
        current_index = inputs.index(line_edit)

        if text and current_index < 5:
            inputs[current_index + 1].setFocus()

        elif not text and current_index > 0:
            inputs[current_index - 1].setFocus()

        code = ''.join(i.text() for i in inputs)
        self.textChanged(code)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelTitle = None
        self.__labelDescription = None
        self.__labelQR = None
        self.__labelQRDescription = None
        self.__labelKey = None
        self.__labelInputTitle = None
        self.__codeInputWidget = None
        self.__pushButtonConfirm = None
        self.__loadingEffectConfirm = None

    def setup(self):
        font = QFont('Roboto', 18)
        line_edit_size = QSize(41, 51)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.AuthenticatorSetupTab.SCAN)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QApplication.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.__labelDescription = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignHCenter
        )
        self.__labelDescription.setWordWrap(False)

        self.__labelQR = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=QSize(131, 131)
        )

        self.__labelQRDescription = SPGraphics.QuickLabel(
            self, fixed_height=31
        )

        self.__labelKey = qlabeladdress.QLabelAddress(
            self, fixed_height=21, copy_tooltip=QApplication.toolTip.copyR
        )

        self.__labelInputTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignHCenter
        )

        self.__codeInputWidget = CodeInputWidget(self, text_changed=self.otp_code_changed)

        self.__pushButtonConfirm = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonConfirm.setLayout(QVBoxLayout())
        self.__pushButtonConfirm.setDisabled(True)
        self.__pushButtonConfirm.clicked.connect(self.confirm_clicked)

        self.__loadingEffectConfirm = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.__pushButtonBack.raise_()

        self.layout().addWidget(self.__labelTitle, 0, 0, 1, 2)
        self.layout().addWidget(self.__labelDescription, 1, 0, 1, 2)
        self.layout().addWidget(self.__labelQR, 3, 0, 2, 1)
        self.layout().addWidget(self.__labelQRDescription, 3, 1, 1, 1, Qt.AlignVCenter)
        self.layout().addWidget(self.__labelKey, 4, 1, 1, 1, Qt.AlignTop)
        self.layout().addWidget(self.__labelInputTitle, 5, 0, 1, 2)
        self.layout().addWidget(self.__codeInputWidget, 6, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonConfirm, 7, 0, 1, 2, Qt.AlignHCenter)
        self.__pushButtonConfirm.layout().addWidget(self.__loadingEffectConfirm, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_less_left21))
        self.__labelKey.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__labelTitle.setText(translator("Scan QR Code"))
        self.__labelDescription.setText(translator("Scan this QR code in your authenticator app."))
        self.__labelQRDescription.setText(translator(
            "If you are unable to scan this QR code,\nPlease enter this key manually into the app."
        ))
        self.__labelInputTitle.setText(translator("Confirmation Code"))
        self.__pushButtonConfirm.setText(translator("Confirm"))

    def re_font(self):
        font = QFont()

        self.__labelQRDescription.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__labelDescription.setFont(font)
        self.__labelKey.setFont(font)
        self.__labelInputTitle.setFont(font)

        font.setBold(True)
        self.__pushButtonConfirm.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelTitle.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    def otp_code_changed(self, text: str, valid: bool = False):
        self.__codeInputWidget.setProperty('isValid', valid)
        self.__inputs_validation()

    @pyqtSlot()
    def confirm_clicked(self):
        self.__all_inputs_disabled(True)
        self.__loadingEffectConfirm.start()
        self.__pushButtonBack.hide()
        self.__pushButtonConfirm.setText("")

    def confirm_completed(self):
        self.__all_inputs_disabled(False)
        self.__loadingEffectConfirm.stop()
        self.__pushButtonBack.show()
        self.__codeInputWidget.clear()
        QTimer().singleShot(1000, self.re_translate)

    def set_data(self, username: str, key: str):
        title = 'Payroma%20Wallet'
        qr_format = f'otpauth://totp/{title}:{username}?secret={key}&issuer={title}'
        pixmap = to_qr_code(qr_format, self.__labelQR.size())
        self.__labelQR.setPixmap(pixmap)
        self.__labelKey.setText(key, is_ellipsis=False)
        SPGraphics.text_ellipsis(self.__labelKey.label, Qt.ElideMiddle, width=221)

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__labelQR.clear()
        self.__labelKey.clear()
        self.__codeInputWidget.clear()

    def __inputs_validation(self):
        valid = False
        if self.__codeInputWidget.property('isValid'):
            valid = True

        self.__pushButtonConfirm.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__codeInputWidget.setDisabled(status)
