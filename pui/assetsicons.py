from plibs import os, json, QPixmap
from pheader import Dir


def __coins_loader() -> dict:
    with open(os.path.join(Dir.ASSETS, 'coins.json'), 'r') as file:
        return json.load(file)


__coinIcons = __coins_loader()


def get_asset_icon(symbol: str) -> QPixmap:
    unknown = os.path.join(
        os.path.join(Dir.ASSETS, 'coins'), 'unknown.png'
    )
    return QPixmap(__coinIcons.get(symbol, unknown))
