from .eventsignals import *


# The model that is inherited to objects
class EventForm:
    def events_listening(self):
        """Listen to all signals"""

        appStarted.listen(self.app_started_event)
        mainTabChanged.listen(self.main_tab_changed_event)
        themeChanged.listen(self.theme_changed_event)
        networkChanged.listen(self.network_changed_event)
        networkEdited.listen(self.network_edited_event)
        walletChanged.listen(self.wallet_changed_event)
        walletEdited.listen(self.wallet_edited_event)
        loginForward.listen(self.login_forward_event)
        authenticatorForward.listen(self.authenticator_forward_event)
        authenticatorSetupTabChanged.listen(self.authenticator_setup_tab_changed_event)
        authenticatorSetupVerified.listen(self.authenticator_setup_verified_event)
        walletTabChanged.listen(self.wallet_tab_changed_event)
        tokenEdited.listen(self.token_edited_event)
        stakePairChanged.listen(self.stake_pair_changed_event)
        stakePairApproved.listen(self.stake_pair_approved_event)
        withdrawAddressChanged.listen(self.withdraw_address_changed_event)
        addressBookEdited.listen(self.address_book_edited_event)
        transactionSenderChanged.listen(self.transaction_sender_changed_event)

    def app_started_event(self):
        pass

    def main_tab_changed_event(self, tab: str, recordable: bool = True):
        pass

    def theme_changed_event(self, name: str):
        pass

    def network_changed_event(self, name: str, status: bool):
        pass

    def network_edited_event(self):
        pass

    def wallet_changed_event(self, username: str, address: str):
        pass

    def wallet_edited_event(self):
        pass

    def login_forward_event(self, method):
        pass

    def authenticator_forward_event(self, method, password: str = ''):
        pass

    def authenticator_setup_tab_changed_event(self, tab: str):
        pass

    def authenticator_setup_verified_event(self, username: str, otp_hash: str):
        pass

    def wallet_tab_changed_event(self, tab: str):
        pass

    def token_edited_event(self):
        pass

    def stake_pair_changed_event(
            self, block_title: str, blocks: int, total_staked: str,
            balance: str, staked: str, claim: str, stake_symbol: str, earn_symbol: str
    ):
        pass

    def stake_pair_approved_event(self):
        pass

    def withdraw_address_changed_event(self, address: str):
        pass

    def address_book_edited_event(self):
        pass

    def transaction_sender_changed_event(self, tx: dict, details: dict, symbol: str):
        pass
