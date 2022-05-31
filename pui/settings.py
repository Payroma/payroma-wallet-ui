from plibs import *
from pheader import *
from pcontroller import translator, button_text_visible
from pui import SetupForm, fonts, images, styles, Size, qnotice


class NetworkWidget(QWidget):
    def __init__(self, parent):
        super(NetworkWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0, 11, 0, 11)
        self.layout().setHorizontalSpacing(11)
        self.layout().setVerticalSpacing(0)

        self.qnotice = qnotice.QNotice(
            self, fixed_size=Size.s21, tooltip=QApplication.toolTip.networkStatusR
        )
        self.qnotice.setCursor(Qt.PointingHandCursor)
        self.qnotice.setDisabled(True)

        self.labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=21
        )
        self.labelTitle.setWordWrap(False)

        self.pushButton = SPGraphics.QuickPushButton(
            fixed_height=21, value_changed=QApplication.textColorAnimate,
            start_value=styles.data.colors.font_description, end_value=styles.data.colors.highlight
        )
        self.pushButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.layout().addWidget(self.labelTitle, 0, 0, 1, 1)
        self.layout().addWidget(self.qnotice, 0, 1, 1, 1, Qt.AlignRight)
        self.layout().addWidget(self.pushButton, 1, 0, 1, 2)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelThemeIllustration = None
        self.__labelDarkMode = None
        self.__switchDarkMode = None
        self.__networkWidget = None
        self.__labelBackupTitle = None
        self.__loadingEffectBackup = None
        self.__pushButtonBackup = None
        self.__loadingEffectImport = None
        self.__pushButtonImport = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.SETTINGS)

        self.__labelThemeIllustration = SPGraphics.QuickLabel(
            self, fixed_size=Size.s100, scaled=True
        )

        self.__labelDarkMode = SPGraphics.QuickLabel(
            self, fixed_height=31
        )

        self.__switchDarkMode = SPGraphics.QSwitch(self, 10, 13)
        self.__switchDarkMode.clicked.connect(self.switch_clicked)
        if styles.CURRENT_TEMPLATE:
            self.__switchDarkMode.setChecked(True)

        self.__networkWidget = NetworkWidget(self)
        self.__networkWidget.pushButton.clicked.connect(self.network_clicked)

        self.__labelBackupTitle = SPGraphics.QuickLabel(
            self, fixed_height=81, align=Qt.AlignCenter
        )

        self.__loadingEffectBackup = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.__pushButtonBackup = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonBackup.setLayout(QVBoxLayout())
        self.__pushButtonBackup.clicked.connect(self.backup_clicked)

        self.__loadingEffectImport = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.__pushButtonImport = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonImport.setLayout(QVBoxLayout())
        self.__pushButtonImport.clicked.connect(self.import_clicked)

        self.layout().addWidget(self.__labelThemeIllustration, 0, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelDarkMode, 1, 0, 1, 1)
        self.layout().addWidget(self.__switchDarkMode, 1, 1, 1, 1)
        self.layout().addWidget(self.__networkWidget, 2, 0, 1, 2)
        self.layout().addWidget(self.__labelBackupTitle, 3, 0, 1, 2)
        self.layout().addWidget(self.__pushButtonBackup, 4, 0, 1, 2, Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonImport, 5, 0, 1, 2, Qt.AlignHCenter)
        self.__pushButtonBackup.layout().addWidget(self.__loadingEffectBackup, alignment=Qt.AlignCenter)
        self.__pushButtonImport.layout().addWidget(self.__loadingEffectImport, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.__labelThemeIllustration.setPixmap(images.data.illustrations.theme_status)

    def re_translate(self):
        self.__labelDarkMode.setText(translator("Switch to dark mode theme."))
        self.__networkWidget.labelTitle.setText(translator("Current blockchain network."))
        self.__labelBackupTitle.setText(translator(
            "Backup all your wallets to a specific location on your system."
        ))
        self.__pushButtonBackup.setText(translator("Backup Your Wallets"))
        self.__pushButtonImport.setText(translator("Import From External File"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.title)
        self.__labelDarkMode.setFont(font)

        font.setBold(True)
        self.__networkWidget.labelTitle.setFont(font)

        self.__labelBackupTitle.setFont(font)
        self.__pushButtonBackup.setFont(font)
        self.__pushButtonImport.setFont(font)

        font.setBold(False)
        font.setUnderline(True)
        self.__networkWidget.pushButton.setFont(font)

    @pyqtSlot(bool)
    def switch_clicked(self, state: bool):
        pass

    @pyqtSlot()
    def network_clicked(self):
        pass

    @pyqtSlot()
    def backup_clicked(self):
        self.__loadingEffectBackup.start()
        button_text_visible(self.__pushButtonBackup, False)

    @pyqtSlot()
    def import_clicked(self):
        self.__loadingEffectImport.start()
        button_text_visible(self.__pushButtonImport, False)

    def backup_completed(self):
        self.__loadingEffectBackup.stop()
        button_text_visible(self.__pushButtonBackup, True)

    def import_completed(self):
        self.__loadingEffectImport.stop()
        button_text_visible(self.__pushButtonImport, True)

    def set_data(self, network_connected: bool, network_name: str):
        self.__networkWidget.qnotice.setEnabled(network_connected)
        self.__networkWidget.pushButton.setText(network_name)
