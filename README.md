# PYNQ-CDMA-Driver
 PYNQ Driver for Xilinx Central Direct Memory Access IP

## Usage

Currently, we only support simple DMA transfer

### Auto bind

First import `CDMA`

```python
from pynq_cdma import CDMA
```

Now if your design contains CDMA IP, Pynq will automatically bind it to a `CDMA` instance.

You can check its status by accessing the `idle` property:

```python
from pynq import Overlay
ol = Overlay('top.bit')
print(ol.axi_cdma_0.idle)
```

### Data transfer

```python
import numpy as np
from pynq import allocate
input_buffer = allocate(shape=(8,), dtype=np.uint8)
output_buffer = allocate(shape=(8,), dtype=np.uint8)
for i in range(8):
    input_buffer[i] = i
ol.axi_cdma_0.transfer(input_buffer, 0xF000_0000)
ol.axi_cdma_0.transfer(0xF000_0000, output_buffer)
print(output_buffer)
```
