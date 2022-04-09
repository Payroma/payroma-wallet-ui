from plibs import *
from pcontroller import event
from pui import tokenslist
from pmodel import tokenitem


class TokensListModel(tokenslist.UiForm, event.EventForm):
    def __init__(self, parent):
        super(TokensListModel, self).__init__(parent)

        self.setup()
        self.events_listening()

    def token_edited_event(self):
        self.refresh()

    def network_changed_event(self, name: str, status: bool):
        self.refresh()

    def refresh(self):
        self.reset()

        # Test
        tokens = {
            'Ethereum Token': {'balance': '100', 'symbol': 'ETH'},
            'Wrapped BNB': {'balance': '10.456789', 'symbol': 'BNB'},
            'BTCB Token': {'balance': '7', 'symbol': 'BTC'},
            'BSC-USD': {'balance': '547,544', 'symbol': 'USDT'},
            'XRP Token': {'balance': '1,244,650', 'symbol': 'XRP'}
        }
        for name, info in tokens.items():
            item = tokenitem.TokenItem(self)
            item.set_name(name)
            item.set_balance(info['balance'])
            item.set_symbol(info['symbol'])
            self.add_item(item)
            if name == 'Ethereum Token':
                item.set_master()
