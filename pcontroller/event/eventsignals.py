from . import eventcaller


# All events signals
appStarted = eventcaller.EventCaller()
mainTabChanged = eventcaller.EventCaller()
themeChanged = eventcaller.EventCaller()

networkChanged = eventcaller.EventCaller()
networkBlockChanged = eventcaller.EventCaller()
networkEdited = eventcaller.EventCaller()

walletChanged = eventcaller.EventCaller()
walletEdited = eventcaller.EventCaller()

loginForward = eventcaller.EventCaller()

authenticatorForward = eventcaller.EventCaller()

authenticatorSetupTabChanged = eventcaller.EventCaller()
authenticatorSetupVerified = eventcaller.EventCaller()

walletTabChanged = eventcaller.EventCaller()
tokenEdited = eventcaller.EventCaller()

stakePairChanged = eventcaller.EventCaller()
stakePairApproved = eventcaller.EventCaller()

withdrawAddressChanged = eventcaller.EventCaller()
addressBookEdited = eventcaller.EventCaller()

transactionSenderChanged = eventcaller.EventCaller()
transactionHistoryEdited = eventcaller.EventCaller()
