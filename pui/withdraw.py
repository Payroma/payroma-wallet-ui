from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(11, 11, 11, 11)
        self.layout().setSpacing(11)

        self.labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.lineEditAddress = SPGraphics.QuickLineEdit(
            self, fixed_size=QSize(351, 51), layout_support=True, length=42
        )
        self.lineEditAddress.setFocusPolicy(Qt.ClickFocus)
        self.lineEditAddress.setProperty("iconable", True)
        self.lineEditAddress.setObjectName('lineEditAddress')

        self.labelAddressIcon = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21
        )

        self.labelAddressValid = SPGraphics.QuickLabel(
            self, scaled=True, fixed_size=Size.s21,
            pixmap=images.data.icons.ok41, tooltip=QApplication.toolTip.addressValidB
        )
        self.labelAddressValid.setCursor(Qt.PointingHandCursor)
        self.labelAddressValid.hide()

        self.labelAddressAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QApplication.toolTip.addressAlert
        )
        self.labelAddressAlert.setCursor(Qt.PointingHandCursor)
        self.labelAddressAlert.hide()

        self.pushButtonAddNew = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QApplication.toolTip.addNewAddressBook
        )
        self.pushButtonAddNew.hide()

        self.layout().addWidget(self.labelTitle)
        self.layout().addWidget(self.lineEditAddress, alignment=Qt.AlignHCenter)
        self.lineEditAddress.layout().addWidget(self.labelAddressIcon, alignment=Qt.AlignLeft)
        self.lineEditAddress.layout().addWidget(self.labelAddressValid, alignment=Qt.AlignLeft)
        self.lineEditAddress.layout().addWidget(self.labelAddressAlert, alignment=Qt.AlignRight)
        self.lineEditAddress.layout().addWidget(self.pushButtonAddNew, alignment=Qt.AlignRight)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__headerWidget = None
        self.__tabWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.WITHDRAW)

        self.__headerWidget = HeaderWidget(self)
        self.__headerWidget.lineEditAddress.textChanged.connect(self.address_changed)
        self.__headerWidget.pushButtonAddNew.clicked.connect(self.add_new_clicked)

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__tabWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.withdraw)
        self.__headerWidget.labelAddressIcon.setPixmap(images.data.icons.changeable.search21)
        self.__headerWidget.pushButtonAddNew.setIcon(QIcon(images.data.icons.changeable.plus21))

    def re_translate(self):
        self.__headerWidget.labelTitle.setText(translator("Send to"))
        self.__headerWidget.lineEditAddress.setPlaceholderText(translator("Search, Public Address (0x)"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.title)
        self.__headerWidget.lineEditAddress.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        font.setBold(True)
        self.__headerWidget.labelTitle.setFont(font)

    @pyqtSlot()
    def add_new_clicked(self):
        pass

    @pyqtSlot(str)
    def address_changed(self, text: str, valid: bool = False, addable: bool = False):
        self.__headerWidget.lineEditAddress.setProperty('isValid', valid)
        self.__headerWidget.lineEditAddress.setProperty('addable', addable)
        self.__headerWidget.labelAddressIcon.setHidden(valid)
        self.__headerWidget.labelAddressValid.setVisible(valid)
        self.__headerWidget.labelAddressAlert.setHidden(valid or not text)
        self.__headerWidget.pushButtonAddNew.setVisible(addable)
        self.__polish(self.__headerWidget.lineEditAddress)
        self.__inputs_validation()

    @pyqtSlot()
    def __tab_changed(self):
        widget = self.__tabWidget.currentWidget()
        self.__tabTransMotion = SPGraphics.OpacityMotion(widget)
        self.__tabTransMotion.temp_show(
            duration=500, finished=lambda: widget.setGraphicsEffect(None)
        ).start()

    def add_tab(self, model: QWidget, name: str):
        self.__tabWidget.addTab(model, name)

    def set_address(self, text: str):
        self.__headerWidget.lineEditAddress.setText(text)

    def get_address_text(self) -> str:
        return self.__headerWidget.lineEditAddress.text()

    def reset(self):
        self.__headerWidget.lineEditAddress.clear()
        self.__tabWidget.setCurrentIndex(0)

    def __inputs_validation(self):
        valid = False
        if self.__headerWidget.lineEditAddress.property('isValid'):
            valid = True

        if valid:
            self.__headerWidget.lineEditAddress.setReadOnly(True)
            self.__tabWidget.setCurrentIndex(1)
        else:
            self.__headerWidget.lineEditAddress.setReadOnly(False)
            self.__tabWidget.setCurrentIndex(0)

    @staticmethod
    def __polish(widget: QLineEdit):
        widget.style().unpolish(widget)
        widget.style().polish(widget)
