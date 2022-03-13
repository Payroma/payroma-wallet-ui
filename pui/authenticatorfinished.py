from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelIllustration = None
        self.__labelTitle = None
        self.__labelDescription = None
        self.__labelKey = None
        self.__pushButtonDone = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(21, 0, 21, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.AuthenticatorSetupTab.FINISHED)

        self.__labelIllustration = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=QSize(151, 151),
            pixmap=images.data.illustrations.done, align=Qt.AlignHCenter
        )

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=61
        )

        self.__labelDescription = SPGraphics.QuickLabel(
            self, fixed_height=81, align=Qt.AlignCenter
        )

        self.__labelKey = qlabeladdress.QLabelAddress(
            self, fixed_height=31, copy_tooltip=QApplication.toolTip.copyR
        )

        self.__pushButtonDone = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonDone.clicked.connect(self.done_clicked)

        self.layout().addWidget(self.__labelIllustration, 0, 0, 1, 1)
        self.layout().addWidget(self.__labelTitle, 0, 1, 1, 1)
        self.layout().addWidget(self.__labelDescription, 1, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelKey, 2, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonDone, 3, 0, 1, 2, Qt.AlignHCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.__labelKey.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__labelTitle.setText(translator("Congratulations we're done!"))
        self.__labelDescription.setText(translator(
            "Please save this key on paper, This key will allow you to recover your "
            "authenticator app in case of phone loss or repeat the same previous steps to recover again."
        ))
        self.__pushButtonDone.setText(translator("Done"))

    def re_font(self):
        font = QFont()

        self.__labelDescription.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__labelKey.setFont(font)

        font.setBold(True)
        self.__pushButtonDone.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setPointSize(fonts.data.size.large)
        font.setBold(False)
        self.__labelTitle.setFont(font)

    @pyqtSlot()
    def done_clicked(self):
        pass

    def set_data(self, text: str):
        self.__labelKey.setText(text, is_ellipsis=False)
        SPGraphics.text_ellipsis(self.__labelKey.label, Qt.ElideMiddle, width=221)

    def reset(self):
        self.__labelKey.clear()
