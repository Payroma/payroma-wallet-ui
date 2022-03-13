from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles


class HeaderWidget(QWidget):
    def __init__(self, parent):
        super(HeaderWidget, self).__init__(parent, flags=Qt.SubWindow)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignHCenter)
        self.layout().setContentsMargins(11, 11, 11, 11)
        self.layout().setSpacing(11)

        self.labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=51, align=Qt.AlignCenter
        )

        self.labelTVL = SPGraphics.QuickLabel(
            self, fixed_height=21, align=Qt.AlignCenter
        )
        self.labelTVL.setWordWrap(False)
        self.labelTVL.setObjectName('labelTVL')

        self.layout().addWidget(self.labelTitle)
        self.layout().addWidget(self.labelTVL)


class TabsWidget(QWidget):
    def __init__(self, parent):
        super(TabsWidget, self).__init__(parent, flags=Qt.SubWindow)

        button_size = QSize(121, 41)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QHBoxLayout())
        self.layout().setAlignment(Qt.AlignHCenter)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(11)

        self.pushButtonUpcoming = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=self.__button_light_animate,
            start_value=styles.data.colors.font_description, end_value=styles.data.colors.highlight
        )
        self.pushButtonUpcoming.setCheckable(True)
        self.pushButtonUpcoming.setAutoExclusive(True)

        self.pushButtonLive = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=self.__button_light_animate,
            start_value=styles.data.colors.font_description, end_value=styles.data.colors.highlight
        )
        self.pushButtonLive.setCheckable(True)
        self.pushButtonLive.setAutoExclusive(True)

        self.pushButtonEnded = SPGraphics.QuickPushButton(
            self, fixed_size=button_size, value_changed=self.__button_light_animate,
            start_value=styles.data.colors.font_description, end_value=styles.data.colors.highlight
        )
        self.pushButtonEnded.setCheckable(True)
        self.pushButtonEnded.setAutoExclusive(True)

        self.layout().addWidget(self.pushButtonUpcoming)
        self.layout().addWidget(self.pushButtonLive)
        self.layout().addWidget(self.pushButtonEnded)

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
        ''' % (str(value.getRgb()), styles.data.colors.highlight.name())
        sender.parent().setStyleSheet(css)


class ListWidget(SPGraphics.QuickListWidget):
    def __init__(self, parent):
        super(ListWidget, self).__init__(
            parent, spacing=10, empty_illustration=images.data.illustrations.no_data
        )

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.layout().setContentsMargins(21, 0, 21, 0)
        self.layout().setAlignment(Qt.AlignVCenter)
        self.labelIllustration.setAlignment(Qt.AlignHCenter)
        self.labelTitle.setAlignment(Qt.AlignHCenter)


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__headerWidget = None
        self.__tabsWidget = None
        self.__listWidget = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.setObjectName(Tab.STAKE_LIST)

        self.__headerWidget = HeaderWidget(self)

        self.__tabsWidget = TabsWidget(self)
        self.__tabsWidget.pushButtonUpcoming.clicked.connect(self.upcoming_clicked)
        self.__tabsWidget.pushButtonLive.clicked.connect(self.live_clicked)
        self.__tabsWidget.pushButtonEnded.clicked.connect(self.ended_clicked)

        self.__listWidget = ListWidget(self)
        self.__listWidget.itemClicked.connect(self.item_clicked)

        self.layout().addWidget(self.__headerWidget)
        self.layout().addWidget(self.__listWidget)
        self.__headerWidget.layout().addWidget(self.__tabsWidget)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.stakelist)

    def re_translate(self):
        self.__headerWidget.labelTitle.setText(
            translator("Just stake some tokens to earn.\nHigh APR, low risk.")
        )
        self.__tabsWidget.pushButtonUpcoming.setText(translator("Upcoming"))
        self.__tabsWidget.pushButtonLive.setText(translator("Live"))
        self.__tabsWidget.pushButtonEnded.setText(translator("Ended"))
        self.__listWidget.labelTitle.setText(translator("No pairs has been added yet!"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.average)
        font.setBold(True)
        self.__headerWidget.labelTitle.setFont(font)

        font.setPointSize(fonts.data.size.title)
        self.__tabsWidget.pushButtonUpcoming.setFont(font)
        self.__tabsWidget.pushButtonLive.setFont(font)
        self.__tabsWidget.pushButtonEnded.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        font.setBold(False)
        self.__headerWidget.labelTVL.setFont(font)

        font.setFamily(fonts.data.family.black)
        self.__listWidget.labelTitle.setFont(font)

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

    def set_data(self, tvl: str, symbol: str):
        self.update_tvl(tvl, symbol)

    def update_tvl(self, tvl: str, symbol: str):
        self.__headerWidget.labelTVL.setText("TVL: {} {}".format(tvl, symbol))

    def reset(self):
        self.__headerWidget.labelTVL.clear()
        self.__listWidget.clear()
        self.__tabsWidget.pushButtonLive.click()
