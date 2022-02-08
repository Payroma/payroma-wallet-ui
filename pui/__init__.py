"""
- pui is a GUI object

WARRING: Only pmodel can manage it
"""

from plibs import QSize
import pui.styles as __styles
import pui.images as __images
import pui.fonts as __fonts


class Size:
    s16 = QSize(16, 16)
    s21 = QSize(21, 21)
    s24 = QSize(24, 24)
    s31 = QSize(31, 31)
    s41 = QSize(41, 41)
    s51 = QSize(51, 51)
    s61 = QSize(61, 61)
    s71 = QSize(71, 71)
    s81 = QSize(81, 81)
    s91 = QSize(91, 91)
    s100 = QSize(100, 100)
    default = QSize(301, 51)
    defaultMainWidget = None
    minimumMainWidget = None
    maximumMainWidget = None


class AppReForm:
    re_translate_list = []
    re_style_list = []
    re_font_list = []
    re_license_list = []

    @staticmethod
    def __re_call(array: list):
        for call in array:
            try:
                call()

            except RuntimeError:
                continue

    @staticmethod
    def re_translate_all():
        AppReForm.__re_call(AppReForm.re_translate_list)

    @staticmethod
    def re_style_all():
        AppReForm.__re_call(AppReForm.re_style_list)

    @staticmethod
    def re_font_all():
        AppReForm.__re_call(AppReForm.re_font_list)

    @staticmethod
    def re_license_all():
        AppReForm.__re_call(AppReForm.re_license_list)


class SetupForm:
    def setup(self):
        """Setup The form contents"""

        AppReForm.re_translate_list.append(self.re_translate)
        AppReForm.re_style_list.append(self.re_style)
        AppReForm.re_font_list.append(self.re_font)
        AppReForm.re_license_list.append(self.re_license)

        self.re_translate()
        self.re_style()
        self.re_font()
        self.re_license()

    def re_translate(self):
        """Translate the contents"""

    def re_style(self):
        """Update the application style"""

    def re_font(self):
        """Update the application font"""

    def re_license(self):
        """Update the application license"""
