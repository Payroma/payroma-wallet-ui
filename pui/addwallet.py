from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, validator


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelTitle = None
        self.__lineEditUsername = None
        self.__labelUsernameIcon = None
        self.__labelUsernameAlert = None
        self.__labelUsernameInfo = None
        self.__lineEditPassword = None
        self.__labelPasswordIcon = None
        self.__pushButtonPasswordEye = None
        self.__labelPasswordAlert = None
        self.__strengthBar = None
        self.__lineEditConfirmPassword = None
        self.__labelConfirmPasswordIcon = None
        self.__pushButtonConfirmPasswordEye = None
        self.__labelConfirmPasswordAlert = None
        self.__lineEditPINCode = None
        self.__labelPINCodeIcon = None
        self.__pushButtonPINCodeEye = None
        self.__labelPINCodeInfo = None
        self.__labelPINCodeAlert = None
        self.__lineWidget = None
        self.__pushButtonAdd = None
        self.__loadingEffectAdd = None
        self.__inputManager = None
        self.__inputManagerConfirm = None
        self.__inputManagerPINCode = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.ADD_WALLET)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=71, align=Qt.AlignHCenter
        )

        self.__lineEditUsername = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=30
        )
        self.__lineEditUsername.setProperty("iconable", True)
        self.__lineEditUsername.setProperty("iconableRight", True)
        self.__lineEditUsername.setValidator(validator.username)
        self.__lineEditUsername.textChanged.connect(self.username_changed)

        self.__labelUsernameIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.__labelUsernameInfo = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21, tooltip=QApplication.toolTip.usernameInfoR
        )
        self.__labelUsernameInfo.setCursor(Qt.PointingHandCursor)

        self.__labelUsernameAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QApplication.toolTip.usernameAlert
        )
        self.__labelUsernameAlert.setCursor(Qt.PointingHandCursor)
        self.__labelUsernameAlert.hide()

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

        self.__labelPasswordAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QApplication.toolTip.passwordAlert
        )
        self.__labelPasswordAlert.setCursor(Qt.PointingHandCursor)
        self.__labelPasswordAlert.hide()

        self.__strengthBar = SPInputmanager.QStrengthBar(self)
        self.__strengthBar.setFixedSize(QSize(301, 21))

        self.__lineEditConfirmPassword = SPGraphics.QuickLineEdit(
            self, mode=QLineEdit.Password, fixed_size=Size.default, layout_support=True
        )
        self.__lineEditConfirmPassword.setProperty("iconable", True)
        self.__lineEditConfirmPassword.setProperty("iconableRight", True)
        self.__lineEditConfirmPassword.textChanged.connect(self.confirm_password_changed)

        self.__labelConfirmPasswordIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.__pushButtonConfirmPasswordEye = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.showR
        )

        self.__labelConfirmPasswordAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QApplication.toolTip.passwordConfirmAlert
        )
        self.__labelConfirmPasswordAlert.setCursor(Qt.PointingHandCursor)
        self.__labelConfirmPasswordAlert.hide()

        self.__lineEditPINCode = SPGraphics.QuickLineEdit(
            self, mode=QLineEdit.Password, fixed_size=Size.default, layout_support=True, length=6
        )
        self.__lineEditPINCode.setProperty("iconable", True)
        self.__lineEditPINCode.setProperty("iconableRight", True)
        self.__lineEditPINCode.setValidator(validator.number)
        self.__lineEditPINCode.textChanged.connect(self.pin_code_changed)

        self.__labelPINCodeIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.__pushButtonPINCodeEye = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.showR
        )

        self.__labelPINCodeInfo = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21, tooltip=QApplication.toolTip.pinCodeInfoR
        )
        self.__labelPINCodeInfo.setCursor(Qt.PointingHandCursor)

        self.__labelPINCodeAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QApplication.toolTip.pinCodeAlert
        )
        self.__labelPINCodeAlert.setCursor(Qt.PointingHandCursor)
        self.__labelPINCodeAlert.hide()

        self.__lineWidget = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget.setObjectName('lineWidget')

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
        self.layout().addWidget(self.__lineEditUsername)
        self.layout().addWidget(self.__lineEditPassword)
        self.layout().addWidget(self.__strengthBar)
        self.layout().addWidget(self.__lineEditConfirmPassword)
        self.layout().addWidget(self.__lineEditPINCode)
        self.layout().addWidget(self.__lineWidget)
        self.layout().addWidget(self.__pushButtonAdd)
        self.__lineEditUsername.layout().addWidget(self.__labelUsernameIcon, alignment=Qt.AlignLeft)
        self.__lineEditUsername.layout().addWidget(self.__labelUsernameAlert, alignment=Qt.AlignRight)
        self.__lineEditUsername.layout().addWidget(self.__labelUsernameInfo)
        self.__lineEditPassword.layout().addWidget(self.__labelPasswordIcon, alignment=Qt.AlignLeft)
        self.__lineEditPassword.layout().addWidget(self.__labelPasswordAlert, alignment=Qt.AlignRight)
        self.__lineEditPassword.layout().addWidget(self.__pushButtonPasswordEye)
        self.__lineEditConfirmPassword.layout().addWidget(self.__labelConfirmPasswordIcon, alignment=Qt.AlignLeft)
        self.__lineEditConfirmPassword.layout().addWidget(self.__labelConfirmPasswordAlert, alignment=Qt.AlignRight)
        self.__lineEditConfirmPassword.layout().addWidget(self.__pushButtonConfirmPasswordEye)
        self.__lineEditPINCode.layout().addWidget(self.__labelPINCodeIcon, alignment=Qt.AlignLeft)
        self.__lineEditPINCode.layout().addWidget(self.__labelPINCodeAlert, alignment=Qt.AlignRight)
        self.__lineEditPINCode.layout().addWidget(self.__pushButtonPINCodeEye)
        self.__lineEditPINCode.layout().addWidget(self.__labelPINCodeInfo)
        self.__pushButtonAdd.layout().addWidget(self.__loadingEffectAdd, alignment=Qt.AlignCenter)

        self.__inputManager = SPInputmanager.InputManager(self.__lineEditPassword)
        self.__inputManager.eye_connect(self.__pushButtonPasswordEye)
        self.__inputManager.strength_bar_connect(self.__strengthBar)

        self.__inputManagerConfirm = SPInputmanager.InputManager(self.__lineEditConfirmPassword)
        self.__inputManagerConfirm.eye_connect(self.__pushButtonConfirmPasswordEye)

        self.__inputManagerPINCode = SPInputmanager.InputManager(self.__lineEditPINCode)
        self.__inputManagerPINCode.eye_connect(self.__pushButtonPINCodeEye)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.addwallet)
        self.__labelUsernameIcon.setPixmap(images.data.icons.changeable.username21)
        self.__labelUsernameInfo.setPixmap(images.data.icons.changeable.info21)
        self.__labelPasswordIcon.setPixmap(images.data.icons.changeable.key21)
        self.__pushButtonPasswordEye.setIcon(QIcon(images.data.icons.changeable.eye_visible21))
        self.__labelConfirmPasswordIcon.setPixmap(images.data.icons.changeable.key21)
        self.__pushButtonConfirmPasswordEye.setIcon(QIcon(images.data.icons.changeable.eye_visible21))
        self.__labelPINCodeIcon.setPixmap(images.data.icons.changeable.pin_code21)
        self.__pushButtonPINCodeEye.setIcon(QIcon(images.data.icons.changeable.eye_visible21))
        self.__labelPINCodeInfo.setPixmap(images.data.icons.changeable.info21)

    def re_translate(self):
        self.__labelTitle.setText(translator(
            "Create a new or add an existing wallet, "
            "whatever, your private key and password are not stored anywhere."
        ))
        self.__lineEditUsername.setPlaceholderText(translator("Username/Email/Phone"))
        self.__lineEditPassword.setPlaceholderText(translator("Password"))
        self.__lineEditConfirmPassword.setPlaceholderText(translator("Confirm password"))
        self.__lineEditPINCode.setPlaceholderText(translator("PIN Code 6 numbers"))
        self.__pushButtonAdd.setText(translator("Add Wallet"))

    def re_font(self):
        font = QFont()

        self.__strengthBar.setFontSize(fonts.data.size.small)

        self.__lineEditUsername.setFont(font)
        self.__lineEditPassword.setFont(font)
        self.__lineEditConfirmPassword.setFont(font)
        self.__lineEditPINCode.setFont(font)

        font.setPointSize(fonts.data.size.title)
        font.setBold(True)
        self.__pushButtonAdd.setFont(font)
        self.__labelTitle.setFont(font)

    @pyqtSlot(str)
    def username_changed(self, text: str, valid: bool = False):
        self.__lineEditUsername.setProperty('isValid', valid)
        self.__labelUsernameAlert.setHidden(valid or not text)
        self.__polish(self.__lineEditUsername)
        self.__inputs_validation()

    @pyqtSlot(str)
    def password_changed(self, text: str, valid: bool = False):
        self.__lineEditPassword.setProperty('isValid', valid)
        self.__labelPasswordAlert.setHidden(valid or not text)
        self.__polish(self.__lineEditPassword)
        self.__inputs_validation()

    @pyqtSlot(str)
    def confirm_password_changed(self, text: str, valid: bool = False):
        self.__lineEditConfirmPassword.setProperty('isValid', valid)
        self.__labelConfirmPasswordAlert.setHidden(valid or not text)
        self.__polish(self.__lineEditConfirmPassword)
        self.__inputs_validation()

    @pyqtSlot(str)
    def pin_code_changed(self, text: str, valid: bool = False):
        self.__lineEditPINCode.setProperty('isValid', valid)
        self.__labelPINCodeAlert.setHidden(valid or not text)
        self.__inputs_validation()

    @pyqtSlot()
    def add_clicked(self):
        self.__all_inputs_disabled(True)
        self.__loadingEffectAdd.start()
        self.__pushButtonAdd.setText("")

    def add_completed(self):
        self.__all_inputs_disabled(False)
        self.__loadingEffectAdd.stop()
        QTimer().singleShot(1000, self.re_translate)

    def get_strength_state(self) -> str:
        return self.__strengthBar.state().text

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__lineEditUsername.clear()
        self.__lineEditPassword.clear()
        self.__lineEditConfirmPassword.clear()
        self.__lineEditPINCode.clear()

    def __inputs_validation(self):
        valid = False
        if (
            self.__lineEditUsername.property('isValid') and
            self.__lineEditPassword.property('isValid') and
            self.__lineEditConfirmPassword.property('isValid') and
            self.__lineEditPINCode.property('isValid')
        ):
            valid = True

        self.__pushButtonAdd.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__lineEditUsername.setDisabled(status)
        self.__lineEditPassword.setDisabled(status)
        self.__lineEditConfirmPassword.setDisabled(status)
        self.__lineEditPINCode.setDisabled(status)

    @staticmethod
    def __polish(widget: QLineEdit):
        widget.style().unpolish(widget)
        widget.style().polish(widget)
