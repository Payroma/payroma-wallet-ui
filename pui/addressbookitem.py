from plibs import *
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress


class UiForm(SPGraphics.QuickListWidgetItem, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__labelIcon = None
        self.__labelUsername = None
        self.__labelAddress = None
        self.__pushButtonRemove = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(81)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignVCenter)
        self.layout().setVerticalSpacing(0)
        self.setCursor(Qt.PointingHandCursor)
        self.setGraphicsEffect(SPGraphics.QuickShadow(
            color=styles.data.colors.shadow_a40, radius=40, offset=8
        ))

        self.__labelIcon = SPGraphics.QuickLabel(
            self, fixed_size=Size.s51, pixmap=images.data.icons.wallet51, align=Qt.AlignCenter
        )

        self.__labelUsername = SPGraphics.QuickLabel(
            self, fixed_height=31
        )
        self.__labelUsername.setWordWrap(False)

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, copy_tooltip=QApplication.toolTip.copyR
        )
        self.__labelAddress.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.__pushButtonRemove = SPGraphics.QuickPushButton(
            self, icon_size=Size.s16, fixed_size=Size.s21, tooltip=QApplication.toolTip.remove
        )
        self.__pushButtonRemove.clicked.connect(self.remove_clicked)

        self.layout().addWidget(self.__labelIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.__labelUsername, 0, 1, 1, 1)
        self.layout().addWidget(self.__pushButtonRemove, 0, 2, 1, 1, Qt.AlignTop | Qt.AlignRight)
        self.layout().addWidget(self.__labelAddress, 1, 1, 1, 2)

        self.item.setSizeHint(self.size())
        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonRemove.setIcon(QIcon(images.data.icons.changeable.close21))
        self.__labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_font(self):
        font = QFont()

        self.__labelAddress.setFont(font)

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__labelUsername.setFont(font)

    @pyqtSlot()
    def remove_clicked(self):
        pass

    def get_username(self) -> str:
        return self.__labelUsername.text()

    def get_address(self) -> str:
        return self.__labelAddress.text()

    def set_username(self, text: str):
        self.__labelUsername.setText(text)

    def set_address(self, text: str):
        self.__labelAddress.setText(text)
