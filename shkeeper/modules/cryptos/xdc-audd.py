from shkeeper.modules.classes.xdc import XDC


class xdc_audd(XDC):
    _display_name = "XDC XRC20 AUDD"

    def __init__(self):
        self.crypto = "XDC-AUDD"

    def getname(self):
        return "XDC-AUDD"
