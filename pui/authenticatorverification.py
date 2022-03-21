from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress, validator


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelIllustration = None
        self.__labelTitle = None
        self.__labelDescription = None
        self.__labelUsername = None
        self.__labelAddress = None
        self.__lineEditPINCode = None
        self.__labelPINCodeIcon = None
        self.__pushButtonPINCodeEye = None
        self.__labelPINCodeAlert = None
        self.__pushButtonVerify = None
        self.__loadingEffectVerify = None
        self.__inputManager = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setHorizontalSpacing(21)
        self.layout().setVerticalSpacing(11)
        self.setObjectName(Tab.AuthenticatorSetupTab.VERIFICATION)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QApplication.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelIllustration = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=QSize(151, 151),
            pixmap=images.data.illustrations.verify, align=Qt.AlignHCenter
        )

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__labelDescription = SPGraphics.QuickLabel(
            self, fixed_height=31
        )
        self.__labelDescription.setObjectName('labelDescription')

        self.__labelUsername = SPGraphics.QuickLabel(
            self, fixed_height=31, align=Qt.AlignCenter
        )
        self.__labelUsername.setWordWrap(False)

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, fixed_height=21, copy_tooltip=QApplication.toolTip.copyR
        )
        self.__labelAddress.hide()

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

        self.layout().addWidget(self.__labelIllustration, 0, 0, 2, 1)
        self.layout().addWidget(self.__labelTitle, 0, 1, 1, 1, Qt.AlignBottom)
        self.layout().addWidget(self.__labelDescription, 1, 1, 1, 1, Qt.AlignTop)
        self.layout().addWidget(self.__labelUsername, 2, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelAddress, 3, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__lineEditPINCode, 4, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonVerify, 5, 0, 1, 2, Qt.AlignHCenter)
        self.__lineEditPINCode.layout().addWidget(self.__labelPINCodeIcon, alignment=Qt.AlignLeft)
        self.__lineEditPINCode.layout().addWidget(self.__labelPINCodeAlert, alignment=Qt.AlignRight)
        self.__lineEditPINCode.layout().addWidget(self.__pushButtonPINCodeEye)
        self.__pushButtonVerify.layout().addWidget(self.__loadingEffectVerify, alignment=Qt.AlignCenter)

        self.__inputManager = SPInputmanager.InputManager(self.__lineEditPINCode)
        self.__inputManager.eye_connect(self.__pushButtonPINCodeEye)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_less_left21))
        self.__labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))
        self.__labelPINCodeIcon.setPixmap(images.data.icons.changeable.pin_code21)
        self.__pushButtonPINCodeEye.setIcon(QIcon(images.data.icons.changeable.eye_visible21))

    def re_translate(self):
        self.__labelTitle.setText(translator("Wallet Verification"))
        self.__labelDescription.setText(translator("Confirm your wallet's PIN code\nto generate your key."))
        self.__lineEditPINCode.setPlaceholderText(translator("PIN Code 6 numbers"))
        self.__pushButtonVerify.setText(translator("Verify"))

    def re_font(self):
        font = QFont()

        self.__labelDescription.setFont(font)
        self.__labelAddress.setFont(font)
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

    def set_data(self, username: str, address: str = ''):
        self.__labelUsername.setText(username)
        if address:
            self.__labelAddress.setText(address, is_ellipsis=False)
            self.__labelAddress.show()
        else:
            self.__labelAddress.hide()

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__labelUsername.clear()
        self.__labelAddress.clear()
        self.__lineEditPINCode.clear()

    def __inputs_validation(self):
        valid = False
        if self.__lineEditPINCode.property('isValid'):
            valid = True

        self.__pushButtonVerify.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__lineEditPINCode.setDisabled(status)
