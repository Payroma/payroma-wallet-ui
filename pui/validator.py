from plibs import QRegExpValidator, QRegExp


username = QRegExpValidator(QRegExp('[0-9-a-z-A-Z-!-~]{40}'))
symbol = QRegExpValidator(QRegExp('[A-Z]{20}'))
number = QRegExpValidator(QRegExp('[0-9]{40}'))
url = QRegExpValidator(QRegExp('[0-9-a-z-A-Z-!-~]{200}'))