from plibs import QRegExpValidator, QRegExp


username = QRegExpValidator(QRegExp('[0-9-a-z-A-Z-!-~]{42}'))
address = QRegExpValidator(QRegExp('0x?[0-9-a-f-A-F]{40}'))
symbol = QRegExpValidator(QRegExp('[A-Z]{20}'))
number = QRegExpValidator(QRegExp('[0-9]{40}'))
balance = QRegExpValidator(QRegExp('[-+]?[1-9][\\d]*\\.?[0-9]+'))
url = QRegExpValidator(QRegExp('[0-9-a-z-A-Z-!-~]{200}'))
