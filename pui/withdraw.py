from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, Size


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelTitle = None
        self.__lineEditSearch = None
        self.__labelAddressIcon = None
        self.__labelAddressValid = None
        self.__labelAddressAlert = None
        self.__tabWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(11, 11, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.WITHDRAW)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.__lineEditSearch = SPGraphics.QuickLineEdit(
            self, fixed_size=QSize(351, 51), layout_support=True, length=42
        )
        self.__lineEditSearch.setFocusPolicy(Qt.ClickFocus)
        self.__lineEditSearch.setProperty("iconable", True)
        self.__lineEditSearch.textChanged.connect(self.address_changed)

        self.__labelAddressIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21
        )

        self.__labelAddressValid = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21,
            pixmap=images.data.icons.ok41, tooltip=QObject.toolTip.addressValidB
        )
        self.__labelAddressValid.setCursor(Qt.PointingHandCursor)
        self.__labelAddressValid.hide()

        self.__labelAddressAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QObject.toolTip.addressAlert
        )
        self.__labelAddressAlert.setCursor(Qt.PointingHandCursor)
        self.__labelAddressAlert.hide()

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.__pushButtonBack.raise_()

        self.layout().addWidget(self.__labelTitle)
        self.layout().addWidget(self.__lineEditSearch, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__tabWidget)
        self.__lineEditSearch.layout().addWidget(self.__labelAddressIcon, alignment=Qt.AlignLeft)
        self.__lineEditSearch.layout().addWidget(self.__labelAddressValid, alignment=Qt.AlignLeft)
        self.__lineEditSearch.layout().addWidget(self.__labelAddressAlert, alignment=Qt.AlignRight)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))
        self.__labelAddressIcon.setPixmap(images.data.icons.changeable.search21)

    def re_translate(self):
        self.__labelTitle.setText(translator("Send to"))
        self.__lineEditSearch.setPlaceholderText(translator("Search, Public Address (0x)"))

    def re_font(self):
        font = QFont()

        self.__lineEditSearch.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        font.setBold(True)
        self.__labelTitle.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot(str)
    def address_changed(self, text: str, valid: bool = False):
        self.__lineEditSearch.setProperty('isValid', valid)
        self.__labelAddressAlert.setHidden(valid)
        self.__polish(self.__lineEditSearch)
        self.__inputs_validation()

    @pyqtSlot()
    def __tab_changed(self):
        widget = self.__tabWidget.currentWidget()
        self.__tabTransMotion = SPGraphics.GeometryMotion(widget)
        self.__tabTransMotion.temp_x(start_x=widget.width(), end_x=0, duration=500).start()

    def add_tab(self, model: QObject, name: str):
        self.__tabWidget.addTab(model, name)

    def set_address(self, text: str):
        self.__lineEditSearch.setText(text)

    def reset(self):
        self.__lineEditSearch.clear()
        self.__tabWidget.setCurrentIndex(0)

    def __inputs_validation(self):
        valid = False
        if self.__lineEditSearch.property('isValid'):
            valid = True

        if valid:
            self.__lineEditSearch.setReadOnly(True)
            self.__labelAddressIcon.hide()
            self.__labelAddressValid.show()
            self.__tabWidget.setCurrentIndex(1)
        else:
            self.__lineEditSearch.setReadOnly(False)
            self.__labelAddressIcon.show()
            self.__labelAddressValid.hide()
            self.__tabWidget.setCurrentIndex(0)

    @staticmethod
    def __polish(widget: QLineEdit):
        widget.style().unpolish(widget)
        widget.style().polish(widget)