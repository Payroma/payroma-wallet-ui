from plibs import *
from pcontroller import re_amount
from pui import SetupForm, fonts, styles, images, Size, qlabeladdress, assetsicons


class UiForm(SPGraphics.QuickListWidgetItem, SetupForm):
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILED = 'failed'

    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__labelIcon = None
        self.__labelFunctionName = None
        self.__labelPending = None
        self.__labelSuccess = None
        self.__labelFailed = None
        self.__labelAmount = None
        self.__labelAddress = None
        self.__pushButtonExplorer = None
        self.__labelDate = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(101)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(11, 11, 11, 11)
        self.layout().setHorizontalSpacing(11)
        self.layout().setVerticalSpacing(0)
        self.setGraphicsEffect(SPGraphics.QuickShadow(
            color=styles.data.colors.shadow_a40, radius=40, offset=8
        ))

        self.__labelIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41, align=Qt.AlignCenter
        )
        self.__labelIcon.setObjectName('labelIcon')

        self.__labelFunctionName = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelFunctionName.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.__labelPending = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21, tooltip=QApplication.toolTip.pending
        )
        self.__labelPending.setProperty(UiForm.PENDING, True)
        self.__labelPending.setCursor(Qt.PointingHandCursor)

        self.__labelSuccess = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21, pixmap=images.data.icons.ok41,
            tooltip=QApplication.toolTip.success
        )
        self.__labelSuccess.setProperty(UiForm.SUCCESS, True)
        self.__labelSuccess.setCursor(Qt.PointingHandCursor)

        self.__labelFailed = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21, pixmap=images.data.icons.warning41,
            tooltip=QApplication.toolTip.failed
        )
        self.__labelFailed.setProperty(UiForm.FAILED, True)
        self.__labelFailed.setCursor(Qt.PointingHandCursor)

        self.__labelAmount = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelAmount.setWordWrap(False)

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, fixed_height=21, copy_tooltip=QApplication.toolTip.copyR
        )
        self.__labelAddress.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.__pushButtonExplorer = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.viewExplorer
        )
        self.__pushButtonExplorer.clicked.connect(self.explorer_clicked)

        self.__labelDate = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.__labelDate.setObjectName('labelDescription')

        self.layout().addWidget(self.__labelIcon, 0, 0, 3, 1, Qt.AlignTop)
        self.layout().addWidget(self.__labelFunctionName, 0, 1, 1, 1)
        self.layout().addWidget(self.__labelPending, 0, 2, 1, 1, Qt.AlignLeft)
        self.layout().addWidget(self.__labelSuccess, 0, 2, 1, 1, Qt.AlignLeft)
        self.layout().addWidget(self.__labelFailed, 0, 2, 1, 1, Qt.AlignLeft)
        self.layout().addWidget(self.__labelAmount, 0, 3, 1, 1, Qt.AlignRight)
        self.layout().addWidget(self.__labelAddress, 1, 1, 1, 2)
        self.layout().addWidget(self.__pushButtonExplorer, 1, 3, 1, 1, Qt.AlignRight)
        self.layout().addWidget(self.__labelDate, 2, 1, 1, 3)

        self.item.setSizeHint(self.size())
        super(UiForm, self).setup()

    def re_style(self):
        self.__labelPending.setPixmap(images.data.icons.changeable.time21)
        self.__labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))
        self.__pushButtonExplorer.setIcon(QIcon(images.data.icons.changeable.external21))

    def re_font(self):
        font = QFont()

        self.__labelAmount.setFont(font)
        self.__labelAddress.setFont(font)
        self.__labelDate.setFont(font)

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__labelFunctionName.setFont(font)

    @pyqtSlot()
    def explorer_clicked(self):
        pass

    def set_icon(self, symbol: str):
        self.__labelIcon.setPixmap(assetsicons.get_asset_icon(symbol))

    def set_function_name(self, text: str):
        self.__labelFunctionName.setText(text)

    def set_status(self, text: str):
        for item in [self.__labelPending, self.__labelSuccess, self.__labelFailed]:
            item.setVisible(item.property(text) or False)

    def set_balance(self, text: str, symbol: str):
        self.__labelAmount.setText("{} {}".format(re_amount(text), symbol))

    def set_address(self, text: str):
        self.__labelAddress.setText(text)

    def set_date(self, text: str):
        self.__labelDate.setText(text)
