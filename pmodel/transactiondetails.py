from pui import transactiondetails


class TransactionDetailsModel(transactiondetails.UiForm):
    def __init__(self, parent):
        super(TransactionDetailsModel, self).__init__(parent)

        self.setup()
