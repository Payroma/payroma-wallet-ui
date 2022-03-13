from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size


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

        self.__labelIcon = None
        self.__labelTitle = None
        self.__labelDescription = None
        self.__codeInputWidget = None
        self.__pushButtonConfirm = None
        self.__loadingEffectConfirm = None
        self.__pushButtonForgot = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(21)
        self.setObjectName(Tab.AUTHENTICATOR)

        self.__labelIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s100, pixmap=images.data.illustrations.authenticator
        )

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=31, align=Qt.AlignCenter
        )

        self.__labelDescription = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignCenter
        )
        self.__labelDescription.setObjectName('labelDescription')

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

        self.__pushButtonForgot = SPGraphics.QuickPushButton(
            self, fixed_size=QSize(301, 31), value_changed=QApplication.textColorAnimate,
            start_value=styles.data.colors.font_description, end_value=styles.data.colors.highlight
        )
        self.__pushButtonForgot.clicked.connect(self.forgot_clicked)

        self.layout().addWidget(self.__labelIcon, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__labelTitle, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__labelDescription, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__codeInputWidget, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonConfirm, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonForgot, alignment=Qt.AlignHCenter)
        self.__pushButtonConfirm.layout().addWidget(self.__loadingEffectConfirm, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_translate(self):
        self.__labelTitle.setText(translator("Authenticator"))
        self.__labelDescription.setText(
            translator("Enter a one-time passcode from\nyour authenticator app.")
        )
        self.__pushButtonConfirm.setText(translator("Confirm"))
        self.__pushButtonForgot.setText(translator("I've lost my authenticator code"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.title)
        self.__labelDescription.setFont(font)

        font.setUnderline(True)
        self.__pushButtonForgot.setFont(font)

        font.setBold(True)
        font.setUnderline(False)
        self.__pushButtonConfirm.setFont(font)

        font.setPointSize(fonts.data.size.large)
        self.__labelTitle.setFont(font)

    @pyqtSlot()
    def forgot_clicked(self):
        pass

    def otp_code_changed(self, text: str, valid: bool = False):
        self.__codeInputWidget.setProperty('isValid', valid)
        self.__inputs_validation()

    @pyqtSlot()
    def confirm_clicked(self):
        self.__all_inputs_disabled(True)
        self.__loadingEffectConfirm.start()
        self.__pushButtonConfirm.setText("")

    def confirm_completed(self):
        self.__all_inputs_disabled(False)
        self.__loadingEffectConfirm.stop()
        QTimer().singleShot(1000, self.re_translate)

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__codeInputWidget.clear()

    def __inputs_validation(self):
        valid = False
        if self.__codeInputWidget.property('isValid'):
            valid = True

        self.__pushButtonConfirm.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__codeInputWidget.setDisabled(status)
