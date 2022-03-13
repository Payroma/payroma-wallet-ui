from plibs import *
from pheader import *
from pcontroller import globalmethods
from pui import transactionsender


class TransactionSenderModel(transactionsender.UiForm):
    def __init__(self, parent):
        super(TransactionSenderModel, self).__init__(parent)

        self.setup()

        # Test
        amount = "547,544"
        estimated_gas = "0.00012"
        total = '{:,}'.format(float(amount.replace(',', '')) + float(estimated_gas))
        self.set_data(
            network="Binance Smart Chain",
            function="Transfer",
            address="0x0000000000000000000000000000000000000001",
            amount=amount,
            symbol="USDT",
            estimated_gas=estimated_gas,
            max_fee=estimated_gas,
            total=total,
            max_amount=total
        )

    @pyqtSlot()
    def network_clicked(self):
        globalmethods.MainModel.setCurrentTab(Tab.NETWORKS_LIST)

    @pyqtSlot()
    def confirm_clicked(self):
        super(TransactionSenderModel, self).confirm_clicked()
        QTimer().singleShot(5000, self.confirm_completed)

    def confirm_completed(self):
        super(TransactionSenderModel, self).confirm_completed()
        globalmethods.MainModel.setCurrentTab(Tab.HISTORY_LIST)
