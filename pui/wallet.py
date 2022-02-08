from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress, qmenu


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__headerWidget = None
        self.__labelUsername = None
        self.__pushButtonMenu = None
        self.__pushButtonDetails = None
        self.__pushButtonAddToken = None
        self.__pushButtonExplorer = None
        self.__pushButtonRemove = None
        self.__pushButtonLogout = None
        self.__menuWallet = None
        self.__labelAddress = None
        self.__footerWidget = None
        self.__pushButtonDeposit = None
        self.__pushButtonWithdraw = None
        self.__pushButtonStake = None
        self.__pushButtonSwap = None
        self.__pushButtonHistory = None
        self.__tabWidget = None

    def setup(self):
        button_size = QSize(61, 31)
        menu_button_size = QSize(180, 41)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.WALLET)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__headerWidget = QWidget(self, flags=Qt.SubWindow)
        self.__headerWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.__headerWidget.setLayout(QGridLayout())
        self.__headerWidget.setObjectName('headerWidget')

        self.__labelUsername = SPGraphics.QuickLabel(
            self, fixed_height=31, align=Qt.AlignHCenter | Qt.AlignBottom
        )
        self.__labelUsername.setWordWrap(False)

        self.__pushButtonMenu = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QObject.toolTip.menu
        )
        self.__pushButtonMenu.clicked.connect(self.menu_clicked)

        self.__pushButtonDetails = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.details21), icon_size=Size.s21, fixed_size=menu_button_size
        )
        self.__pushButtonDetails.clicked.connect(self.details_clicked)

        self.__pushButtonAddToken = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.plus21), icon_size=Size.s21, fixed_size=menu_button_size
        )
        self.__pushButtonAddToken.clicked.connect(self.add_token_clicked)

        self.__pushButtonExplorer = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.external21), icon_size=Size.s21, fixed_size=menu_button_size
        )
        self.__pushButtonExplorer.clicked.connect(self.explorer_clicked)

        self.__pushButtonRemove = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.trash21), icon_size=Size.s21, fixed_size=menu_button_size
        )
        self.__pushButtonRemove.clicked.connect(self.remove_clicked)

        self.__pushButtonLogout = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.logout21), icon_size=Size.s21, fixed_size=menu_button_size
        )
        self.__pushButtonLogout.clicked.connect(self.logout_clicked)

        self.__menuWallet = qmenu.UiForm(self)
        self.__menuWallet.setup()
        self.__menuWallet.add_button(self.__pushButtonDetails)
        self.__menuWallet.add_button(self.__pushButtonAddToken)
        self.__menuWallet.add_button(self.__pushButtonExplorer)
        self.__menuWallet.add_button(self.__pushButtonRemove)
        self.__menuWallet.add_button(self.__pushButtonLogout)

        self.__labelAddress = qlabeladdress.QLabelAddress(
            self, fixed_height=21, copy_tooltip=QObject.toolTip.copyR
        )

        self.__footerWidget = QWidget(self, flags=Qt.SubWindow)
        self.__footerWidget.setLayout(QHBoxLayout())
        self.__footerWidget.layout().setContentsMargins(0, 0, 0, 0)
        self.__footerWidget.layout().setAlignment(Qt.AlignHCenter)

        self.__pushButtonDeposit = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size, tooltip=QObject.toolTip.depositB
        )
        self.__pushButtonDeposit.clicked.connect(self.deposit_clicked)

        self.__pushButtonWithdraw = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size, tooltip=QObject.toolTip.withdrawB
        )
        self.__pushButtonWithdraw.clicked.connect(self.withdraw_clicked)

        self.__pushButtonStake = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size, tooltip=QObject.toolTip.stakeB
        )
        self.__pushButtonStake.clicked.connect(self.stake_clicked)

        self.__pushButtonSwap = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size, tooltip=QObject.toolTip.swapB
        )
        self.__pushButtonSwap.clicked.connect(self.swap_clicked)

        self.__pushButtonHistory = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=button_size, tooltip=QObject.toolTip.historyB
        )
        self.__pushButtonHistory.clicked.connect(self.history_clicked)

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.__pushButtonBack.raise_()

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__tabWidget)
        self.__headerWidget.layout().addWidget(self.__labelUsername, 0, 0, 1, 2, Qt.AlignHCenter)
        self.__headerWidget.layout().addWidget(self.__pushButtonMenu, 0, 1, 1, 1, Qt.AlignRight)
        self.__headerWidget.layout().addWidget(self.__labelAddress, 1, 0, 1, 2, Qt.AlignHCenter)
        self.__headerWidget.layout().addWidget(self.__footerWidget, 2, 0, 1, 2)
        self.__footerWidget.layout().addWidget(self.__pushButtonDeposit)
        self.__footerWidget.layout().addWidget(self.__pushButtonWithdraw)
        self.__footerWidget.layout().addWidget(self.__pushButtonStake)
        self.__footerWidget.layout().addWidget(self.__pushButtonSwap)
        self.__footerWidget.layout().addWidget(self.__pushButtonHistory)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.wallet)
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))
        self.__pushButtonMenu.setIcon(QIcon(images.data.icons.changeable.dots21))
        self.__labelAddress.set_icon(QIcon(images.data.icons.changeable.copy21))
        self.__pushButtonDeposit.setIcon(QIcon(images.data.icons.changeable.deposit24))
        self.__pushButtonWithdraw.setIcon(QIcon(images.data.icons.changeable.withdraw24))
        self.__pushButtonStake.setIcon(QIcon(images.data.icons.changeable.stake24))
        self.__pushButtonSwap.setIcon(QIcon(images.data.icons.changeable.swap24))
        self.__pushButtonHistory.setIcon(QIcon(images.data.icons.changeable.history24))

    def re_translate(self):
        self.__pushButtonDetails.setText(translator("Wallet Details"))
        self.__pushButtonAddToken.setText(translator("Add Token"))
        self.__pushButtonExplorer.setText(translator("View in Explorer"))
        self.__pushButtonRemove.setText(translator("Remove Wallet"))
        self.__pushButtonLogout.setText(translator("Logout"))

    def re_font(self):
        font = QFont()

        self.__pushButtonDetails.setFont(font)
        self.__pushButtonAddToken.setFont(font)
        self.__pushButtonExplorer.setFont(font)
        self.__pushButtonRemove.setFont(font)
        self.__pushButtonLogout.setFont(font)
        self.__labelAddress.set_font(font)

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__labelUsername.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def menu_clicked(self):
        pos = self.__pushButtonMenu.mapToGlobal(QPoint())
        pos.setX(pos.x() - 20)
        pos.setY(pos.y() + 20)

        self.__menuWallet.exec_(pos)

    @pyqtSlot()
    def details_clicked(self):
        self.__menuWallet.close()

    @pyqtSlot()
    def add_token_clicked(self):
        self.__menuWallet.close()

    @pyqtSlot()
    def explorer_clicked(self):
        self.__menuWallet.close()

    @pyqtSlot()
    def remove_clicked(self):
        self.__menuWallet.close()

    @pyqtSlot()
    def logout_clicked(self):
        self.__menuWallet.close()

    @pyqtSlot()
    def deposit_clicked(self):
        pass

    @pyqtSlot()
    def withdraw_clicked(self):
        pass

    @pyqtSlot()
    def stake_clicked(self):
        pass

    @pyqtSlot()
    def swap_clicked(self):
        pass

    @pyqtSlot()
    def history_clicked(self):
        pass

    @pyqtSlot()
    def __tab_changed(self):
        widget = self.__tabWidget.currentWidget()
        self.__tabTransMotion = SPGraphics.GeometryMotion(widget)
        self.__tabTransMotion.temp_x(start_x=widget.width(), end_x=0, duration=300).start()

    def add_tab(self, model: QObject, name: str):
        self.__tabWidget.addTab(model, name)

    def set_current_tab(self, name: str):
        widget = self.__tabWidget.findChild(QWidget, name)
        self.__tabWidget.setCurrentWidget(widget)

    def set_username(self, text: str):
        self.__labelUsername.setText(text)

    def set_address(self, text: str):
        self.__labelAddress.set_address(text, False)

    def reset(self):
        self.__labelUsername.clear()
        self.__labelAddress.label.clear()
