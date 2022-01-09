from pynq import DefaultIP
from pynq.buffer import PynqBuffer


class CDMA(DefaultIP):
    def __init__(self, description):
        super().__init__(description=description)

    bindto = ['xilinx.com:ip:axi_cdma:4.1']

    @property
    def idle(self):
        """
        `transfer` can only be called when the DMA is idle
        :return: True if the DMA engine is idle
        """
        return self.register_map.CDMASR.Idle

    def _do_transfer(self, source: int, dest: int, bytes_count: int):
        """
        Execute DMA transfer
        :param source: source address
        :param dest: destination address
        :param bytes_count: bytes to transfer
        :return: None
        """
        if not self.idle:
            raise Exception('DMA transfer can only start when engine is idle')

        assert source > 0
        if source > 0xFFFF_FFFF:
            self.register_map.SA_MSB[:] = source >> 8
        self.register_map.SA[:] = source & 0xFFFF_FFFF

        assert dest > 0
        if dest > 0xFFFF_FFFF:
            self.register_map.DA_MSB[:] = dest >> 8
        self.register_map.DA[:] = dest & 0xFFFF_FFFF

        assert bytes_count > 0
        self.register_map.BTT = bytes_count

        # Spin
        while not self.idle:
            pass

    def transfer(self, source, dest, bytes_count=None):
        """
        Transfer data through DMA
        :param source:
        :param dest:
        :param bytes_count:
        :return:
        """
        # Set source
        bytes_source = None
        if isinstance(source, PynqBuffer):
            source_addr = source.device_address
            bytes_source = source.nbytes
        elif isinstance(source, int):
            source_addr = source
        else:
            raise TypeError(f'Type {type(source)} not supported as source')

        bytes_dest = None
        if isinstance(dest, PynqBuffer):
            dest_addr = dest.device_address
            bytes_dest = dest.nbytes
        elif isinstance(dest, int):
            dest_addr = dest
        else:
            raise TypeError(f'Type {type(source)} not supported as dest')

        if bytes_count is None:
            if bytes_source is not None and bytes_dest is not None:
                bytes_count = min(bytes_source, bytes_dest)
            elif bytes_source is not None:
                bytes_count = bytes_source
            elif bytes_dest is not None:
                bytes_count = bytes_dest
            else:
                raise RuntimeError(f'Bytes to transfer is not set and cannot be inferred')

        self._do_transfer(source_addr, dest_addr, bytes_count)
