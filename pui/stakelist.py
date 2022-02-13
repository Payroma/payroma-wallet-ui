from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelTitle = None
        self.__labelTVL = None
        self.__tabsWidget = None
        self.__pushButtonUpcoming = None
        self.__pushButtonLive = None
        self.__pushButtonEnded = None
        self.__lineWidget = None
        self.__listWidget = None

    def setup(self):
        button_size = QSize(121, 41)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(11, 11, 11, 0)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.STAKE_LIST)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=51, align=Qt.AlignCenter
        )

        self.__labelTVL = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.__labelTVL.setObjectName('labelTVL')

        self.__tabsWidget = SPGraphics.QuickWidget(
            self, fixed_height=51
        )
        self.__tabsWidget.setLayout(QHBoxLayout())
        self.__tabsWidget.layout().setAlignment(Qt.AlignCenter)
        self.__tabsWidget.layout().setContentsMargins(0, 0, 0, 0)

        self.__pushButtonUpcoming = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=self.__button_light_animate,
            start_value=styles.data.colors.disabled_font, end_value=styles.data.colors.highlight
        )
        self.__pushButtonUpcoming.setCheckable(True)
        self.__pushButtonUpcoming.setAutoExclusive(True)
        self.__pushButtonUpcoming.clicked.connect(self.upcoming_clicked)

        self.__pushButtonLive = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=self.__button_light_animate,
            start_value=styles.data.colors.disabled_font, end_value=styles.data.colors.highlight
        )
        self.__pushButtonLive.setCheckable(True)
        self.__pushButtonLive.setAutoExclusive(True)
        self.__pushButtonLive.setChecked(True)
        self.__pushButtonLive.clicked.connect(self.live_clicked)

        self.__pushButtonEnded = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=self.__button_light_animate,
            start_value=styles.data.colors.disabled_font, end_value=styles.data.colors.highlight
        )
        self.__pushButtonEnded.setCheckable(True)
        self.__pushButtonEnded.setAutoExclusive(True)
        self.__pushButtonEnded.clicked.connect(self.ended_clicked)

        self.__lineWidget = SPGraphics.QuickWidget(
            self, fixed_height=1
        )
        self.__lineWidget.setAttribute(Qt.WA_StyledBackground, True)
        self.__lineWidget.setObjectName('lineWidget')

        self.__listWidget = SPGraphics.QuickListWidget(
            self, spacing=10, empty_illustration=images.data.illustrations.no_data
        )
        self.__listWidget.layout().setAlignment(Qt.AlignCenter)
        self.__listWidget.labelIllustration.setAlignment(Qt.AlignHCenter)
        self.__listWidget.labelTitle.setAlignment(Qt.AlignHCenter)
        self.__listWidget.itemClicked.connect(self.item_clicked)

        self.__pushButtonBack.raise_()

        self.layout().addWidget(self.__labelTitle)
        self.layout().addWidget(self.__labelTVL)
        self.layout().addWidget(self.__tabsWidget)
        self.layout().addWidget(self.__lineWidget)
        self.layout().addWidget(self.__listWidget)
        self.__tabsWidget.layout().addWidget(self.__pushButtonUpcoming)
        self.__tabsWidget.layout().addWidget(self.__pushButtonLive)
        self.__tabsWidget.layout().addWidget(self.__pushButtonEnded)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.stakelist)
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))

    def re_translate(self):
        self.__labelTitle.setText(translator("Just stake some tokens to earn.\nHigh APR, low risk."))
        self.__pushButtonUpcoming.setText(translator("Upcoming"))
        self.__pushButtonLive.setText(translator("Live"))
        self.__pushButtonEnded.setText(translator("Ended"))
        self.__listWidget.labelTitle.setText(translator("No pairs has been added yet!"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__labelTitle.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__pushButtonUpcoming.setFont(font)
        self.__pushButtonLive.setFont(font)
        self.__pushButtonEnded.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        font.setBold(False)
        self.__labelTVL.setFont(font)

        font.setFamily(fonts.data.family.black)
        self.__listWidget.labelTitle.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot()
    def upcoming_clicked(self):
        pass

    @pyqtSlot()
    def live_clicked(self):
        pass

    @pyqtSlot()
    def ended_clicked(self):
        pass

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem) -> QWidget:
        return self.__listWidget.itemWidget(item)

    def add_item(self, item: QListWidgetItem):
        self.__listWidget.add_quick_item(item)

    def set_tvl(self, text: str, symbol: str):
        self.__labelTVL.setText("TVL: {} {}".format(text, symbol))

    def reset(self):
        self.__listWidget.clear()

    def __button_light_animate(self, value: QColor):
        sender = self.sender()
        if not isinstance(sender, QVariantAnimation):
            return

        css = '''
        QPushButton {
            color: rgba%s;
        }
        QPushButton:checked
        {
            color: %s;
        }
        ''' % (
            str(value.getRgb()), styles.data.colors.highlight.name()
        )
        sender.parent().setStyleSheet(css)
