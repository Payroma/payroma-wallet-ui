"""
- This section for colors and css code
- Usable for any object
"""

from plibs import os
from pcontroller import Struct, dict_merge
from pui.styles import head


DIR = os.path.abspath('pui/styles')
CURRENT_TEMPLATE = None
CSS = {}


class data:
    pass


def css_compiler(colors_rules: dict, stylesheet: str):
    """
    Apply the colors rule on the stylesheet
    Expected rules like this {str: QColor}
    Note: Only rgba supported

    :return: str
    """

    for name, color in colors_rules.items():

        if name in stylesheet:
            stylesheet = stylesheet.replace(f'@{name};', f'rgba{color.getRgb()};')
            stylesheet = stylesheet.replace(f'@{name} ', f'rgba{color.getRgb()} ')
            stylesheet = stylesheet.replace(f'@{name}\n', f'rgba{color.getRgb()}\n')

    return stylesheet


def load():
    """Loading and store css code"""

    for f in os.listdir(DIR):
        if f.endswith('.css'):
            name = f.split('.')[0]
            contents = open(os.path.join(DIR, f), 'r').read()
            CSS.update({name: contents})


def update(template: str = None):
    """
    Switch between templates just by template name, you can access from data class

    Note: Original data doesn't changed, the changes will be in memory only
    """

    global CURRENT_TEMPLATE

    CURRENT_TEMPLATE = template
    cache = {
        'colors': {},
        'css': {}
    }

    if template:
        merge = dict(dict_merge(head.DEFAULT, head.TEMPLATES[template]))
        cache.update({'colors': merge})

    else:
        cache.update({'colors': head.DEFAULT})

    for name, css in CSS.items():
        cache['css'].update({
            name: css_compiler(cache['colors'], css)
        })

    Struct(parent=data, data=cache)


load()
update()

__all__ = [
    'data', 'update'
]
