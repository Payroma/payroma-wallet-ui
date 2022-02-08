"""
This object is ( Completed )

Requirements:
    - Create standard style with #1 arg of background color changes in menu.css
    - EX:
        #mainWidget,
        #shadowWidget
        {
            background-color: %s;
            border-radius: 10px;
            padding: 10px;
        }

How to Use?
    1- Create a new object
    2- Use setup method
    3- Use add_button method to add menu buttons
"""

from plibs import *
from pui import styles, SetupForm


class UiForm(SPGraphics.QuickMenu, SetupForm):
    def __init__(self, parent, background_color: QColor = styles.data.colors.highlight):
        super(UiForm, self).__init__(
            parent=parent,
            shadow=SPGraphics.QuickShadow(
                color=styles.data.colors.shadow_a60, radius=20, offset=0
            ),
            margin=11
        )

        self.__backgroundColor = background_color
        self.__animation = None
        self.__buttons = []

    def showEvent(self, event):
        super(UiForm, self).showEvent(event)

        self.__animation.start()

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(styles.data.css.menu % self.__backgroundColor.name())

        self.mainWidget.setLayout(QVBoxLayout())
        self.mainWidget.layout().setContentsMargins(0, 9, 0, 9)
        self.mainWidget.layout().setSpacing(0)

        self.__animation = SPGraphics.OpacityMotion(self, SPGraphics.Property.OPACITY)
        self.__animation.temp_show(500)

    def add_button(self, button: QPushButton):
        self.mainWidget.layout().addWidget(button)
        self.__buttons.append(button)

    def get_button(self, index: int):
        return self.__buttons[index]
