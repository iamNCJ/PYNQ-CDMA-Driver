from pynq import DefaultIP


class CDMA(DefaultIP):
    def __init__(self, description):
        super().__init__(description=description)

    bindto = ['xilinx.com:ip:axi_cdma:4.1']

    @property
    def idle(self):
        """True if the DMA engine is idle

        `transfer` can only be called when the DMA is idle

        """
        return self.register_map.CDMASR.Idle
