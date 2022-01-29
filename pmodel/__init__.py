"""
- pmodel is a organizer for pui and pcontroller
- pmodel is the starting point of the application

WARRING: Don't import pmodel from another object
"""

from plibs import QMessageBox, QFont, SPGraphics, SPInputmanager
from pheader import *
import pcontroller
import pui


def input_manager_setup():
    SPInputmanager.Setup.set_icons(
        eye_show=pui.images.data.icons.changeable.eye_visible21,
        eye_hide=pui.images.data.icons.changeable.eye_invisible21
    )


def graphics_setup():
    SPGraphics.Setup.set_icons(
        eye_show=pui.images.data.icons.changeable.eye_visible21,
        eye_hide=pui.images.data.icons.changeable.eye_invisible21,
        enter_button=pui.images.data.icons.arrow_right21,
        close_button=pui.images.data.icons.changeable.close21,
        information_state=pui.images.data.icons.info41,
        warning_state=pui.images.data.icons.warning41,
        success_state=pui.images.data.icons.ok41,
        failed_state=pui.images.data.icons.failed41
    )

    SPGraphics.Setup.set_colors(
        font=pui.styles.data.colors.font.name(),
        information=pui.styles.data.colors.white.name(),
        warning=pui.styles.data.colors.warning.name(),
        success=pui.styles.data.colors.positive.name(),
        failed=pui.styles.data.colors.negative.name()
    )

    title_font = QFont(pui.fonts.data.family.normal, pui.fonts.data.size.title)
    title_font.setBold(True)
    title_font.setItalic(True)
    title_text = "{} {}".format(SOFTWARE_NAME, "Message")

    SPGraphics.Setup.set_message_box_details(
        SOFTWARE_NAME, title_text, title_font, pui.styles.data.css.messagebox
    )


def launch():
    """Application boot"""

    if IS_WINDOWS:
        pcontroller.anti_duplicate_process(stop=True)

    Global.logsSystem = pcontroller.LogsSystem()

    try:
        input_manager_setup()
        graphics_setup()
        Global.settings = pcontroller.settings_load()

        from pmodel.main import MainModel
        main = MainModel(parent=None)
        main.show()
        Global.kernel.exec_()

    except Exception as issue:
        Global.logsSystem.save(
            Global.logsSystem.issue(issue)
        )

        message = QMessageBox()
        message.setIcon(QMessageBox.Warning)
        message.setWindowTitle("{} issue message".format(SOFTWARE_NAME))
        message.setText("Issue Type : {}\nIssue Text : {}".format(type(issue), str(issue)))
        message.setInformativeText(
            "Please contact us to solve the problem\n{}".format(Website.PAYROMA)
        )
        message.setStandardButtons(QMessageBox.Close)
        message.exec_()
