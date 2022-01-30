from plibs import *
from pheader import *
from pui import SetupForm, fonts, images, Size


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.labelBrandIcon = None
        self.labelBrandName = None
        self.labelSoftwareVersion = None
        self.pushButtonSettings = None
        self.pushButtonExit = None

        self.__leftClickPressed = None
        self.__clickPressedX = None
        self.__clickPressedY = None

    def mousePressEvent(self, event):
        super(UiForm, self).mousePressEvent(event)

        is_maximized = self.nativeParentWidget().isMaximized()

        if event.button() == Qt.LeftButton and self.underMouse() and not is_maximized:
            margin = self.nativeParentWidget().layout().contentsRect()
            self.__clickPressedX = event.pos().x() + margin.x()
            self.__clickPressedY = event.pos().y() + margin.y()
            self.__leftClickPressed = True

    def mouseReleaseEvent(self, event):
        super(UiForm, self).mouseReleaseEvent(event)

        self.__leftClickPressed = False

    def mouseMoveEvent(self, event):
        super(UiForm, self).mouseMoveEvent(event)

        if self.__leftClickPressed:
            x = event.globalPos().x() - self.__clickPressedX
            y = event.globalPos().y() - self.__clickPressedY
            self.nativeParentWidget().move(x, y)

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(81)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignVCenter)
        self.layout().setContentsMargins(15, 0, 15, 0)
        self.layout().setVerticalSpacing(0)
        self.setObjectName('headerWidget')

        self.labelBrandIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s41,
            pixmap=images.data.brands.brand, align=Qt.AlignCenter
        )

        self.labelBrandName = SPGraphics.QuickLabel(
            self, text=SOFTWARE_NAME
        )
        self.labelBrandName.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))

        self.labelSoftwareVersion = SPGraphics.QuickLabel(
            self, text=VERSION
        )
        self.labelSoftwareVersion.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))

        self.pushButtonSettings = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.settings
        )

        self.pushButtonExit = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.exit
        )

        self.layout().addWidget(self.labelBrandIcon, 0, 0, 2, 1)
        self.layout().addWidget(self.labelBrandName, 0, 1, 1, 1)
        self.layout().addWidget(self.labelSoftwareVersion, 1, 1, 1, 1)
        self.layout().addWidget(self.pushButtonSettings, 0, 2, 2, 1, Qt.AlignRight)
        self.layout().addWidget(self.pushButtonExit, 0, 3, 2, 1)

        super(UiForm, self).setup()

    def re_style(self):
        self.pushButtonSettings.setIcon(QIcon(images.data.icons.changeable.settings21))
        self.pushButtonExit.setIcon(QIcon(images.data.icons.changeable.close21))

    def re_font(self):
        font = QFont(fonts.data.family.brand, fonts.data.size.small)

        self.labelSoftwareVersion.setFont(font)

        font.setPointSize(fonts.data.size.brand)
        font.setBold(True)
        self.labelBrandName.setFont(font)
