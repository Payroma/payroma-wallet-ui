from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelAddressTitle = None
        self.__labelAddressQR = None
        self.__labelDateCreatedTitle = None
        self.__labelDateCreated = None
        self.__labelPrivateKey = None
        self.__pushButtonPrivateKey = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.WalletTab.WALLET_DETAILS)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelAddressTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.__labelAddressQR = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=QSize(201, 201)
        )

        self.__labelDateCreatedTitle = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__labelDateCreated = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelDateCreated.setWordWrap(False)
        self.__labelDateCreated.setObjectName('labelDescription')

        self.__labelPrivateKey = qlabeladdress.QLabelAddress(
            self, fixed_size=Size.default, copy_tooltip=QObject.toolTip.copyR
        )

        self.__pushButtonPrivateKey = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QObject.mainModel.backgroundColorAnimated,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonPrivateKey.setLayout(QVBoxLayout())
        self.__pushButtonPrivateKey.clicked.connect(self.private_key_clicked)

        self.layout().addWidget(self.__labelAddressTitle, 0, 0, 1, 2)
        self.layout().addWidget(self.__labelAddressQR, 1, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelDateCreatedTitle, 2, 0, 1, 1)
        self.layout().addWidget(self.__labelDateCreated, 2, 1, 1, 1)
        self.layout().addWidget(self.__labelPrivateKey, 3, 0, 1, 2)
        self.layout().addWidget(self.__pushButtonPrivateKey, 4, 0, 1, 2)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_less_left21))
        self.__labelPrivateKey.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__labelAddressTitle.setText(translator("QR Address"))
        self.__labelDateCreatedTitle.setText(translator("Date Created:"))
        self.__pushButtonPrivateKey.setText(translator("Show Private Key"))

    def re_font(self):
        font = QFont()

        self.__labelPrivateKey.setFont(font)

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__labelAddressTitle.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__labelDateCreatedTitle.setFont(font)
        self.__pushButtonPrivateKey.setFont(font)

        font.setBold(False)
        self.__labelDateCreated.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def private_key_clicked(self):
        self.__labelPrivateKey.show()
        self.__pushButtonPrivateKey.hide()

    def set_address(self, text: str):
        image_file = io.BytesIO()

        qr_generator = pyqrcode.create(text, error='L', version=3, mode='binary')
        qr_generator.png(
            image_file, scale=7, module_color=styles.data.colors.font.getRgb(),
            background=styles.data.colors.background.getRgb()
        )

        image = QImage.fromData(image_file.getvalue(), 'png')

        self.__labelAddressQR.setPixmap(QPixmap.fromImage(image))

    def set_date_created(self, text: str):
        self.__labelDateCreated.setText(text)

    def set_private_key(self, text: str):
        self.__labelPrivateKey.setText(text, is_ellipsis=False)
        SPGraphics.text_ellipsis(self.__labelPrivateKey.label, Qt.ElideMiddle, width=271)

    def reset(self):
        self.__labelAddressQR.clear()
        self.__labelPrivateKey.clear()
        self.__labelPrivateKey.hide()
        self.__pushButtonPrivateKey.show()
