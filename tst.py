#!/usr/bin/env python

# loopback test script
#   connect MOSI and MISO

import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 5000
spi.mode = 0b01

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

def IntToBytes(Int):
    hexValue = hex(Int)
    values = [hexValue[i:i+n] for i in range(0, len(line), 2)]
    print(values)

def IntToBytes(Int):
    hexValue = hex(Int)
    values = [hexValue[i:i+2] for i in range(2, len(hexValue), 2)]
    result = []
    for value in values:
        stringValue = "0x"+value
        result.append(int(stringValue,0))
    return result

try:
    while True:
        print(IntToBytes(1500))
        resp = spi.xfer([0x87] + IntToBytes(1500))
        print(resp)
        #print(asd)
        #print(BytesToHex(resp))
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()