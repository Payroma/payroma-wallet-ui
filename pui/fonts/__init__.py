"""
- This section for fonts
- Usable for any object
"""

from plibs import os, QFontDatabase
from pcontroller import Struct, dict_merge
from pui.fonts import head


DIR = os.path.abspath('pui/fonts')
CURRENT_TEMPLATE = None


class data:
    size = None


def load():
    """Loading the fonts list to QFontDatabase"""

    for f in os.listdir(DIR):
        if f.endswith('.ttf'):
            QFontDatabase().addApplicationFont(os.path.join(DIR, f))


def update(template: str = None):
    """
    Switch between templates just by template name, you can access from data class

    Note: Original data doesn't changed, the changes will be in memory only
    """

    global CURRENT_TEMPLATE

    CURRENT_TEMPLATE = template
    cache = {}

    if template:
        merge = dict(dict_merge(head.DEFAULT, head.TEMPLATES[template]))
        cache.update(merge)

    else:
        cache.update(head.DEFAULT)

    Struct(parent=data, data=cache)


load()
update()

__all__ = [
    'data', 'update'
]
