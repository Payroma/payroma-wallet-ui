from plibs import *
from pheader import *
from pcontroller import event, translator
from pui import transactionsender, fonts, styles, Size
from pmodel import transactiondetails


class TransactionSenderModel(transactionsender.UiForm, event.EventForm):
    def __init__(self, parent):
        super(TransactionSenderModel, self).__init__(parent)

        self.setup()
        self.events_listening()

        # Variables
        self.__tx = None
        self.__abi = None
        self.__args = None
        self.__data = None

    def transaction_sender_changed_event(self, tx: dict, details: dict, symbol: str):
        self.__tx = tx
        self.__abi = details.get('abi', {})
        self.__args = details.get('args', {})
        self.__data = details.get('data', '')

        fn_name = self.__abi.get('name', "transfer").title()
        address = self.__args.get('recipient', self.__args.get('spender'))
        amount = self.__args.get('amount', self.__args.get('_amount'))

        self.reset()
        self.set_data(
            network="Binance Smart Chain",
            function=translator(fn_name),
            address=address,
            amount=amount,
            symbol=symbol
        )

    @pyqtSlot()
    def network_clicked(self):
        event.mainTabChanged.notify(tab=Tab.NETWORKS_LIST)

    @pyqtSlot()
    def details_clicked(self):
        details_widget = transactiondetails.TransactionDetailsModel(self)
        details_widget.set_data(
            function_type=self.__abi.get('name', 'transfer'),
            from_address=self.__tx['from'],
            to_address=self.__tx['to'],
            tx=json.dumps(self.__tx, sort_keys=False, indent=4),
            abi=json.dumps(self.__abi, sort_keys=False, indent=4),
            args=json.dumps(self.__args, sort_keys=False, indent=4),
            data=self.__data
        )

        messagebox = SPGraphics.MessageBox(
            parent=self,
            text=translator("Transaction Details"),
            font_size=fonts.data.size.title,
            color=styles.data.colors.font.name(),
            window_size=QSize(Size.messageBox.width(), 451)
        )
        messagebox.frame.layout().setContentsMargins(0, 21, 0, 11)
        messagebox.frame.layout().setSpacing(11)
        messagebox.frame.layout().addWidget(details_widget)
        messagebox.exec_()

    @pyqtSlot()
    def confirm_clicked(self):
        super(TransactionSenderModel, self).confirm_clicked()
        QTimer().singleShot(5000, self.confirm_completed)

    def confirm_completed(self):
        super(TransactionSenderModel, self).confirm_completed()
        event.mainTabChanged.notify(tab=Tab.HISTORY_LIST)
