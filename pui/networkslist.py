from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(11, 11, 11, 11)
        self.layout().setSpacing(0)

        self.labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=31, align=Qt.AlignCenter
        )
        self.labelTitle.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))

        self.pushButtonAddNew = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QApplication.toolTip.addNewR
        )

        self.layout().addWidget(self.labelTitle, 0, 0, 1, 2)
        self.layout().addWidget(self.pushButtonAddNew, 0, 1, 1, 1, Qt.AlignRight)


class ListWidget(SPGraphics.QuickListWidget):
    def __init__(self, parent):
        super(ListWidget, self).__init__(
            parent, spacing=10, empty_illustration=images.data.illustrations.no_data
        )

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout().setContentsMargins(21, 0, 21, 0)
        self.layout().setAlignment(Qt.AlignVCenter)
        self.labelIllustration.setAlignment(Qt.AlignHCenter)
        self.labelTitle.setAlignment(Qt.AlignHCenter)
        self.labelDescription.setAlignment(Qt.AlignHCenter)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__headerWidget = None
        self.__listWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.NETWORKS_LIST)

        self.__headerWidget = HeaderWidget(self)
        self.__headerWidget.pushButtonAddNew.clicked.connect(self.add_new_clicked)

        self.__listWidget = ListWidget(self)
        self.__listWidget.itemClicked.connect(self.item_clicked)

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__listWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.networkslist)
        self.__headerWidget.pushButtonAddNew.setIcon(QIcon(images.data.icons.changeable.plus21))

    def re_translate(self):
        self.__headerWidget.labelTitle.setText(translator("Blockchain Networks"))
        self.__listWidget.labelTitle.setText(translator("No networks has been added yet!"))
        self.__listWidget.labelDescription.setText(translator(
            "Let's add your first network today, click on \"+\" button. It's easy."
        ))

    def re_font(self):
        font = QFont()

        self.__listWidget.labelDescription.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        font.setBold(True)
        self.__headerWidget.labelTitle.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setBold(False)
        self.__listWidget.labelTitle.setFont(font)

    @pyqtSlot()
    def add_new_clicked(self):
        pass

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem) -> QWidget:
        return self.__listWidget.itemWidget(item)

    def add_item(self, item: QListWidgetItem):
        self.__listWidget.add_quick_item(item)

    def reset(self):
        self.__listWidget.clear()
