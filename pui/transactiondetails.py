from plibs import *
from pcontroller import translator
from pui import SetupForm, images, qlabeladdress


class UiForm(QScrollArea, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__detailsWidget = None
        self.__labelFunctionTitle = None
        self.__labelFunction = None
        self.__labelFromTitle = None
        self.__labelFrom = None
        self.__labelToTitle = None
        self.__labelTo = None
        self.__labelTXTitle = None
        self.__textEditTX = None
        self.__labelABITitle = None
        self.__textEditABI = None
        self.__labelArgsTitle = None
        self.__textEditArgs = None
        self.__labelDataTitle = None
        self.__textEditData = None

    def setup(self):
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.horizontalScrollBar().setCursor(Qt.PointingHandCursor)
        self.verticalScrollBar().setCursor(Qt.PointingHandCursor)

        self.__detailsWidget = QWidget(self, flags=Qt.SubWindow)
        self.__detailsWidget.setLayout(QGridLayout())
        self.__detailsWidget.layout().setContentsMargins(11, 11, 0, 11)
        self.__detailsWidget.layout().setVerticalSpacing(21)
        self.__detailsWidget.setObjectName('detailsWidget')

        self.__labelFunctionTitle = SPGraphics.QuickLabel(
            self, fixed_width=101
        )

        self.__labelFunction = SPGraphics.QuickLabel(self)
        self.__labelFunction.setObjectName('labelDescription')

        self.__labelFromTitle = SPGraphics.QuickLabel(
            self, fixed_width=101
        )

        self.__labelFrom = qlabeladdress.QLabelAddress(
            self, copy_tooltip=QApplication.toolTip.copyR
        )
        self.__labelFrom.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.__labelToTitle = SPGraphics.QuickLabel(
            self, fixed_width=101
        )

        self.__labelTo = qlabeladdress.QLabelAddress(
            self, copy_tooltip=QApplication.toolTip.copyR
        )
        self.__labelTo.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.__labelTXTitle = SPGraphics.QuickLabel(
            self, fixed_width=101, align=Qt.AlignTop
        )

        self.__textEditTX = QTextEdit(self)
        self.__textEditTX.setFixedHeight(201)
        self.__textEditTX.setReadOnly(True)
        self.__textEditTX.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__textEditTX.verticalScrollBar().setCursor(Qt.PointingHandCursor)

        self.__labelABITitle = SPGraphics.QuickLabel(
            self, fixed_width=101, align=Qt.AlignTop
        )

        self.__textEditABI = QTextEdit(self)
        self.__textEditABI.setFixedHeight(201)
        self.__textEditABI.setReadOnly(True)
        self.__textEditABI.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__textEditABI.verticalScrollBar().setCursor(Qt.PointingHandCursor)

        self.__labelArgsTitle = SPGraphics.QuickLabel(
            self, fixed_width=101, align=Qt.AlignTop
        )

        self.__textEditArgs = QTextEdit(self)
        self.__textEditArgs.setFixedHeight(201)
        self.__textEditArgs.setReadOnly(True)
        self.__textEditArgs.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__textEditArgs.verticalScrollBar().setCursor(Qt.PointingHandCursor)

        self.__labelDataTitle = SPGraphics.QuickLabel(
            self, fixed_width=101, align=Qt.AlignTop
        )

        self.__textEditData = QTextEdit(self)
        self.__textEditData.setFixedHeight(201)
        self.__textEditData.setReadOnly(True)
        self.__textEditData.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__textEditData.verticalScrollBar().setCursor(Qt.PointingHandCursor)

        self.setWidgetResizable(True)
        self.setWidget(self.__detailsWidget)

        self.__detailsWidget.layout().addWidget(self.__labelFunctionTitle, 0, 0, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelFunction, 0, 1, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelFromTitle, 1, 0, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelFrom, 1, 1, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelToTitle, 2, 0, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelTo, 2, 1, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelTXTitle, 3, 0, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__textEditTX, 3, 1, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelABITitle, 4, 0, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__textEditABI, 4, 1, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelArgsTitle, 5, 0, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__textEditArgs, 5, 1, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__labelDataTitle, 6, 0, 1, 1)
        self.__detailsWidget.layout().addWidget(self.__textEditData, 6, 1, 1, 1)

        super(UiForm, self).setup()

    def re_style(self):
        self.__labelFrom.setIcon(QIcon(images.data.icons.changeable.copy21))
        self.__labelTo.setIcon(QIcon(images.data.icons.changeable.copy21))

    def re_translate(self):
        self.__labelFunctionTitle.setText(translator("Function Type"))
        self.__labelFromTitle.setText(translator("From"))
        self.__labelToTitle.setText(translator("To"))
        self.__labelTXTitle.setText(translator("Transaction"))
        self.__labelABITitle.setText(translator("ABI"))
        self.__labelArgsTitle.setText(translator("Arguments"))
        self.__labelDataTitle.setText(translator("Data Hex"))

    def re_font(self):
        font = QFont()

        self.__labelFunctionTitle.setFont(font)
        self.__labelFunction.setFont(font)
        self.__labelFromTitle.setFont(font)
        self.__labelFrom.setFont(font)
        self.__labelToTitle.setFont(font)
        self.__labelTo.setFont(font)
        self.__labelTXTitle.setFont(font)
        self.__textEditTX.setFont(font)
        self.__labelABITitle.setFont(font)
        self.__textEditABI.setFont(font)
        self.__labelArgsTitle.setFont(font)
        self.__textEditArgs.setFont(font)
        self.__labelDataTitle.setFont(font)
        self.__textEditData.setFont(font)

    def set_data(
            self, function_type: str, from_address: str, to_address: str,
            tx: str, abi: str, args: str, data: str
    ):
        self.__labelFunction.setText(function_type)
        self.__labelFrom.setText(from_address)
        self.__labelTo.setText(to_address)
        self.__textEditTX.setText(tx)
        self.__textEditABI.setText(abi)
        self.__textEditArgs.setText(args)
        self.__textEditData.setText(data)
