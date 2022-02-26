from plibs import *
from pheader import *
from pui import historylist


class HistoryListModel(historylist.UiForm):
    def __init__(self, parent):
        super(HistoryListModel, self).__init__(parent)

        self.setup()

    @pyqtSlot()
    def back_clicked(self):
        QObject.mainModel.currentTabChanged(Tab.WALLET)

    @pyqtSlot(QListWidgetItem)
    def item_clicked(self, item: QListWidgetItem):
        widget = super(HistoryListModel, self).item_clicked(item)
