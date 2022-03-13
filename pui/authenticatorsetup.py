from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, styles, Size, qnotice


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 21, 11, 21)
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
            self, fixed_size=QSize(51, 1)
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
            self, fixed_size=QSize(51, 1)
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

        self.__headerWidget = None
        self.__tabWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.AUTHENTICATOR_SETUP)

        self.__headerWidget = HeaderWidget(self)

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__tabWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.authenticatorsetup)

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
        self.__headerWidget.tabs_update(self.__tabWidget.currentIndex())

    def reset(self):
        self.__tabWidget.setCurrentIndex(0)
        self.__headerWidget.tabs_update(self.__tabWidget.currentIndex())
