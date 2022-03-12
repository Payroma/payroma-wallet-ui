from plibs import *
from pcontroller import translator
from pui import SetupForm, images, qlabeladdress


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.labelDonate = None
        self.labelAddressDonate = None
        self.labelSplit = None
        self.pushButtonInvest = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(51)
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setObjectName('footerWidget')

        self.labelDonate = SPGraphics.QuickLabel(
            self, fixed_height=31
        )

        self.labelAddressDonate = qlabeladdress.QLabelAddress(
            self, '0x9BfDe70BF991697bCD8bAD287D2C46AaD662544d', fixed_height=31,
            copy_tooltip=QApplication.toolTip.copy
        )

        self.labelSplit = SPGraphics.QuickLabel(
            self, '|', fixed_height=31
        )

        self.pushButtonInvest = SPGraphics.QuickPushButton(
            self, fixed_height=31
        )
        self.pushButtonInvest.setObjectName('pushButtonInvest')

        self.layout().addWidget(self.labelDonate)
        self.layout().addWidget(self.labelAddressDonate)
        self.layout().addWidget(self.labelSplit)
        self.layout().addWidget(self.pushButtonInvest)

        super(UiForm, self).setup()

    def re_style(self):
        self.labelAddressDonate.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.labelDonate.setText(translator("Donate"))
        self.pushButtonInvest.setText(translator("Payroma.com"))

    def re_font(self):
        font = QFont()

        self.labelDonate.setFont(font)

        font.setUnderline(True)
        self.pushButtonInvest.setFont(font)

        font.setBold(True)
        font.setUnderline(False)
        self.labelAddressDonate.setFont(font)
