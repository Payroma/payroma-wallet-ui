from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelIcon = None
        self.__labelUsername = None
        self.__labelAddress = None
        self.__lineEditPassword = None
        self.__labelPasswordIcon = None
        self.__pushButtonPasswordEye = None
        self.__strengthBar = None
        self.__pushButtonLogin = None
        self.__loadingEffectLogin = None
        self.__pushButtonSkip = None
        self.__inputManager = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.LOGIN)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s100, pixmap=images.data.brands.brand
        )

        self.__labelUsername = SPGraphics.QuickLabel(
            self, fixed_height=35, align=Qt.AlignCenter
        )

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, fixed_height=21, copy_tooltip=QObject.toolTip.copyR
        )

        self.__lineEditPassword = SPGraphics.QuickLineEdit(
            self, mode=QLineEdit.Password, fixed_size=Size.defaultLineEdit, layout_support=True
        )
        self.__lineEditPassword.textChanged.connect(self.password_changed)

        self.__labelPasswordIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s21
        )

        self.__pushButtonPasswordEye = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QObject.toolTip.showR
        )

        self.__strengthBar = SPInputmanager.QStrengthBar(self)
        self.__strengthBar.setFixedSize(QSize(301, 21))

        self.__pushButtonLogin = SPGraphics.QuickPushButton(
            self, fixed_size=Size.defaultLineEdit, value_changed=QObject.mainModel.backgroundColorAnimated,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonLogin.setLayout(QVBoxLayout())
        self.__pushButtonLogin.setDisabled(True)
        self.__pushButtonLogin.clicked.connect(self.login_clicked)

        self.__loadingEffectLogin = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.__pushButtonSkip = SPGraphics.QuickPushButton(
            self, fixed_size=QSize(151, 31), value_changed=QObject.mainModel.textColorAnimated,
            start_value=styles.data.colors.disabled, end_value=styles.data.colors.highlight
        )
        self.__pushButtonSkip.clicked.connect(self.skip_clicked)

        self.layout().addWidget(self.__labelIcon, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__labelUsername, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__labelAddress, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__lineEditPassword, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__strengthBar, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonLogin, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonSkip, alignment=Qt.AlignHCenter)
        self.__lineEditPassword.layout().addWidget(self.__labelPasswordIcon, alignment=Qt.AlignLeft)
        self.__lineEditPassword.layout().addWidget(self.__pushButtonPasswordEye, alignment=Qt.AlignRight)
        self.__pushButtonLogin.layout().addWidget(self.__loadingEffectLogin, alignment=Qt.AlignCenter)

        self.__inputManager = SPInputmanager.InputManager(self.__lineEditPassword)
        self.__inputManager.eye_connect(self.__pushButtonPasswordEye)
        self.__inputManager.strength_bar_connect(self.__strengthBar)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.login)
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))
        self.__labelAddress.set_icon(QIcon(images.data.icons.changeable.copy21))
        self.__labelPasswordIcon.setPixmap(images.data.icons.changeable.key21)
        self.__pushButtonPasswordEye.setIcon(QIcon(images.data.icons.changeable.eye_visible21))

    def re_translate(self):
        self.__lineEditPassword.setPlaceholderText(translator("Password"))
        self.__pushButtonLogin.setText(translator("Login"))
        self.__pushButtonSkip.setText(translator("Skip to View"))

    def re_font(self):
        font = QFont()

        self.__labelAddress.set_font(font)
        self.__lineEditPassword.setFont(font)
        self.__strengthBar.setFontSize(fonts.data.size.small)

        font.setPointSize(fonts.data.size.title)
        font.setBold(True)
        self.__pushButtonLogin.setFont(font)
        self.__pushButtonSkip.setFont(font)

        font.setPointSize(fonts.data.size.large)
        self.__labelUsername.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def skip_clicked(self):
        pass

    @pyqtSlot(str)
    def password_changed(self, text: str, valid: bool = False):
        self.__lineEditPassword.isValid = valid
        self.__inputs_validation()

    @pyqtSlot()
    def login_clicked(self):
        self.__all_inputs_disabled(True)
        self.__loadingEffectLogin.start()
        self.__pushButtonBack.hide()
        self.__pushButtonLogin.setText("")

    def login_completed(self):
        self.__all_inputs_disabled(False)
        self.__loadingEffectLogin.stop()
        self.__pushButtonBack.show()
        QTimer().singleShot(1000, self.re_translate)

    def set_username(self, text: str):
        self.__labelUsername.setText(text)

    def set_address(self, text: str):
        self.__labelAddress.set_address(text, False)

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__labelUsername.clear()
        self.__labelAddress.label.clear()
        self.__lineEditPassword.clear()

    def __inputs_validation(self):
        valid = False
        try:
            if self.__lineEditPassword.isValid:
                valid = True
        except AttributeError:
            pass

        self.__pushButtonLogin.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__lineEditPassword.setDisabled(status)
