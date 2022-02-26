from plibs import QRegExpValidator, QRegExp


username = QRegExpValidator(QRegExp('[0-z-!-~]{30}'))
address = QRegExpValidator(QRegExp('0x?[0-9-a-f-A-F]{40}'))
symbol = QRegExpValidator(QRegExp('[A-Z]'))
number = QRegExpValidator(QRegExp('[0-9]'))
balance = QRegExpValidator(QRegExp('[-+]?[1-9][\\d]*\\.?[0-9]+'))
url = QRegExpValidator(QRegExp('http|https?://[0-z-!-~]*'))
