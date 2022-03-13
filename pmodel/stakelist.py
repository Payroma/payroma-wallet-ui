from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import stakelist
from pmodel import stakeitem


class StakeListModel(stakelist.UiForm):
    def __init__(self, parent):
        super(StakeListModel, self).__init__(parent)

        self.setup()
        self.reset()

        # Test
        self.set_data("4,561,012", "PYA")
        data = {
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f6': {
                'earnSymbol': 'PYA',
                'stakeSymbol': 'PYA',
                'apy': 189,
                'totalStaked': '3,544,796',
                'block': 192000,
                'lock': True,
                'balance': '10,000,000',
                'staked': '1,000,000',
                'claim': '3,000'
            },
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f7': {
                'earnSymbol': 'USDT',
                'stakeSymbol': 'PYA',
                'apy': 14,
                'totalStaked': '234,155',
                'block': 292000,
                'lock': True,
                'balance': '10,000,000',
                'staked': '100,000',
                'claim': '300'
            },
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f8': {
                'earnSymbol': 'BUSD',
                'stakeSymbol': 'PYA',
                'apy': 9,
                'totalStaked': '688,171',
                'block': 392000,
                'lock': True,
                'balance': '10,000,000',
                'staked': '0',
                'claim': '0'
            },
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f9': {
                'earnSymbol': 'BUSD',
                'stakeSymbol': 'USDT',
                'apy': 4.6,
                'totalStaked': '1,326,654',
                'block': 592000,
                'lock': False,
                'balance': '547,544',
                'staked': '100,000',
                'claim': '1,000'
            },
            '0x8c5e85747b529360bd90a9dd5d8405c4f91c53f0': {
                'earnSymbol': 'BTC',
                'stakeSymbol': 'USDC',
                'apy': 2.1,
                'totalStaked': '34,112',
                'block': 2092000,
                'lock': False,
                'balance': '100,000',
                'staked': '10,000',
                'claim': '0.006'
            }
        }

        for contract, info in data.items():
            item = stakeitem.StakeItem(self)
            item.set_pair_symbols(info['stakeSymbol'], info['earnSymbol'])
            item.set_apy(info['apy'])
            item.set_duration_type(info['lock'])
            item.interface = info
            self.add_item(item)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem):
        widget = super(StakeListModel, self).item_clicked(item)
        globalmethods.StakePairModel.setData(
            'Ends in',
            widget.interface['block'],
            widget.interface['totalStaked'],
            widget.interface['stakeSymbol'],
            widget.interface['earnSymbol']
        )
        globalmethods.StakePairAmountModel.setData(
            widget.interface['balance'],
            widget.interface['staked'],
            widget.interface['claim'],
            widget.interface['stakeSymbol'],
            widget.interface['earnSymbol']
        )
        globalmethods.MainModel.setCurrentTab(Tab.STAKE_PAIR)
