from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qlabeladdress, qmenu


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        button_size = QSize(181, 41)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(11, 11, 11, 11)

        self.labelUsername = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.labelUsername.setWordWrap(False)

        self.pushButtonMenu = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=QApplication.toolTip.menuR
        )

        self.pushButtonDetails = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.details21), icon_size=Size.s21, fixed_size=button_size
        )

        self.pushButtonAddToken = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.plus21), icon_size=Size.s21, fixed_size=button_size
        )

        self.pushButtonExplorer = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.external21), icon_size=Size.s21, fixed_size=button_size
        )

        self.pushButtonRemove = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.trash21), icon_size=Size.s21, fixed_size=button_size
        )

        self.pushButtonLogout = SPGraphics.QuickPushButton(
            self, icon=QIcon(images.data.icons.logout21), icon_size=Size.s21, fixed_size=button_size
        )

        self.menuWallet = qmenu.UiForm(self)
        self.menuWallet.setup()
        self.menuWallet.add_button(self.pushButtonDetails)
        self.menuWallet.add_button(self.pushButtonAddToken)
        self.menuWallet.add_button(self.pushButtonExplorer)
        self.menuWallet.add_button(self.pushButtonRemove)
        self.menuWallet.add_button(self.pushButtonLogout)

        self.labelAddress = qlabeladdress.QLabelAddress(
            self, fixed_height=21, copy_tooltip=QApplication.toolTip.copyR
        )

        self.layout().addWidget(self.labelUsername, 0, 0, 1, 2)
        self.layout().addWidget(self.pushButtonMenu, 0, 1, 1, 1, Qt.AlignRight)
        self.layout().addWidget(self.labelAddress, 1, 0, 1, 2, Qt.AlignHCenter)


class TabsWidget(QWidget):
    def __init__(self, parent):
        super(TabsWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignHCenter)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(21)

        self.pushButtonDeposit = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=Size.s31, tooltip=QApplication.toolTip.depositB
        )

        self.pushButtonWithdraw = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=Size.s31, tooltip=QApplication.toolTip.withdrawB
        )

        self.pushButtonStake = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=Size.s31, tooltip=QApplication.toolTip.stakeB
        )

        self.pushButtonSwap = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=Size.s31, tooltip=QApplication.toolTip.swapB
        )

        self.pushButtonHistory = SPGraphics.QuickPushButton(
            self, icon_size=Size.s24, fixed_size=Size.s31, tooltip=QApplication.toolTip.historyB
        )

        self.layout().addWidget(self.pushButtonDeposit)
        self.layout().addWidget(self.pushButtonWithdraw)
        self.layout().addWidget(self.pushButtonStake)
        self.layout().addWidget(self.pushButtonSwap)
        self.layout().addWidget(self.pushButtonHistory)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__headerWidget = None
        self.__tabsWidget = None
        self.__tabWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.WALLET)

        self.__headerWidget = HeaderWidget(self)
        self.__headerWidget.pushButtonMenu.clicked.connect(self.menu_clicked)
        self.__headerWidget.pushButtonDetails.clicked.connect(self.details_clicked)
        self.__headerWidget.pushButtonAddToken.clicked.connect(self.add_token_clicked)
        self.__headerWidget.pushButtonExplorer.clicked.connect(self.explorer_clicked)
        self.__headerWidget.pushButtonRemove.clicked.connect(self.remove_clicked)
        self.__headerWidget.pushButtonLogout.clicked.connect(self.logout_clicked)

        self.__tabsWidget = TabsWidget(self)
        self.__tabsWidget.pushButtonDeposit.clicked.connect(self.deposit_clicked)
        self.__tabsWidget.pushButtonWithdraw.clicked.connect(self.withdraw_clicked)
        self.__tabsWidget.pushButtonStake.clicked.connect(self.stake_clicked)
        self.__tabsWidget.pushButtonSwap.clicked.connect(self.swap_clicked)
        self.__tabsWidget.pushButtonHistory.clicked.connect(self.history_clicked)

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__tabWidget)
        self.__headerWidget.layout().addWidget(self.__tabsWidget, 2, 0, 1, 2)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.wallet)
        self.__headerWidget.pushButtonMenu.setIcon(QIcon(images.data.icons.changeable.dots21))
        self.__headerWidget.labelAddress.setIcon(QIcon(images.data.icons.changeable.copy21))
        self.__tabsWidget.pushButtonDeposit.setIcon(QIcon(images.data.icons.changeable.deposit24))
        self.__tabsWidget.pushButtonWithdraw.setIcon(QIcon(images.data.icons.changeable.withdraw24))
        self.__tabsWidget.pushButtonStake.setIcon(QIcon(images.data.icons.changeable.stake24))
        self.__tabsWidget.pushButtonSwap.setIcon(QIcon(images.data.icons.changeable.swap24))
        self.__tabsWidget.pushButtonHistory.setIcon(QIcon(images.data.icons.changeable.history24))

    def re_translate(self):
        self.__headerWidget.pushButtonDetails.setText(translator("Wallet Details"))
        self.__headerWidget.pushButtonAddToken.setText(translator("Add Token"))
        self.__headerWidget.pushButtonExplorer.setText(translator("View at Explorer"))
        self.__headerWidget.pushButtonRemove.setText(translator("Remove Wallet"))
        self.__headerWidget.pushButtonLogout.setText(translator("Logout"))

    def re_font(self):
        font = QFont()

        self.__headerWidget.pushButtonDetails.setFont(font)
        self.__headerWidget.pushButtonAddToken.setFont(font)
        self.__headerWidget.pushButtonExplorer.setFont(font)
        self.__headerWidget.pushButtonRemove.setFont(font)
        self.__headerWidget.pushButtonLogout.setFont(font)
        self.__headerWidget.labelAddress.setFont(font)

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__headerWidget.labelUsername.setFont(font)

    @pyqtSlot()
    def menu_clicked(self):
        pos = self.__headerWidget.pushButtonMenu.mapToGlobal(QPoint())
        pos.setX(pos.x() - 20)
        pos.setY(pos.y() + 20)

        self.__headerWidget.menuWallet.exec_(pos)

    @pyqtSlot()
    def details_clicked(self):
        self.__headerWidget.menuWallet.close()

    @pyqtSlot()
    def add_token_clicked(self):
        self.__headerWidget.menuWallet.close()

    @pyqtSlot()
    def explorer_clicked(self):
        self.__headerWidget.menuWallet.close()

    @pyqtSlot()
    def remove_clicked(self):
        self.__headerWidget.menuWallet.close()

    @pyqtSlot()
    def logout_clicked(self):
        self.__headerWidget.menuWallet.close()

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
        self.__tabTransMotion = SPGraphics.OpacityMotion(widget)
        self.__tabTransMotion.temp_show(
            duration=500, finished=lambda: widget.setGraphicsEffect(None)
        ).start()

    def add_tab(self, model: QObject, name: str):
        self.__tabWidget.addTab(model, name)

    def set_current_tab(self, name: str):
        widget = self.__tabWidget.findChild(QWidget, name)
        self.__tabWidget.setCurrentWidget(widget)

    def set_data(self, username: str, address: str):
        self.__headerWidget.labelUsername.setText(username)
        self.__headerWidget.labelAddress.setText(address, is_ellipsis=False)

    def reset(self):
        self.__headerWidget.labelUsername.clear()
        self.__headerWidget.labelAddress.clear()
