"""
- The main header for all objects
- Usable for any object
"""

from plibs import os, sys, platform, psutil, QApplication, QTranslator


# OS info
OS_TYPE = platform.system().lower()
ARCH_TYPE = platform.architecture()[0]
IS_WINDOWS = (OS_TYPE == 'windows')
IS_LINUX = (OS_TYPE == 'linux')
IS_MAC = (OS_TYPE == 'darwin')


# Application info
SOFTWARE_NAME = 'Payroma'
VERSION = 'Decentralized Wallet v2.2022-02'
SECRET_VALUE = (
    # Set the application password here
    (116, 101, 115, 116)
)


# Websites
class Website:
    PAYROMA = 'www.payroma.com'


# Directories
class Dir:
    if IS_WINDOWS:
        DESKTOP = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:
        DESKTOP = os.path.join(os.environ['HOME'], 'Desktop')
    LANGUAGES = 'languages'
    SETTINGS = 'settings'
    DATABASE = 'database'
    TEMP = 'temp'
    LOGS = 'logs'
    ASSETS = 'assets'


# Settings Options  // Set settings options here
class SettingsOption:
    pass


# Shortcuts
class Global:
    processExecutable = psutil.Process()
    kernel = QApplication(sys.argv)
    translator = QTranslator()
    logsSystem = None
    settings = None


# Tabs
class Tab:
    WALLETS_LIST = 'walletsListModel'
    ADD_WALLET = 'addWalletModel'
    SETTINGS = 'settingsModel'
    NETWORKS_LIST = 'networksListModel'
    ADD_NETWORK = 'addNetworkModel'
    LOGIN = 'loginModel'
    AUTHENTICATOR = 'authenticatorModel'
    AUTHENTICATOR_SETUP = 'authenticatorSetupModel'
    WALLET = 'walletModel'
    STAKE_LIST = 'stakeListModel'
    STAKE_PAIR = 'stakePairModel'
    DEPOSIT = 'depositModel'
    WITHDRAW = 'withdrawModel'
    SWAP = 'swapModel'
    HISTORY_LIST = 'historyListModel'
    TRANSACTION_SENDER = 'transactionSenderModel'

    class WalletTab:
        TOKENS_LIST = 'tokensListModel'
        WALLET_DETAILS = 'walletDetailsModel'
        ADD_TOKEN = 'addTokenModel'

    class AuthenticatorSetupTab:
        DOWNLOAD = 'authenticatorDownloadModel'
        VERIFICATION = 'authenticatorVerificationModel'
        SCAN = 'authenticatorScanModel'
        FINISHED = 'authenticatorFinishedModel'
