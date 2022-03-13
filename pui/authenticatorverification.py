from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress, validator


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelTitle = None
        self.__labelDescription = None
        self.__labelUsername = None
        self.__labelAddress = None
        self.__lineEditPassword = None
        self.__labelPasswordIcon = None
        self.__pushButtonPasswordEye = None
        self.__lineEditPINCode = None
        self.__labelPINCodeIcon = None
        self.__pushButtonPINCodeEye = None
        self.__labelPINCodeAlert = None
        self.__pushButtonVerify = None
        self.__loadingEffectVerify = None
        self.__inputManager = None
        self.__inputManagerPINCode = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.AuthenticatorSetupTab.VERIFICATION)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.__labelDescription = SPGraphics.QuickLabel(
            self, fixed_height=31, align=Qt.AlignTop | Qt.AlignHCenter
        )
        self.__labelDescription.setObjectName('labelDescription')

        self.__labelUsername = SPGraphics.QuickLabel(
            self, fixed_height=31, align=Qt.AlignCenter
        )

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, fixed_height=21, copy_tooltip=QApplication.toolTip.copyR
        )

        self.__lineEditPassword = SPGraphics.QuickLineEdit(
            self, mode=QLineEdit.Password, fixed_size=Size.default, layout_support=True
        )
        self.__lineEditPassword.setProperty("iconable", True)
        self.__lineEditPassword.setProperty("iconableRight", True)
        self.__lineEditPassword.textChanged.connect(self.password_changed)

        self.__labelPasswordIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.__pushButtonPasswordEye = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.showR
        )

        self.__lineEditPINCode = SPGraphics.QuickLineEdit(
            self, mode=QLineEdit.Password, fixed_size=Size.default, layout_support=True, length=6
        )
        self.__lineEditPINCode.setProperty("iconable", True)
        self.__lineEditPINCode.setValidator(validator.number)
        self.__lineEditPINCode.textChanged.connect(self.pin_code_changed)

        self.__labelPINCodeIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.__pushButtonPINCodeEye = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.showR
        )

        self.__labelPINCodeAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QApplication.toolTip.pinCodeAlert
        )
        self.__labelPINCodeAlert.setCursor(Qt.PointingHandCursor)
        self.__labelPINCodeAlert.hide()

        self.__pushButtonVerify = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonVerify.setLayout(QVBoxLayout())
        self.__pushButtonVerify.setDisabled(True)
        self.__pushButtonVerify.clicked.connect(self.verify_clicked)

        self.__loadingEffectVerify = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.layout().addWidget(self.__labelTitle, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__labelDescription, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__labelUsername, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__labelAddress, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__lineEditPassword, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__lineEditPINCode, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonVerify, alignment=Qt.AlignHCenter)
        self.__lineEditPassword.layout().addWidget(self.__labelPasswordIcon, alignment=Qt.AlignLeft)
        self.__lineEditPassword.layout().addWidget(self.__pushButtonPasswordEye, alignment=Qt.AlignRight)
        self.__lineEditPINCode.layout().addWidget(self.__labelPINCodeIcon, alignment=Qt.AlignLeft)
        self.__lineEditPINCode.layout().addWidget(self.__labelPINCodeAlert, alignment=Qt.AlignRight)
        self.__lineEditPINCode.layout().addWidget(self.__pushButtonPINCodeEye)
        self.__pushButtonVerify.layout().addWidget(self.__loadingEffectVerify, alignment=Qt.AlignCenter)

        self.__inputManager = SPInputmanager.InputManager(self.__lineEditPassword)
        self.__inputManager.eye_connect(self.__pushButtonPasswordEye)

        self.__inputManagerPINCode = SPInputmanager.InputManager(self.__lineEditPINCode)
        self.__inputManagerPINCode.eye_connect(self.__pushButtonPINCodeEye)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_less_left21))
        self.__labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))
        self.__labelPasswordIcon.setPixmap(images.data.icons.changeable.key21)
        self.__pushButtonPasswordEye.setIcon(QIcon(images.data.icons.changeable.eye_visible21))
        self.__labelPINCodeIcon.setPixmap(images.data.icons.changeable.pin_code21)
        self.__pushButtonPINCodeEye.setIcon(QIcon(images.data.icons.changeable.eye_visible21))

    def re_translate(self):
        self.__labelTitle.setText(translator("Wallet Verification"))
        self.__labelDescription.setText(translator(
            "Confirm your wallet password and PIN code to generate your key."
        ))
        self.__lineEditPassword.setPlaceholderText(translator("Password"))
        self.__lineEditPINCode.setPlaceholderText(translator("PIN Code 6 numbers"))
        self.__pushButtonVerify.setText(translator("Verify"))

    def re_font(self):
        font = QFont()

        self.__labelDescription.setFont(font)
        self.__labelAddress.setFont(font)
        self.__lineEditPassword.setFont(font)
        self.__lineEditPINCode.setFont(font)

        font.setPointSize(fonts.data.size.title)
        font.setBold(True)
        self.__pushButtonVerify.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelTitle.setFont(font)
        self.__labelUsername.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot(str)
    def password_changed(self, text: str, valid: bool = False):
        self.__lineEditPassword.setProperty('isValid', valid)
        self.__inputs_validation()

    @pyqtSlot(str)
    def pin_code_changed(self, text: str, valid: bool = False):
        self.__lineEditPINCode.setProperty('isValid', valid)
        self.__labelPINCodeAlert.setHidden(valid or not text)
        self.__inputs_validation()

    @pyqtSlot()
    def verify_clicked(self):
        self.__all_inputs_disabled(True)
        self.__loadingEffectVerify.start()
        self.__pushButtonBack.hide()
        self.__pushButtonVerify.setText("")

    def verify_completed(self):
        self.__all_inputs_disabled(False)
        self.__loadingEffectVerify.stop()
        self.__pushButtonBack.show()
        QTimer().singleShot(1000, self.re_translate)

    def set_data(self, username: str, address: str, password: str = '', pin_code: str = ''):
        self.__labelUsername.setText(username)
        self.__labelAddress.setText(address, is_ellipsis=False)
        self.__lineEditPassword.setText(password)
        self.__lineEditPINCode.setText(pin_code)

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__labelUsername.clear()
        self.__labelAddress.clear()
        self.__lineEditPassword.clear()
        self.__lineEditPINCode.clear()

    def __inputs_validation(self):
        valid = False
        if (
            self.__lineEditPassword.property('isValid') and
            self.__lineEditPINCode.property('isValid')
        ):
            valid = True

        self.__pushButtonVerify.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__lineEditPassword.setDisabled(status)
        self.__lineEditPINCode.setDisabled(status)
