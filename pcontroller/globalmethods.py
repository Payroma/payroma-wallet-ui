class MainModel:
    _setCurrentTab = None
    _setThemeMode = None
    _backgroundColorAnimate = None
    _textColorAnimate = None

    @staticmethod
    def setCurrentTab(name: str, recordable: bool = True):
        MainModel._setCurrentTab(name, recordable)

    @staticmethod
    def setThemeMode(name: str = ''):
        MainModel._setThemeMode(name)


class LoginModel:
    _setData = None

    @staticmethod
    def setData(username: str, address: str):
        LoginModel._setData(username, address)


class WalletModel:
    _setData = None
    _setCurrentTab = None

    @staticmethod
    def setData(username: str, address: str):
        WalletModel._setData(username, address)

    @staticmethod
    def setCurrentTab(name: str):
        WalletModel._setCurrentTab(name)


class WalletDetailsModel:
    _setData = None
    _setPrivateKey = None

    @staticmethod
    def setData(address: str, created_date: str):
        WalletDetailsModel._setData(address, created_date)

    @staticmethod
    def setPrivateKey(text: str):
        WalletDetailsModel._setPrivateKey(text)


class DepositModel:
    _setData = None

    @staticmethod
    def setData(address: str, network_name: str):
        DepositModel._setData(address, network_name)


class WithdrawModel:
    _setAddress = None

    @staticmethod
    def setAddress(text: str):
        WithdrawModel._setAddress(text)


class AddressesBookListModel:
    _search = None

    @staticmethod
    def search(text: str):
        AddressesBookListModel._search(text)


class StakePairModel:
    _setData = None
    _setApproved = None

    @staticmethod
    def setData(block_title: str, blocks: int, total_staked: str, stake_symbol: str, earn_symbol: str):
        StakePairModel._setData(block_title, blocks, total_staked, stake_symbol, earn_symbol)

    @staticmethod
    def setApproved():
        StakePairModel._setApproved()


class StakePairAmountModel:
    _setData = None

    @staticmethod
    def setData(balance: str, staked: str, claim: str, stake_symbol: str, earn_symbol: str):
        StakePairAmountModel._setData(balance, staked, claim, stake_symbol, earn_symbol)


class AuthenticatorSetupModel:
    _setCurrentTab = None

    @staticmethod
    def setCurrentTab(name: str):
        AuthenticatorSetupModel._setCurrentTab(name)
