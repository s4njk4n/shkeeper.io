from shkeeper.modules.classes.arbitrum import XDC


class xdceth(XDC):
    def __init__(self):
        self.crypto = "XDCETH"

    def getname(self):
        return "XDC ETH"
