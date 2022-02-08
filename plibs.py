"""
- All modules of application
- Usable for any object
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from password_strength import PasswordStats
from Crypto import Random
from Crypto.Cipher import AES
import io
import os
import sys
import six
import time
import json
import shutil
import random
import pickle
import struct
import psutil
import hashlib
import platform
import pyqrcode
import SPCrypto
import SPSecurity
import SPSettings
import SPDatabase
import SPGraphics
import SPInputmanager


if os.name == 'nt':
    from winregistry import WinRegistry
