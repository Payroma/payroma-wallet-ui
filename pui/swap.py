from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelTitle = None
        self.__labelDescription = None
        self.__labelIllustration = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(21)
        self.setObjectName(Tab.SWAP)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=71, align=Qt.AlignCenter
        )

        self.__labelDescription = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignCenter
        )
        self.__labelDescription.setObjectName('labelDescription')

        self.__labelIllustration = SPGraphics.QuickLabel(
            self, fixed_size=QSize(261, 261), pixmap=images.data.illustrations.swap
        )
        self.layout().addWidget(self.__labelTitle)
        self.layout().addWidget(self.__labelDescription)
        self.layout().addWidget(self.__labelIllustration, alignment=Qt.AlignHCenter)

        super(UiForm, self).setup()

    def re_translate(self):
        self.__labelTitle.setText(translator("Payroma Swap\nComing Soon in v3"))
        self.__labelDescription.setText(translator(
            "Payroma swap allows you to exchange your coins to any other coin fastest, secure and decentralized."
        ))

    def re_font(self):
        font = QFont()

        self.__labelDescription.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setPointSize(fonts.data.size.large)
        font.setBold(True)
        self.__labelTitle.setFont(font)
