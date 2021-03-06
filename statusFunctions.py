import usb.core
from wifi import Cell, Scheme
from PIL import Image

VENDOR = 0x2367
PRODUCT = 0x0002
_op1_connected = Image.open("resources/op1_connected.xbm").convert("1")
_op1_notConnected = Image.open("resources/op1_notConnected.xbm").convert("1")
_wifi_notConnected = Image.open("resources/wifi_notConnected.xbm").convert("1")
_wifi_25 = Image.open("resources/wifi_25.xbm").convert("1")
_wifi_50 = Image.open("resources/wifi_50.xbm").convert("1")
_wifi_75 = Image.open("resources/wifi_75.xbm").convert("1")
_wifi_100 = Image.open("resources/wifi_100.xbm").convert("1")




def is_connected():
    if usb.core.find(idVendor=VENDOR, idProduct=PRODUCT) is not None:
        return _op1_connected
    else:
        return _op1_notConnected
        #return not connected img


def wifi_status():
    # TODO get signal strength/connection status EFFICIENTLY (or cache it and only check every 5 seconds or so)
    signal = 0.5
    if signal is None:
        return _wifi_notConnected
    elif signal <=0.25:
        return _wifi_25
    elif signal <=0.50:
        return _wifi_50
    elif signal <=0.75:
        return _wifi_75
    else:
        return _wifi_100