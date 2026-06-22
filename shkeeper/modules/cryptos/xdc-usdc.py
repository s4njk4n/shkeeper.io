from shkeeper.modules.classes.xdc import XDC


class xdc_usdc(XDC):
    _display_name = "XDC XRC20 USDC"

    def __init__(self):
        self.crypto = "XDC-USDC"

    def getname(self):
        return "XDC-USDC"
