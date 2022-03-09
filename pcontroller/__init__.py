"""
- Execution object
- Usable for any object
"""

from plibs import *
from pheader import *


class SignalsThread(QObject):
    normalSignal = pyqtSignal()
    boolSignal = pyqtSignal(bool)
    intSignal = pyqtSignal(int)
    floatSignal = pyqtSignal(float)
    strSignal = pyqtSignal(str)
    listSignal = pyqtSignal(list)
    dictSignal = pyqtSignal(dict)

    # // Set other signals here
    # ...


class ThreadingArea(QThread):
    def __init__(self, core, parent=None):
        super(ThreadingArea, self).__init__(parent)

        self.core = core
        self.signal = SignalsThread()

        self.__issue = None

    @property
    def issue(self):
        value = self.__issue
        self.__issue = None

        return value

    @issue.setter
    def issue(self, value):
        self.__issue = value

    def run(self):
        try:
            self.core()

        except Exception as error:
            self.issue = error
            (_type, _value, _traceback) = sys.exc_info()
            sys.excepthook(_type, _value, _traceback)


class Struct:
    def __init__(self, data, parent=None):

        self.__parent = (parent if parent else self)
        for key, value in data.items():
            self.__convert(key, value)

    def __convert(self, key, value):
        if isinstance(value, (list, tuple)):
            setattr(self.__parent, key, [Struct(i) if isinstance(i, dict) else i for i in value])

        else:
            setattr(self.__parent, key, Struct(value) if isinstance(value, dict) else value)


class Language:
    CURRENT_LANGUAGE = None
    __languages = {}

    for f in os.listdir(Dir.LANGUAGES):
        if f.endswith('.qm'):
            __languages.update({
                f.split('.')[0]: os.path.join(Dir.LANGUAGES, f)
            })

    @staticmethod
    def change(lang_name: str):
        Language.CURRENT_LANGUAGE = lang_name
        Global.translator.load(Language.__languages[lang_name])
        Global.kernel.instance().installTranslator(Global.translator)

    @staticmethod
    def default():
        Language.CURRENT_LANGUAGE = None
        Global.kernel.instance().removeTranslator(Global.translator)


class LogsSystem:
    def __init__(self):
        self.__formSyntax = '{:16} : {}\n'
        self.__formEnd = '=' * 30 + '\n'

    def issue(self, issue) -> tuple[str, str]:
        """
        Issue is just template function
        return: str, str
        """

        issue_type = self.__formSyntax.format("Issue Type", str(type(issue)))
        issue_message = self.__formSyntax.format("Issue Message", str(issue))
        form = issue_type + issue_message
        path = os.path.join(Dir.LOGS, "issue_event.txt")

        return form, path

    def save(self, log_type: tuple):
        form, path = log_type
        current_time = self.__formSyntax.format("Time", time.ctime())

        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'a') as file:
            file.write(current_time + form + self.__formEnd)


def dict_merge(dict1, dict2):
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield k, dict(dict_merge(dict1[k], dict2[k]))

            else:
                # If one of the values is not a dict, you can't continue merging it.
                # Value from second dict overrides one in first and we move on.
                yield k, dict2[k]
                # Alternatively, replace this with exception raiser to alert you of value conflicts

        elif k in dict1:
            yield k, dict1[k]

        else:
            yield k, dict2[k]


def translator(text: str) -> str:
    """
    Translate the messages text
    :return: str
    """

    return Global.kernel.translate('Form', text)


def anti_duplicate_process(stop: bool = False):
    if stop:
        return

    executable = Global.processExecutable.name()
    count = 0

    for process in psutil.process_iter():
        try:
            if process.name() == executable:
                count += 1

                if count >= 2:
                    sys.exit()

        except psutil.AccessDenied:
            continue


def settings_load() -> SPSettings.SettingsManager:
    """
    :exception FILE_SUPPORT_ERROR
    :exception SPCrypto.FILE_SUPPORT_ERROR
    :exception SPCrypto.PERMISSION_ERROR
    :exception pickle.UnpicklingError
    :exception MemoryError, PermissionError
    return: SPSettings.SettingsManager
    """

    # Memory setup
    config = SPSettings.FileConfig()
    config.update(file='settings', extension='config')
    config.setup()

    # Default configuration and load
    settings = SPSettings.SettingsManager(
        config, SPSecurity.secure_string(SECRET_VALUE).decode()
    )

    # Set settings options here
    # ...

    settings.load()

    return settings


def url_open(url: str):
    if not url:
        return

    _url = QUrl(url)
    QDesktopServices().openUrl(_url)


def clipboard(text: str):
    if not text:
        return

    clip = Global.kernel.clipboard()
    clip.clear(mode=clip.Clipboard)
    clip.setText(text, mode=clip.Clipboard)


def to_qr_code(text: str, size: QSize) -> QPixmap:
    from pui import styles
    image_file = io.BytesIO()

    qr_generator = pyqrcode.create(text, error='L', mode='binary')
    qr_generator.png(
        image_file, scale=7, module_color=styles.data.colors.font.getRgb(),
        background=styles.data.colors.background.getRgb()
    )

    image = QImage.fromData(image_file.getvalue(), 'png').scaled(size, Qt.KeepAspectRatio)

    return QPixmap.fromImage(image)
