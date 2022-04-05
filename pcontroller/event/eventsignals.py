from . import eventcaller


# All events signals
appStarted = eventcaller.EventCaller()
mainTabChanged = eventcaller.EventCaller()
themeChanged = eventcaller.EventCaller()

networkChanged = eventcaller.EventCaller()
networkEdited = eventcaller.EventCaller()

walletChanged = eventcaller.EventCaller()
walletEdited = eventcaller.EventCaller()

loginForward = eventcaller.EventCaller()

authenticatorForward = eventcaller.EventCaller()

authenticatorSetupTabChanged = eventcaller.EventCaller()
authenticatorSetupVerified = eventcaller.EventCaller()

walletTabChanged = eventcaller.EventCaller()

stakePairChanged = eventcaller.EventCaller()
stakePairApproved = eventcaller.EventCaller()

withdrawAddressChanged = eventcaller.EventCaller()
