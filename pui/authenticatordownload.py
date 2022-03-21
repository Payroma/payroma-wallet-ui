from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, styles, Size


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelTitle = None
        self.__labelDescription = None
        self.__labelGoogle = None
        self.__pushButtonGooglePlay = None
        self.__pushButtonAppStore = None
        self.__labelAuthy = None
        self.__pushButtonAuthy = None
        self.__lineWidget = None
        self.__pushButtonNext = None

    def setup(self):
        button_size = QSize(137, 41)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setVerticalSpacing(11)
        self.setObjectName(Tab.AuthenticatorSetupTab.DOWNLOAD)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )

        self.__labelDescription = SPGraphics.QuickLabel(
            self, fixed_height=41, align=Qt.AlignTop | Qt.AlignHCenter
        )
        self.__labelDescription.setWordWrap(False)
        self.__labelDescription.setObjectName('labelDescription')

        self.__labelGoogle = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__pushButtonGooglePlay = SPGraphics.QuickPushButton(
            self, fixed_size=button_size
        )
        self.__pushButtonGooglePlay.setObjectName('pushButtonGooglePlay')
        self.__pushButtonGooglePlay.clicked.connect(self.google_play_clicked)

        self.__pushButtonAppStore = SPGraphics.QuickPushButton(
            self, fixed_size=button_size
        )
        self.__pushButtonAppStore.setObjectName('pushButtonAppStore')
        self.__pushButtonAppStore.clicked.connect(self.app_store_clicked)

        self.__labelAuthy = SPGraphics.QuickLabel(
            self, fixed_height=21
        )

        self.__pushButtonAuthy = SPGraphics.QuickPushButton(
            self, fixed_size=button_size
        )
        self.__pushButtonAuthy.setObjectName('pushButtonAuthy')
        self.__pushButtonAuthy.clicked.connect(self.authy_clicked)

        self.__lineWidget = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget.setObjectName('lineWidget')

        self.__pushButtonNext = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonNext.clicked.connect(self.next_clicked)

        self.layout().addWidget(self.__labelTitle, 0, 0, 1, 2)
        self.layout().addWidget(self.__labelDescription, 1, 0, 1, 2)
        self.layout().addWidget(self.__labelGoogle, 2, 0, 1, 2)
        self.layout().addWidget(self.__pushButtonGooglePlay, 3, 0, 1, 1, Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonAppStore, 3, 1, 1, 1, Qt.AlignLeft)
        self.layout().addWidget(self.__labelAuthy, 4, 0, 1, 2)
        self.layout().addWidget(self.__pushButtonAuthy, 5, 0, 1, 1, Qt.AlignHCenter)
        self.layout().addWidget(self.__lineWidget, 6, 0, 1, 2)
        self.layout().addWidget(self.__pushButtonNext, 7, 0, 1, 2, Qt.AlignHCenter)

        super(UiForm, self).setup()

    def re_translate(self):
        self.__labelTitle.setText(translator("Download and install app"))
        self.__labelDescription.setText(translator("Choose the authenticator application to download."))
        self.__labelGoogle.setText(translator("1 - Google Authenticator"))
        self.__labelAuthy.setText(translator("2 - Authy"))
        self.__pushButtonNext.setText(translator("Next"))

    def re_font(self):
        font = QFont()

        self.__labelDescription.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__labelGoogle.setFont(font)
        self.__labelAuthy.setFont(font)

        font.setBold(True)
        self.__pushButtonNext.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelTitle.setFont(font)

    @pyqtSlot()
    def google_play_clicked(self):
        pass

    @pyqtSlot()
    def app_store_clicked(self):
        pass

    @pyqtSlot()
    def authy_clicked(self):
        pass

    @pyqtSlot()
    def next_clicked(self):
        pass
