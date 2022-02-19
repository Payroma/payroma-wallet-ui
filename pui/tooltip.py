from plibs import *
from pcontroller import translator
from pui import SetupForm


class UiForm(SetupForm):
    def __init__(self, parent):
        self.__parent = parent

        self.settings = None
        self.exit = None
        self.copy = None
        self.back = None
        self.remove = None
        self.usernameAlert = None
        self.passwordAlert = None
        self.passwordConfirmAlert = None
        self.pinCodeAlert = None
        self.addressAlert = None
        self.networkStatus = None
        self.ShowBlockTime = None

        self.showR = None
        self.usernameInfoR = None
        self.pinCodeInfoR = None
        self.addressInfoR = None
        self.networkSettingsR = None
        self.addNewR = None
        self.networkNameAlertR = None
        self.networkRPCAlertR = None
        self.networkChainIdAlertR = None
        self.networkExplorerAlertR = None
        self.copyR = None
        self.favoriteR = None
        self.walletStatusR = None
        self.networkStatusR = None
        self.menuR = None

        self.depositB = None
        self.withdrawB = None
        self.stakeB = None
        self.swapB = None
        self.historyB = None
        self.addressValidB = None

    def setup(self):
        self.settings = self.__align_top()
        self.exit = self.__align_top()
        self.copy = self.__align_top()
        self.back = self.__align_top()
        self.remove = self.__align_top()
        self.usernameAlert = self.__align_top()
        self.passwordAlert = self.__align_top()
        self.passwordConfirmAlert = self.__align_top()
        self.pinCodeAlert = self.__align_top()
        self.addressAlert = self.__align_top()
        self.networkStatus = self.__align_top()
        self.ShowBlockTime = self.__align_top()

        self.showR = self.__align_right()
        self.usernameInfoR = self.__align_right()
        self.pinCodeInfoR = self.__align_right()
        self.addressInfoR = self.__align_right()
        self.networkSettingsR = self.__align_right()
        self.addNewR = self.__align_right()
        self.networkNameAlertR = self.__align_right()
        self.networkRPCAlertR = self.__align_right()
        self.networkChainIdAlertR = self.__align_right()
        self.networkExplorerAlertR = self.__align_right()
        self.copyR = self.__align_right()
        self.favoriteR = self.__align_right()
        self.walletStatusR = self.__align_right()
        self.networkStatusR = self.__align_right()
        self.menuR = self.__align_right()

        self.depositB = self.__align_bottom()
        self.withdrawB = self.__align_bottom()
        self.stakeB = self.__align_bottom()
        self.swapB = self.__align_bottom()
        self.historyB = self.__align_bottom()
        self.addressValidB = self.__align_bottom()

        super(UiForm, self).setup()

    def re_translate(self):
        self.settings.labelText.setText(translator("Settings"))
        self.exit.labelText.setText(translator("Exit"))
        self.copy.labelText.setText(translator("Copy"))
        self.back.labelText.setText(translator("Back"))
        self.remove.labelText.setText(translator("Remove"))
        self.usernameAlert.labelText.setText(translator(
            "The username/email/phone is already taken, try another username."
        ))
        self.passwordAlert.labelText.setText(translator(
            "Password must be good at least and including UPPER/lowercase, symbols and numbers."
        ))
        self.passwordConfirmAlert.labelText.setText(translator("Password doesn't match."))
        self.pinCodeAlert.labelText.setText(translator("PIN Code must be 6 numbers."))
        self.addressAlert.labelText.setText(translator("This address invalid."))
        self.networkStatus.labelText.setText(translator("Network Connection Status"))
        self.ShowBlockTime.labelText.setText(translator("Show block time"))

        self.showR.labelText.setText(translator("Show"))
        self.usernameInfoR.labelText.setText(translator(
            "Username/email is sensitive to characters."
        ))
        self.pinCodeInfoR.labelText.setText(translator(
            "PIN code is important to add your wallet to our app later, It acts as a second layer of protection."
        ))
        self.addressInfoR.labelText.setText(translator(
            "If you have an existing wallet, set the wallet address to check."
        ))
        self.networkSettingsR.labelText.setText(translator("Network settings to add a new and switching."))
        self.addNewR.labelText.setText(translator("Add New"))
        self.networkNameAlertR.labelText.setText(translator("Network name already exists before"))
        self.networkRPCAlertR.labelText.setText(translator("This RPC is unable to connect"))
        self.networkChainIdAlertR.labelText.setText(translator("Chain id is wrong"))
        self.networkExplorerAlertR.labelText.setText(translator("Explorer URL is wrong"))
        self.copyR.labelText.setText(translator("Copy"))
        self.favoriteR.labelText.setText(translator("Check to Favorite"))
        self.walletStatusR.labelText.setText(translator("Wallet connection status"))
        self.networkStatusR.labelText.setText(translator("Network connection status"))
        self.menuR.labelText.setText(translator("Menu"))

        self.depositB.labelText.setText(translator("Deposit"))
        self.withdrawB.labelText.setText(translator("Withdraw"))
        self.stakeB.labelText.setText(translator("Staking"))
        self.swapB.labelText.setText(translator("Swap"))
        self.historyB.labelText.setText(translator("Transactions History"))
        self.addressValidB.labelText.setText(translator("Address Valid"))

    def re_font(self):
        font = QFont()

        self.settings.labelText.setFont(font)
        self.exit.labelText.setFont(font)
        self.copy.labelText.setFont(font)
        self.back.labelText.setFont(font)
        self.remove.labelText.setFont(font)
        self.usernameAlert.labelText.setFont(font)
        self.passwordAlert.labelText.setFont(font)
        self.passwordConfirmAlert.labelText.setFont(font)
        self.pinCodeAlert.labelText.setFont(font)
        self.addressAlert.labelText.setFont(font)
        self.networkStatus.labelText.setFont(font)
        self.ShowBlockTime.labelText.setFont(font)

        self.showR.labelText.setFont(font)
        self.usernameInfoR.labelText.setFont(font)
        self.pinCodeInfoR.labelText.setFont(font)
        self.addressInfoR.labelText.setFont(font)
        self.networkSettingsR.labelText.setFont(font)
        self.addNewR.labelText.setFont(font)
        self.networkNameAlertR.labelText.setFont(font)
        self.networkRPCAlertR.labelText.setFont(font)
        self.networkChainIdAlertR.labelText.setFont(font)
        self.networkExplorerAlertR.labelText.setFont(font)
        self.copyR.labelText.setFont(font)
        self.favoriteR.labelText.setFont(font)
        self.walletStatusR.labelText.setFont(font)
        self.networkStatusR.labelText.setFont(font)
        self.menuR.labelText.setFont(font)

        self.depositB.labelText.setFont(font)
        self.withdrawB.labelText.setFont(font)
        self.stakeB.labelText.setFont(font)
        self.swapB.labelText.setFont(font)
        self.historyB.labelText.setFont(font)
        self.addressValidB.labelText.setFont(font)

    def __align_top(self) -> SPGraphics.QuickToolTip:
        return SPGraphics.QuickToolTip(
            self.__parent, text_align=Qt.AlignCenter, align=Qt.AlignTop
        )

    def __align_right(self) -> SPGraphics.QuickToolTip:
        return SPGraphics.QuickToolTip(
            self.__parent, text_align=Qt.AlignCenter, align=Qt.AlignRight,
            arrow_size=QSize(8, 15), margin=15
        )

    def __align_bottom(self) -> SPGraphics.QuickToolTip:
        return SPGraphics.QuickToolTip(
            self.__parent, text_align=Qt.AlignCenter, align=Qt.AlignBottom
        )
