from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelQRDescription = None
        self.__labelAddressQR = None
        self.__labelAddressDescription = None
        self.__labelAddress = None
        self.__labelNoteIcon = None
        self.__labelNote = None
        self.__lineWidget = None
        self.__labelNetwork = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.DEPOSIT)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelQRDescription = SPGraphics.QuickLabel(
            self, fixed_height=51, align=Qt.AlignCenter
        )

        self.__labelAddressQR = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=QSize(201, 201)
        )

        self.__labelAddressDescription = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, copy_tooltip=QObject.toolTip.copyR
        )
        self.__labelAddress.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.__lineWidget = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget.setObjectName('lineWidget')

        self.__labelNoteIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s41, pixmap=images.data.icons.warning41, align=Qt.AlignCenter
        )

        self.__labelNote = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignTop
        )
        self.__labelNote.setWordWrap(False)

        self.__labelNetwork = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignBottom
        )
        self.__labelNetwork.setWordWrap(False)

        self.layout().addWidget(self.__labelQRDescription, 0, 0, 1, 2)
        self.layout().addWidget(self.__labelAddressQR, 1, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelAddressDescription, 2, 0, 1, 2)
        self.layout().addWidget(self.__labelAddress, 3, 0, 1, 2)
        self.layout().addWidget(self.__lineWidget, 4, 0, 1, 2)
        self.layout().addWidget(self.__labelNoteIcon, 5, 0, 1, 1)
        self.layout().addWidget(self.__labelNote, 5, 1, 1, 1)
        self.layout().addWidget(self.__labelNetwork, 5, 1, 1, 1)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_less_left21))
        self.__labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__labelQRDescription.setText(translator(
            "Scan the code on the withdrawal page of the trading platform APP or wallet APP"
        ))
        self.__labelAddressDescription.setText(translator("or Copy your deposit address"))
        self.__labelNote.setText(translator("Ensure the sender network is"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.title)
        self.__labelQRDescription.setFont(font)
        self.__labelAddressDescription.setFont(font)

        font.setBold(True)
        self.__labelNote.setFont(font)

        font.setBold(False)
        font.setUnderline(True)
        self.__labelNetwork.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    def set_address(self, text: str):
        image_file = io.BytesIO()

        qr_generator = pyqrcode.create(text, error='L', mode='binary')
        qr_generator.png(
            image_file, scale=7, module_color=styles.data.colors.font.getRgb(),
            background=styles.data.colors.background.getRgb()
        )

        image = QImage.fromData(image_file.getvalue(), 'png').scaled(
            self.__labelAddressQR.size(), Qt.KeepAspectRatio
        )

        self.__labelAddressQR.setPixmap(QPixmap.fromImage(image))
        self.__labelAddress.setText(text, False)

    def set_network_name(self, text: str):
        self.__labelNetwork.setText(text)

    def reset(self):
        self.__labelAddressQR.clear()
        self.__labelAddress.clear()
        self.__labelNetwork.clear()
