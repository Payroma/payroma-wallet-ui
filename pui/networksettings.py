from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, Size


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__pushButtonAddNew = None
        self.__listWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(11)
        self.setObjectName(Tab.NETWORK_SETTINGS)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__pushButtonAddNew = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.addNewR
        )
        self.__pushButtonAddNew.clicked.connect(self.add_new_clicked)

        self.__listWidget = SPGraphics.QuickListWidget(
            self, spacing=10, empty_illustration=images.data.illustrations.no_data
        )
        self.__listWidget.layout().setAlignment(Qt.AlignCenter)
        self.__listWidget.labelIllustration.setAlignment(Qt.AlignHCenter)
        self.__listWidget.labelTitle.setAlignment(Qt.AlignHCenter)
        self.__listWidget.labelDescription.setAlignment(Qt.AlignHCenter)
        self.__listWidget.labelDescription.setSizePolicy(QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Preferred
        ))
        self.__listWidget.itemClicked.connect(self.item_clicked)

        self.layout().addWidget(self.__pushButtonAddNew, alignment=Qt.AlignRight)
        self.layout().addWidget(self.__listWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))
        self.__pushButtonAddNew.setIcon(QIcon(images.data.icons.changeable.plus21))

    def re_translate(self):
        self.__listWidget.labelTitle.setText(translator("No network has been added yet!"))
        self.__listWidget.labelDescription.setText(translator(
            "Let's add your first network today, click on \"+\" button. It's easy."
        ))

    def re_font(self):
        font = QFont()

        self.__listWidget.labelDescription.setFont(font)

        font.setFamily(fonts.data.family.black)
        font.setPointSize(fonts.data.size.medium)
        self.__listWidget.labelTitle.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

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
