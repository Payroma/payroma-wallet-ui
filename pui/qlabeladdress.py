from plibs import *
from pcontroller import translator, clipboard
from pui import Size


class QLabelAddress(SPGraphics.QuickWidget):
    def __init__(
            self, parent=None,
            text: str = None,
            fixed_width: int = None,
            fixed_height: int = None,
            fixed_size: QSize = None,
            value_changed: callable = None,
            start_value: object = None,
            end_value: object = None,
            duration: int = 300,
            tooltip: SPGraphics.QuickToolTip = None,
            copy_tooltip: SPGraphics.QuickToolTip = None
    ):
        super(QLabelAddress, self).__init__(
            parent=parent, fixed_width=fixed_width, fixed_height=fixed_height,
            fixed_size=fixed_size, value_changed=value_changed,
            start_value=start_value, end_value=end_value, duration=duration,
        )

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.label = SPGraphics.QuickLabel(
            self, tooltip=tooltip
        )
        self.label.setWordWrap(False)
        self.label.setObjectName('labelAddress')

        self.__pushButton = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s21, tooltip=copy_tooltip
        )
        self.__pushButton.clicked.connect(self.__clicked)

        self.layout().addWidget(self.label)
        self.layout().addWidget(self.__pushButton, alignment=Qt.AlignRight)

        self.__text = None

        if text:
            self.setText(text)

    @pyqtSlot()
    def __clicked(self):
        clipboard(self.text())
        QApplication.quickNotification.successfully(translator("Copied Successfully"))

    def clear(self):
        self.__text = ''
        self.label.clear()

    def text(self) -> str:
        return self.__text

    def setText(self, text: str, is_ellipsis: bool = True):
        self.__text = text
        self.label.setText(text)

        if is_ellipsis:
            SPGraphics.text_ellipsis(self.label, Qt.ElideMiddle)

    def setIcon(self, icon: QIcon):
        self.__pushButton.setIcon(icon)

    def setFont(self, font: QFont):
        self.label.setFont(font)
