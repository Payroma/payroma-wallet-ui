from plibs import *
from pheader import *
from pcontroller import translator, to_qr_code
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelAddressTitle = None
        self.__labelAddressQR = None
        self.__labelDateCreated = None
        self.__labelDateCreatedValue = None
        self.__labelPrivateKey = None
        self.__labelPrivateKeyValue = None
        self.__pushButtonPrivateKey = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.WalletTab.WALLET_DETAILS)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QApplication.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelAddressTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.__labelAddressQR = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=QSize(201, 201)
        )

        self.__labelDateCreated = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__labelDateCreatedValue = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelDateCreatedValue.setWordWrap(False)
        self.__labelDateCreatedValue.setObjectName('labelDescription')

        self.__labelPrivateKey = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__labelPrivateKeyValue = qlabeladdress.QLabelAddress(
            self, fixed_height=Size.default.height(), copy_tooltip=QApplication.toolTip.copyR
        )

        self.__pushButtonPrivateKey = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonPrivateKey.setLayout(QVBoxLayout())
        self.__pushButtonPrivateKey.clicked.connect(self.private_key_clicked)

        self.layout().addWidget(self.__labelAddressTitle, 0, 0, 1, 2)
        self.layout().addWidget(self.__labelAddressQR, 1, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelDateCreated, 2, 0, 1, 1)
        self.layout().addWidget(self.__labelDateCreatedValue, 2, 1, 1, 1)
        self.layout().addWidget(self.__labelPrivateKey, 3, 0, 1, 1)
        self.layout().addWidget(self.__labelPrivateKeyValue, 3, 1, 1, 1)
        self.layout().addWidget(self.__pushButtonPrivateKey, 4, 0, 1, 2)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_less_left21))
        self.__labelPrivateKeyValue.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__labelAddressTitle.setText(translator("Scan QR Address"))
        self.__labelDateCreated.setText(translator("Date Created"))
        self.__labelPrivateKey.setText(translator("Private Key"))
        self.__pushButtonPrivateKey.setText(translator("Show Private Key"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__labelAddressTitle.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__labelDateCreated.setFont(font)
        self.__labelPrivateKey.setFont(font)
        self.__pushButtonPrivateKey.setFont(font)

        font.setBold(False)
        self.__labelDateCreatedValue.setFont(font)
        self.__labelPrivateKeyValue.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def private_key_clicked(self):
        self.__labelPrivateKey.show()
        self.__labelPrivateKeyValue.show()
        self.__pushButtonPrivateKey.hide()

    def set_data(self, address: str, created_date: str):
        pixmap = to_qr_code(address, self.__labelAddressQR.size())
        self.__labelAddressQR.setPixmap(pixmap)
        self.__labelDateCreatedValue.setText(created_date)

    def set_private_key(self, text: str):
        self.__labelPrivateKeyValue.setText(text, is_ellipsis=False)
        SPGraphics.text_ellipsis(self.__labelPrivateKeyValue.label, Qt.ElideMiddle, width=151)

    def reset(self):
        self.__labelAddressQR.clear()
        self.__labelPrivateKeyValue.clear()
        self.__labelPrivateKey.hide()
        self.__labelPrivateKeyValue.hide()
        self.__pushButtonPrivateKey.show()
