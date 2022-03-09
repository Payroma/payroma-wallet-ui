from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, images, styles, Size, qnotice


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(21, 21, 21, 21)
        self.layout().setHorizontalSpacing(0)
        self.layout().setVerticalSpacing(11)

        self.labelDownload = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.labelDownload.setObjectName('labelDownload')

        self.qnoticeDownload = qnotice.QNotice(
            self, fixed_size=Size.s21
        )

        self.progressDownloadWidget = SPGraphics.QuickWidget(
            self, fixed_size=QSize(31, 1)
        )
        self.progressDownloadWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.progressDownloadWidget.setObjectName('progressDownloadWidget')

        self.labelVerification = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.labelVerification.setObjectName('labelVerification')

        self.qnoticeVerification = qnotice.QNotice(
            self, fixed_size=Size.s21
        )

        self.progressVerificationWidget = SPGraphics.QuickWidget(
            self, fixed_size=QSize(31, 1)
        )
        self.progressVerificationWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.progressVerificationWidget.setObjectName('progressVerificationWidget')

        self.labelScan = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.labelScan.setObjectName('labelScan')

        self.qnoticeScan = qnotice.QNotice(
            self, fixed_size=Size.s21
        )

        self.layout().addWidget(self.labelDownload, 0, 0, 1, 1)
        self.layout().addWidget(self.qnoticeDownload, 1, 0, 1, 1, Qt.AlignHCenter)
        self.layout().addWidget(self.progressDownloadWidget, 1, 1, 1, 1)
        self.layout().addWidget(self.labelVerification, 0, 2, 1, 1)
        self.layout().addWidget(self.qnoticeVerification, 1, 2, 1, 1, Qt.AlignHCenter)
        self.layout().addWidget(self.progressVerificationWidget, 1, 3, 1, 1)
        self.layout().addWidget(self.labelScan, 0, 4, 1, 1)
        self.layout().addWidget(self.qnoticeScan, 1, 4, 1, 1, Qt.AlignHCenter)

    def tabs_update(self, cur_index: int):
        font = QFont()
        cur_index = cur_index if cur_index > 0 else 0
        tabs = {
            0: {
                'label': self.labelDownload,
                'icon': self.qnoticeDownload,
                'progress': self.progressDownloadWidget
            },
            1: {
                'label': self.labelVerification,
                'icon': self.qnoticeVerification,
                'progress': self.progressVerificationWidget
            },
            2: {
                'label': self.labelScan,
                'icon': self.qnoticeScan,
                'progress': None
            },
            3: {
                'label': None,
                'icon': None,
                'progress': None
            }
        }

        for index, tab in tabs.items():
            status = False
            if cur_index > index:
                status = True

            if tab['label']:
                focus_status = True if cur_index == index else False
                font.setBold(focus_status)
                tab['label'].setEnabled(focus_status)
                tab['label'].setFont(font)

            if tab['icon']:
                tab['icon'].setEnabled(status)

            if tab['progress']:
                tab['progress'].setEnabled(status)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__headerWidget = None
        self.__tabWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.AUTHENTICATOR_SETUP)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__headerWidget = HeaderWidget(self)

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.__pushButtonBack.raise_()

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__tabWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.authenticatorsetup)
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))

    def re_translate(self):
        self.__headerWidget.labelDownload.setText(translator("Download App"))
        self.__headerWidget.labelVerification.setText(translator("Verification"))
        self.__headerWidget.labelScan.setText(translator("Scan QR Code"))

    def re_font(self):
        font = QFont()

        self.__headerWidget.labelDownload.setFont(font)
        self.__headerWidget.labelVerification.setFont(font)
        self.__headerWidget.labelScan.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def __tab_changed(self):
        widget = self.__tabWidget.currentWidget()
        self.__tabTransMotion = SPGraphics.GeometryMotion(widget)
        self.__tabTransMotion.temp_x(start_x=widget.width(), end_x=0, duration=500).start()

    def add_tab(self, model: QObject, name: str):
        self.__tabWidget.addTab(model, name)

    def set_current_tab(self, name: str):
        widget = self.__tabWidget.findChild(QWidget, name)
        self.__tabWidget.setCurrentWidget(widget)
        self.__headerWidget.tabs_update(self.__tabWidget.currentIndex())

    def reset(self):
        self.__tabWidget.setCurrentIndex(0)
        self.__headerWidget.tabs_update(self.__tabWidget.currentIndex())
