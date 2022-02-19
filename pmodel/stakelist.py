from plibs import *
from pheader import *
from pui import stakelist
from pmodel import stakeitem


class StakeListModel(stakelist.UiForm):
    def __init__(self, parent):
        super(StakeListModel, self).__init__(parent)

        self.setup()

        # Test
        self.set_tvl("4,561,012", "PYA")
        data = {
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f6': {
                'earnSymbol': 'PYA',
                'stakeSymbol': 'PYA',
                'apy': '189%',
                'totalStaked': '3,544,796',
                'block': '292,000',
                'lock': True
            },
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f7': {
                'earnSymbol': 'USDT',
                'stakeSymbol': 'PYA',
                'apy': '14%',
                'totalStaked': '234,155',
                'block': '292,000',
                'lock': True
            },
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f8': {
                'earnSymbol': 'BUSD',
                'stakeSymbol': 'PYA',
                'apy': '9%',
                'totalStaked': '688,171',
                'block': '292,000',
                'lock': True
            },
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f9': {
                'earnSymbol': 'BUSD',
                'stakeSymbol': 'USDT',
                'apy': '4.6%',
                'totalStaked': '1,326,654',
                'block': '292,000',
                'lock': False
            },
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f0': {
                'earnSymbol': 'BTC',
                'stakeSymbol': 'USDC',
                'apy': '2.1%',
                'totalStaked': '34,112',
                'block': '292,000',
                'lock': False
            }
        }

        for contract, info in data.items():
            item = stakeitem.StakeItem(self)
            item.set_pair_symbols(info['stakeSymbol'], info['earnSymbol'])
            item.set_apy(info['apy'])
            item.set_block_number(info['block'])
            item.set_total_staked(info['totalStaked'], info['stakeSymbol'])
            item.set_duration_type(info['lock'])
            self.add_item(item)

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)
