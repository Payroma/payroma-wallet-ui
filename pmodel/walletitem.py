from pui import walletitem


class WalletItem(walletitem.UiForm):
    def __init__(self, parent):
        super(WalletItem, self).__init__(parent)

        self.setup()
