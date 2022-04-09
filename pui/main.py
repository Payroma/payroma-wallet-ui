from plibs import *
from pheader import *
from pui import AppReForm, SetupForm, fonts, images, styles, Size, header, footer, tooltip

Size.defaultMainWidget = QSize(450, 660)
Size.minimumMainWidget = QSize(450, 600)


class UiForm(SPGraphics.QuickMainWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(
            parent=parent,
            shadow=SPGraphics.QuickShadow(
                color=styles.data.colors.shadow_a60, radius=20, offset=0
            ),
            margin=11
        )

        self.__headerWidget = None
        self.__tabWidget = None
        self.__footerWidget = None

    def setup(self):
        self.default_theme()
        super(UiForm, self).setup()

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowIcon(QIcon(images.data.brands.brand))
        self.setWindowTitle(SOFTWARE_NAME)
        self.setMinimumSize(Size.minimumMainWidget)
        self.resize(Size.defaultMainWidget)

        self.mainWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.mainWidget.setFocusPolicy(Qt.ClickFocus)
        self.mainWidget.setLayout(QGridLayout())
        self.mainWidget.layout().setContentsMargins(0, 0, 0, 0)
        self.mainWidget.layout().setSpacing(0)

        QApplication.toolTip = tooltip.UiForm(self)
        QApplication.toolTip.setup()

        QApplication.backgroundColorAnimate = self.__background_color_animate
        QApplication.textColorAnimate = self.__text_color_animate

        self.__headerWidget = header.UiForm(self)
        self.__headerWidget.setup()
        self.__headerWidget.pushButtonBack.clicked.connect(self.back_clicked)
        self.__headerWidget.pushButtonHome.clicked.connect(self.home_clicked)
        self.__headerWidget.pushButtonSettings.clicked.connect(self.settings_clicked)
        self.__headerWidget.pushButtonMinimize.clicked.connect(self.minimize_clicked)
        self.__headerWidget.pushButtonExit.clicked.connect(self.exit_clicked)

        self.__tabWidget = QTabWidget(self)
        self.__tabWidget.findChild(QTabBar).hide()
        self.__tabWidget.currentChanged.connect(self.__tab_changed)

        self.__footerWidget = footer.UiForm(self)
        self.__footerWidget.setup()
        self.__footerWidget.pushButtonInvest.clicked.connect(self.invest_clicked)

        self.mainWidget.layout().addWidget(self.__headerWidget, 0, 0, 1, 1, Qt.AlignTop)
        self.mainWidget.layout().addWidget(self.__tabWidget, 1, 0, 1, 1)
        self.mainWidget.layout().addWidget(self.__footerWidget, 2, 0, 1, 1, Qt.AlignBottom)

    def re_style(self):
        palette = QPalette()
        palette.setColor(QPalette.Highlight, styles.data.colors.positive)
        palette.setColor(QPalette.Light, Qt.gray)
        palette.setColor(QPalette.Dark, styles.data.colors.disabled)
        Global.kernel.setPalette(palette)

        QApplication.quickNotification = SPGraphics.QuickNotification(
            self, stylesheet=styles.data.css.notices, top_margin=11, right_margin=11
        )
        QApplication.quickNotification.setFixedHeight(121)

        SPGraphics.Setup.set_colors(
            font=styles.data.colors.font.name(),
            information=styles.data.colors.white.name(),
            warning=styles.data.colors.warning.name(),
            success=styles.data.colors.positive.name(),
            failed=styles.data.colors.negative.name()
        )

        SPGraphics._STYLESHEET = styles.data.css.messagebox

        self.setStyleSheet(styles.data.css.main)

    def re_font(self):
        font = QFont(fonts.data.family.normal, fonts.data.size.normal)
        Global.kernel.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def home_clicked(self):
        pass

    @pyqtSlot()
    def settings_clicked(self):
        pass

    @pyqtSlot()
    def minimize_clicked(self):
        pass

    @pyqtSlot()
    def exit_clicked(self):
        pass

    @pyqtSlot()
    def invest_clicked(self):
        pass

    def default_theme(self):
        pass

    @pyqtSlot(int)
    def __tab_changed(self, index: int):
        widget = self.__tabWidget.currentWidget()
        self.__tabTransMotion = SPGraphics.OpacityMotion(widget)
        self.__tabTransMotion.temp_show(
            duration=500, finished=lambda: widget.setGraphicsEffect(None)
        ).start()

        if index > 0 and self.__headerWidget.pushButtonBack.isHidden():
            self.__headerWidget.back_button_visible(True)
        elif index < 1 and self.__headerWidget.pushButtonBack.isVisible():
            self.__headerWidget.back_button_visible(False)

    def add_tab(self, model: QWidget, name: str):
        self.__tabWidget.addTab(model, name)

    def set_current_tab(self, name: str):
        widget = self.__tabWidget.findChild(QWidget, name)
        self.__tabWidget.setCurrentWidget(widget)

    @staticmethod
    def set_theme_mode(name: str = ''):
        styles.update(name)
        images.update(name)
        AppReForm.re_style_all()

    def __background_color_animate(self, value: QColor):
        sender = self.sender()
        if not isinstance(sender, QVariantAnimation):
            return

        css = '''
        QWidget {
            background-color: rgba%s;
        }
        QWidget::disabled {
            color: %s;
            background-color: %s;
        }
        ''' % (
            str(value.getRgb()), styles.data.colors.disabled_font.name(),
            styles.data.colors.disabled.name()
        )
        sender.parent().setStyleSheet(css)

    def __text_color_animate(self, value: QColor):
        sender = self.sender()
        if not isinstance(sender, QVariantAnimation):
            return

        css = '''
        QWidget {
            color: rgba%s;
        }
        QWidget::disabled {
            color: %s;
        }
        ''' % (str(value.getRgb()), styles.data.colors.disabled_font.name())
        sender.parent().setStyleSheet(css)
