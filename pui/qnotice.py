from plibs import *


class QNotice(SPGraphics.QuickWidget):
    def __init__(self, parent, fixed_size: QSize, tooltip: SPGraphics.QuickToolTip = None):
        super(QNotice, self).__init__(
            parent=parent, fixed_size=fixed_size
        )

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.childPoint = SPGraphics.QuickWidget(
            self, fixed_size=fixed_size / 2
        )
        self.childPoint.setAttribute(Qt.WA_StyledBackground, True)
        self.childPoint.setObjectName('childPoint')

        self.layout().addWidget(self.childPoint, 0, 0, 1, 1)

        self.__tooltip = tooltip

    def enterEvent(self, event):
        super(QNotice, self).enterEvent(event)

        if self.__tooltip:
            self.__tooltip.exec_(self)

    def leaveEvent(self, event):
        super(QNotice, self).leaveEvent(event)

        if self.__tooltip:
            self.__tooltip.hide()
