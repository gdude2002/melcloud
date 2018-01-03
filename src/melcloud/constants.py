# coding=utf-8

"""
Constant values used across the MELCloud module
"""

from enum import IntEnum

__author__ = "Gareth Coles"
__version__ = "0.0.1"

URL_LOGIN = "https://app.melcloud.com/Mitsubishi.Wifi.Client/Login/ClientLogin"
URL_LIST_DEVICES = "https://app.melcloud.com/Mitsubishi.Wifi.Client/User/ListDevices"
URL_GET_DEVICE = "https://app.melcloud.com/Mitsubishi.Wifi.Client/Device/Get"  # id, buildingID
URL_SET_VALUE = "https://app.melcloud.com/Mitsubishi.Wifi.Client/Device/SetAta"
URL_SET_OPTIONS = "https://app.melcloud.com/Mitsubishi.Wifi.Client/User/UpdateApplicationOptions"

KEY_HEADER = "X-MitsContextKey"


class LANGUAGES(IntEnum):
    """
    Enum of supported language codes
    """

    EN = 0  #: English
    BG = 1  #: Bulgarian
    CS = 2  #: Czech
    DA = 3  #: Danish
    DE = 4  #: German
    ET = 5  #: Estonian
    ES = 6  #: Spanish
    FR = 7  #: French
    HY = 8  #: Armenian
    LV = 9  #: Latvian
    LT = 10  #: Lithuanian
    HU = 11  #: Hungarian
    NL = 12  #: Dutch
    NO = 13  #: Norwegian
    PL = 14  #: Polish
    PT = 15  #: Portuguese
    RU = 16  #: Russian
    FI = 17  #: Finnish
    SV = 18  #: Swedish
    IT = 19  #: Italian
    UK = 20  #: Ukrainian
    TR = 21  #: Turkish
    EL = 22  #: Greek
    HR = 23  #: Croatian
    RO = 24  #: Romanian
    SL = 25  #: Slovenian
