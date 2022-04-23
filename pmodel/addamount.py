from plibs import *
from pheader import *
from pcontroller import event
from pui import addamount


class AddAmountModel(addamount.UiForm, event.EventForm):
    def __init__(self, parent):
        super(AddAmountModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Variables
        self.__senderAddress = None
        self.__recipientAddress = None

        # Test
        self.__currentTokenIndex = 0
        self.__tokens = {
            0: {'balance': '100', 'symbol': 'ETH'},
            1: {'balance': '10.456789', 'symbol': 'BNB'},
            2: {'balance': '7', 'symbol': 'BTC'},
            3: {'balance': '547,544', 'symbol': 'USDT'},
            4: {'balance': '1,244,650', 'symbol': 'XRP'}
        }
        for name, info in self.__tokens.items():
            self.add_item(info['symbol'])

    def wallet_changed_event(self, username: str, address: str):
        self.__senderAddress = address

    def withdraw_address_changed_event(self, address: str):
        self.__recipientAddress = address

    @pyqtSlot(int)
    def token_changed(self, index: int):
        self.__currentTokenIndex = index if index >= 0 else 0
        balance = self.__tokens[self.__currentTokenIndex]['balance']
        super(AddAmountModel, self).token_changed(index, balance)

    @pyqtSlot(str)
    def amount_changed(self, text: str):
        balance = self.__tokens[self.__currentTokenIndex]['balance'].replace(',', '')
        valid = True if float(text or 0) <= float(balance) else False
        super(AddAmountModel, self).amount_changed(text, valid)

    @pyqtSlot()
    def max_clicked(self):
        balance = self.__tokens[self.__currentTokenIndex]['balance'].replace(',', '')
        super(AddAmountModel, self).max_clicked(balance)

    @pyqtSlot()
    def continue_clicked(self):
        super(AddAmountModel, self).continue_clicked()
        QTimer().singleShot(3000, self.continue_completed)

    def continue_completed(self):
        super(AddAmountModel, self).continue_completed()
        event.transactionSenderChanged.notify(
            tx={
                "from": self.__senderAddress,
                "to": self.__recipientAddress,
                "value": 887715290264793000,
                "data": "",
                "nonce": 2,
                "chainId": 3,
                "maxPriorityFeePerGas": 2500000000,
                "maxFeePerGas": 3750114223,
                "gas": 21000
            },
            details={
                'abi': {},
                'args': {
                    'recipient': self.__recipientAddress,
                    'amount': self.get_amount_text()
                },
                'data': '',
            },
            symbol=self.__tokens[self.__currentTokenIndex]['symbol']
        )
        event.mainTabChanged.notify(tab=Tab.TRANSACTION_SENDER, recordable=False)
