"""
- This section for images
- Usable for any object
"""

try:
    import pui.images.images_rc
except ModuleNotFoundError:
    pass
from pcontroller import Struct, dict_merge
from pui.images import head


CURRENT_TEMPLATE = None


class data:
    pass


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


update()


__all__ = [
    'data', 'update'
]
