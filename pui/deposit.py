from plibs import *
from pheader import *
from pcontroller import translator, to_qr_code
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress


class NetworkWidget(QWidget):
    def __init__(self, parent):
        super(NetworkWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setHorizontalSpacing(11)
        self.layout().setVerticalSpacing(0)

        self.labelIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s41, pixmap=images.data.icons.warning41, align=Qt.AlignCenter
        )

        self.labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelTitle.setWordWrap(False)

        self.pushButton = SPGraphics.QuickPushButton(
            fixed_height=21, value_changed=QApplication.textColorAnimate,
            start_value=styles.data.colors.font_description, end_value=styles.data.colors.highlight
        )
        self.pushButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.layout().addWidget(self.labelIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.labelTitle, 0, 1, 1, 1)
        self.layout().addWidget(self.pushButton, 1, 1, 1, 1)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelQRDescription = None
        self.__labelAddressQR = None
        self.__labelAddressDescription = None
        self.__labelAddress = None
        self.__lineWidget = None
        self.__networkWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.DEPOSIT)

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
            self, copy_tooltip=QApplication.toolTip.copyR
        )
        self.__labelAddress.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.__lineWidget = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget.setObjectName('lineWidget')

        self.__networkWidget = NetworkWidget(self)
        self.__networkWidget.pushButton.clicked.connect(self.network_clicked)

        self.layout().addWidget(self.__labelQRDescription)
        self.layout().addWidget(self.__labelAddressQR, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__labelAddressDescription)
        self.layout().addWidget(self.__labelAddress)
        self.layout().addWidget(self.__lineWidget)
        self.layout().addWidget(self.__networkWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.__labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__labelQRDescription.setText(translator(
            "Scan the code on the withdrawal page of the trading platform APP or wallet APP"
        ))
        self.__labelAddressDescription.setText(translator("or Copy your deposit address"))
        self.__networkWidget.labelTitle.setText(translator("Ensure the sender network is"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.title)
        self.__labelQRDescription.setFont(font)
        self.__labelAddressDescription.setFont(font)

        font.setBold(True)
        self.__networkWidget.labelTitle.setFont(font)

        font.setBold(False)
        font.setUnderline(True)
        self.__networkWidget.pushButton.setFont(font)

    @pyqtSlot()
    def network_clicked(self):
        pass

    def set_data(self, address: str, network_name: str):
        pixmap = to_qr_code(address, self.__labelAddressQR.size())
        self.__labelAddressQR.setPixmap(pixmap)
        self.__labelAddress.setText(address, False)
        self.__networkWidget.pushButton.setText(network_name)

    def reset(self):
        self.__labelAddressQR.clear()
        self.__labelAddress.clear()
        self.__networkWidget.pushButton.setText("")
