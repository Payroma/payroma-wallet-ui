from plibs import *
from pheader import *
from pcontroller import event
from pui import historylist
from pmodel import historyitem


class HistoryListModel(historylist.UiForm):
    def __init__(self, parent):
        super(HistoryListModel, self).__init__(parent)

        self.setup()

        # Test
        transactions = [
            {
                'function': 'Transfer',
                'status': historyitem.HistoryItem.PENDING,
                'amount': '100,000',
                'symbol': 'BUSD',
                'address': '0x0000000000000000000000000000000000000001',
                'date': 'Tue Mar  1 14:31:33 2022'
            },
            {
                'function': 'Approval',
                'status': historyitem.HistoryItem.SUCCESS,
                'amount': 'Unlimited',
                'symbol': 'USDT',
                'address': '0x0000000000000000000000000000000000000001',
                'date': 'Tue Mar  1 14:31:33 2022'
            },
            {
                'function': 'Deposit',
                'status': historyitem.HistoryItem.FAILED,
                'amount': '1,000',
                'symbol': 'PYA',
                'address': '0x0000000000000000000000000000000000000001',
                'date': 'Tue Mar  1 14:31:33 2022'
            }
        ]
        for transaction in transactions:
            item = historyitem.HistoryItem(self)
            item.set_icon(transaction['symbol'])
            item.set_function_name(transaction['function'])
            item.set_status(transaction['status'])
            item.set_balance(transaction['amount'], transaction['symbol'])
            item.set_address(transaction['address'])
            item.set_date(transaction['date'])
            self.add_item(item)
