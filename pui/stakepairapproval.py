from plibs import *
from pcontroller import translator
from pui import SetupForm, fonts, styles, Size


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__labelTitle = None
        self.__pushButtonApproval = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setContentsMargins(11, 0, 11, 0)
        self.layout().setSpacing(21)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=61, align=Qt.AlignCenter
        )

        self.__pushButtonApproval = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QApplication.backgroundColorAnimate,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonApproval.clicked.connect(self.approval_clicked)

        self.layout().addWidget(self.__labelTitle, alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.__pushButtonApproval, alignment=Qt.AlignHCenter)

        super(UiForm, self).setup()

    def re_translate(self):
        self.__labelTitle.setText(translator("Authorize this staking contract to automate transactions for you"))
        self.__pushButtonApproval.setText(translator("Approval"))

    def re_font(self):
        font = QFont()

        font.setPointSize(fonts.data.size.title)
        font.setBold(True)
        self.__pushButtonApproval.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelTitle.setFont(font)

    @pyqtSlot()
    def approval_clicked(self):
        pass
