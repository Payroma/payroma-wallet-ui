from plibs import *
from pheader import *
from pcontroller import translator
from pui import SetupForm, fonts, images, styles, Size, validator


class UiForm(QWidget, SetupForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent, flags=Qt.SubWindow)

        self.__pushButtonBack = None
        self.__labelTitle = None
        self.__lineEditName = None
        self.__labelNameAlert = None
        self.__lineEditRPC = None
        self.__labelRPCAlert = None
        self.__lineEditChainId = None
        self.__labelChainIdAlert = None
        self.__lineEditSymbol = None
        self.__lineEditExplorer = None
        self.__labelExplorerAlert = None
        self.__pushButtonAdd = None
        self.__loadingEffectAdd = None

    def setup(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignCenter)
        self.layout().setSpacing(11)
        self.setObjectName(Tab.ADD_NETWORK)

        self.__pushButtonBack = SPGraphics.QuickPushButton(
            self, icon_size=Size.s21, fixed_size=Size.s41, tooltip=QObject.toolTip.back
        )
        self.__pushButtonBack.move(10, 10)
        self.__pushButtonBack.clicked.connect(self.back_clicked)

        self.__labelTitle = SPGraphics.QuickLabel(
            self, fixed_height=51, align=Qt.AlignCenter
        )

        self.__lineEditName = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=40
        )
        self.__lineEditName.textChanged.connect(self.name_changed)

        self.__labelNameAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QObject.toolTip.networkNameAlert
        )
        self.__labelNameAlert.setCursor(Qt.PointingHandCursor)
        self.__labelNameAlert.hide()

        self.__lineEditRPC = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=200
        )
        self.__lineEditRPC.setValidator(validator.url)
        self.__lineEditRPC.textChanged.connect(self.rpc_changed)

        self.__labelRPCAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QObject.toolTip.networkRPCAlert
        )
        self.__labelRPCAlert.setCursor(Qt.PointingHandCursor)
        self.__labelRPCAlert.hide()

        self.__lineEditSymbol = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, length=20
        )
        self.__lineEditSymbol.setValidator(validator.symbol)
        self.__lineEditSymbol.textChanged.connect(self.symbol_changed)

        self.__lineEditChainId = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=10
        )
        self.__lineEditChainId.setValidator(validator.number)
        self.__lineEditChainId.textChanged.connect(self.chain_id_changed)

        self.__labelChainIdAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QObject.toolTip.networkChainIdAlert
        )
        self.__labelChainIdAlert.setCursor(Qt.PointingHandCursor)
        self.__labelChainIdAlert.hide()

        self.__lineEditExplorer = SPGraphics.QuickLineEdit(
            self, fixed_size=Size.default, layout_support=True, length=200
        )
        self.__lineEditExplorer.setValidator(validator.url)
        self.__lineEditExplorer.textChanged.connect(self.explorer_changed)

        self.__labelExplorerAlert = SPGraphics.QuickLabel(
            self, scaled=True, pixmap=images.data.icons.warning41,
            fixed_size=Size.s21, tooltip=QObject.toolTip.networkExplorerAlert
        )
        self.__labelExplorerAlert.setCursor(Qt.PointingHandCursor)
        self.__labelExplorerAlert.hide()

        self.__pushButtonAdd = SPGraphics.QuickPushButton(
            self, fixed_size=Size.default, value_changed=QObject.mainModel.backgroundColorAnimated,
            start_value=styles.data.colors.highlight, end_value=styles.data.colors.highlight_hover
        )
        self.__pushButtonAdd.setLayout(QVBoxLayout())
        self.__pushButtonAdd.setDisabled(True)
        self.__pushButtonAdd.clicked.connect(self.add_clicked)

        self.__loadingEffectAdd = SPGraphics.QLoadingEffect(
            self, color=styles.data.colors.highlight_third.name(),
            light_color=styles.data.colors.white.name()
        )

        self.layout().addWidget(self.__labelTitle)
        self.layout().addWidget(self.__lineEditName)
        self.layout().addWidget(self.__lineEditRPC)
        self.layout().addWidget(self.__lineEditSymbol)
        self.layout().addWidget(self.__lineEditChainId)
        self.layout().addWidget(self.__lineEditExplorer)
        self.layout().addWidget(self.__pushButtonAdd)
        self.__lineEditName.layout().addWidget(self.__labelNameAlert, alignment=Qt.AlignRight)
        self.__lineEditRPC.layout().addWidget(self.__labelRPCAlert, alignment=Qt.AlignRight)
        self.__lineEditChainId.layout().addWidget(self.__labelChainIdAlert, alignment=Qt.AlignRight)
        self.__lineEditExplorer.layout().addWidget(self.__labelExplorerAlert, alignment=Qt.AlignRight)
        self.__pushButtonAdd.layout().addWidget(self.__loadingEffectAdd, alignment=Qt.AlignCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.addnetwork)
        self.__pushButtonBack.setIcon(QIcon(images.data.icons.changeable.arrow_left21))

    def re_translate(self):
        self.__labelTitle.setText(translator("Add a Network"))
        self.__lineEditName.setPlaceholderText(translator("Network Name"))
        self.__lineEditRPC.setPlaceholderText(translator("RPC URL"))
        self.__lineEditSymbol.setPlaceholderText(translator("Currency Symbol"))
        self.__lineEditChainId.setPlaceholderText(translator("Chain ID"))
        self.__lineEditExplorer.setPlaceholderText(translator("Block Explorer URL"))
        self.__pushButtonAdd.setText(translator("Add Network"))

    def re_font(self):
        font = QFont()

        self.__lineEditName.setFont(font)
        self.__lineEditRPC.setFont(font)
        self.__lineEditSymbol.setFont(font)
        self.__lineEditChainId.setFont(font)
        self.__lineEditExplorer.setFont(font)

        font.setPointSize(fonts.data.size.title)
        font.setBold(True)
        self.__pushButtonAdd.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelTitle.setFont(font)

    @pyqtSlot()
    def back_clicked(self):
        pass

    @pyqtSlot(str)
    def name_changed(self, text: str, valid: bool = False):
        self.__lineEditName.isValid = valid
        self.__labelNameAlert.setHidden(valid)
        self.__inputs_validation()

    @pyqtSlot(str)
    def rpc_changed(self, text: str, valid: bool = False):
        self.__lineEditRPC.isValid = valid
        self.__labelRPCAlert.setHidden(valid)
        self.__inputs_validation()

    @pyqtSlot(str)
    def symbol_changed(self, text: str, valid: bool = False):
        self.__lineEditSymbol.isValid = valid
        self.__inputs_validation()

    @pyqtSlot(str)
    def chain_id_changed(self, text: str, valid: bool = False):
        self.__lineEditChainId.isValid = valid
        self.__labelChainIdAlert.setHidden(valid)
        self.__inputs_validation()

    @pyqtSlot(str)
    def explorer_changed(self, text: str, valid: bool = False):
        self.__lineEditExplorer.isValid = valid
        self.__labelExplorerAlert.setHidden(valid)
        self.__inputs_validation()

    @pyqtSlot()
    def add_clicked(self):
        self.__all_inputs_disabled(True)
        self.__loadingEffectAdd.start()
        self.__pushButtonBack.hide()
        self.__pushButtonAdd.setText("")

    def add_completed(self):
        self.__all_inputs_disabled(False)
        self.__loadingEffectAdd.stop()
        self.__pushButtonBack.show()
        QTimer().singleShot(1000, self.re_translate)

    def reset(self):
        self.__all_inputs_disabled(False)
        self.__lineEditName.clear()
        self.__lineEditRPC.clear()
        self.__lineEditSymbol.clear()
        self.__lineEditChainId.clear()
        self.__lineEditExplorer.clear()

    def __inputs_validation(self):
        valid = False
        try:
            if (
                self.__lineEditName.isValid and
                self.__lineEditRPC.isValid and
                self.__lineEditSymbol.isValid and
                self.__lineEditChainId.isValid and
                self.__lineEditExplorer.isValid
            ):
                valid = True
        except AttributeError:
            pass

        self.__pushButtonAdd.setEnabled(valid)

    def __all_inputs_disabled(self, status: bool):
        self.__lineEditName.setDisabled(status)
        self.__lineEditRPC.setDisabled(status)
        self.__lineEditSymbol.setDisabled(status)
        self.__lineEditChainId.setDisabled(status)
        self.__lineEditExplorer.setDisabled(status)
