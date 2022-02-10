from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qnotice


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__headerWidget = None
        self.__labelDownload = None
        self.__qnoticeDownload = None
        self.__progressDownloadWidget = None
        self.__labelVerification = None
        self.__qnoticeVerification = None
        self.__progressVerificationWidget = None
        self.__labelScan = None
        self.__qnoticeScan = None
        self.__progressScanWidget = None
        self.__labelBackup = None
        self.__qnoticeBackup = None
        self.__tabWidget = None
        self.__downloadWidget = None
        self.__verificationWidget = None
        self.__scanWidget = None
        self.__backupWidget = None

    def setup(self):
        progress_size = QSize(31, 1)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 21, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.AUTHENTICATOR_SETUP)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__headerWidget = QWidget(self, flags=Qt.SubWindow)
        self.__headerWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.__headerWidget.setLayout(QGridLayout())
        self.__headerWidget.layout().setAlignment(Qt.AlignCenter)
        self.__headerWidget.layout().setContentsMargins(21, 21, 21, 21)
        self.__headerWidget.layout().setSpacing(0)
        self.__headerWidget.setObjectName('headerWidget')

        self.__labelDownload = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignCenter
        )

        self.__qnoticeDownload = qnotice.QNotice(
            self, fixed_size=Size.s21
        )

        self.__progressDownloadWidget = SPGraphics.QuickWidget(
            self, fixed_size=progress_size
        )
        self.__progressDownloadWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__progressDownloadWidget.setObjectName('progressDownloadWidget')

        self.__labelVerification = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignCenter
        )

        self.__qnoticeVerification = qnotice.QNotice(
            self, fixed_size=Size.s21
        )

        self.__progressVerificationWidget = SPGraphics.QuickWidget(
            self, fixed_size=progress_size
        )
        self.__progressVerificationWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__progressVerificationWidget.setObjectName('progressVerificationWidget')

        self.__labelScan = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignCenter
        )

        self.__qnoticeScan = qnotice.QNotice(
            self, fixed_size=Size.s21
        )

        self.__progressScanWidget = SPGraphics.QuickWidget(
            self, fixed_size=progress_size
        )
        self.__progressScanWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__progressScanWidget.setObjectName('progressScanWidget')

        self.__labelBackup = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignCenter
        )

        self.__qnoticeBackup = qnotice.QNotice(
            self, fixed_size=Size.s21
        )

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.__pushButtonBack.raise_()

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__tabWidget)
        self.__headerWidget.layout().addWidget(self.__labelDownload, 0, 0, 1, 1)
        self.__headerWidget.layout().addWidget(self.__qnoticeDownload, 1, 0, 1, 1, Qt.AlignHCenter)
        self.__headerWidget.layout().addWidget(self.__progressDownloadWidget, 1, 1, 1, 1)
        self.__headerWidget.layout().addWidget(self.__labelVerification, 0, 2, 1, 1)
        self.__headerWidget.layout().addWidget(self.__qnoticeVerification, 1, 2, 1, 1, Qt.AlignHCenter)
        self.__headerWidget.layout().addWidget(self.__progressVerificationWidget, 1, 3, 1, 1)
        self.__headerWidget.layout().addWidget(self.__labelScan, 0, 4, 1, 1)
        self.__headerWidget.layout().addWidget(self.__qnoticeScan, 1, 4, 1, 1, Qt.AlignHCenter)
        self.__headerWidget.layout().addWidget(self.__progressScanWidget, 1, 5, 1, 1)
        self.__headerWidget.layout().addWidget(self.__labelBackup, 0, 6, 1, 1)
        self.__headerWidget.layout().addWidget(self.__qnoticeBackup, 1, 6, 1, 1, Qt.AlignHCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.authenticatorsetup)
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))

    def re_translate(self):
        self.__labelDownload.setText(translator("Download App"))
        self.__labelVerification.setText(translator("Verification"))
        self.__labelScan.setText(translator("Scan QR Code"))
        self.__labelBackup.setText(translator("Backup Key"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.small)
        self.__labelDownload.setFont(font)
        self.__labelVerification.setFont(font)
        self.__labelScan.setFont(font)
        self.__labelBackup.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
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
        self.__tabs_update()

    def reset(self):
        self.__tabWidget.setCurrentIndex(0)
        self.__tabs_update()

    def __tabs_update(self):
        cur_index = self.__tabWidget.currentIndex()
        tabs = {
            0: {'icon': self.__qnoticeDownload, 'progress': self.__progressDownloadWidget},
            1: {'icon': self.__qnoticeVerification, 'progress': self.__progressVerificationWidget},
            2: {'icon': self.__qnoticeScan, 'progress': self.__progressScanWidget},
            3: {'icon': self.__qnoticeBackup, 'progress': None}
        }

        for index, tab in tabs.items():
            status = False
            if cur_index > index:
                status = True

            tab['icon'].setEnabled(status)
            if tab['progress']:
                tab['progress'].setEnabled(status)
