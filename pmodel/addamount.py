from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import addamount


class AddAmountModel(addamount.UiForm):
    def __init__(self, parent):
        super(AddAmountModel, self).__init__(parent)

        self.setup()

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
        QTimer().singleShot(5000, self.continue_completed)
        globalmethods.MainModel.setCurrentTab(Tab.TRANSACTION_SENDER, recordable=False)
