from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, qnotice


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelThemeIllustration = None
        self.__labelDarkMode = None
        self.__switchDarkMode = None
        self.__qnoticeNetwork = None
        self.__labelNetwork = None
        self.__pushButtonNetwork = None
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

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

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

        self.__qnoticeNetwork = qnotice.QNotice(
            self, fixed_size=Size.s21, tooltip=QObject.toolTip.networkStatus
        )
        self.__qnoticeNetwork.setCursor(Qt.PointingHandCursor)

        self.__labelNetwork = SPGraphics.QuickLabel(
            self, text='#Current network', fixed_height=31
        )

        self.__pushButtonNetwork = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.networkSettingsR
        )
        self.__pushButtonNetwork.clicked.connect(self.network_clicked)

        self.__labelBackupTitle = SPGraphics.QuickLabel(
            self, fixed_height=81, align=Qt.AlignCenter
        )

        self.__loadingEffectBackup = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.__pushButtonBackup = SPGraphics.QuickPushButton(
            self, fixed_size=QSize(301, 51), value_changed=QObject.mainModel.backgroundColorAnimated,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonBackup.setLayout(QVBoxLayout())
        self.__pushButtonBackup.clicked.connect(self.backup_clicked)

        self.__loadingEffectImport = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.__pushButtonImport = SPGraphics.QuickPushButton(
            self, fixed_size=QSize(301, 51), value_changed=QObject.mainModel.backgroundColorAnimated,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonImport.setLayout(QVBoxLayout())
        self.__pushButtonImport.clicked.connect(self.import_clicked)

        self.layout().addWidget(self.__labelThemeIllustration, 0, 0, 1, 3, Qt.AlignHCenter)
        self.layout().addWidget(self.__labelDarkMode, 1, 1, 1, 1)
        self.layout().addWidget(self.__switchDarkMode, 1, 2, 1, 1)
        self.layout().addWidget(self.__qnoticeNetwork, 2, 0, 1, 1)
        self.layout().addWidget(self.__labelNetwork, 2, 1, 1, 1)
        self.layout().addWidget(self.__pushButtonNetwork, 2, 2, 1, 1)
        self.layout().addWidget(self.__labelBackupTitle, 3, 0, 1, 3)
        self.layout().addWidget(self.__pushButtonBackup, 4, 0, 1, 3, Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonImport, 5, 0, 1, 3, Qt.AlignHCenter)
        self.__pushButtonBackup.layout().addWidget(self.__loadingEffectBackup, alignment=Qt.AlignCenter)
        self.__pushButtonImport.layout().addWidget(self.__loadingEffectImport, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))
        self.__labelThemeIllustration.setPixmap(images.data.illustrations.theme_status)
        self.__pushButtonNetwork.setIcon(QIcon(images.data.icons.changeable.change21))

    def re_translate(self):
        self.__labelDarkMode.setText(translator("Switch to dark mode theme."))
        self.__labelBackupTitle.setText(translator(
            "Backup all your wallets to a specific location on your system."
        ))
        self.__pushButtonBackup.setText(translator("Backup Your Wallets"))
        self.__pushButtonImport.setText(translator("Import From External File"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.title)
        self.__labelDarkMode.setFont(font)
        self.__labelNetwork.setFont(font)

        font.setBold(True)
        self.__labelBackupTitle.setFont(font)
        self.__pushButtonBackup.setFont(font)
        self.__pushButtonImport.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot(bool)
    def switch_clicked(self, state: bool):
        pass

    @pyqtSlot()
    def network_clicked(self):
        pass

    @pyqtSlot()
    def backup_clicked(self):
        self.__loadingEffectBackup.start()
        self.__pushButtonBack.hide()
        self.__pushButtonBackup.setText("")

    @pyqtSlot()
    def import_clicked(self):
        self.__loadingEffectImport.start()
        self.__pushButtonBack.hide()
        self.__pushButtonImport.setText("")

    def backup_completed(self):
        self.__loadingEffectBackup.stop()
        self.__pushButtonBack.show()
        QTimer().singleShot(1000, self.re_translate)

    def import_completed(self):
        self.__loadingEffectImport.stop()
        self.__pushButtonBack.show()
        QTimer().singleShot(1000, self.re_translate)

    def set_network_status(self, enabled: bool):
        self.__qnoticeNetwork.setEnabled(enabled)

    def set_network_name(self, text: str):
        self.__labelNetwork.setText(text)
