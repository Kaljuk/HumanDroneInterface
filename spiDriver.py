<<<<<<< HEAD
#!/usr/bin/env python

import spidev
import time


def init():
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 5000
    spi.mode = 0b01
    return spi


def int_to_bytes(int_value):
    hex_value = hex(int_value)
    values = [hex_value[i:i+2] for i in range(2, len(hex_value), 2)]
    result = []
    for value in values:
        string_value = "0x"+value
        result.append(int(string_value,0))
    return result


def send(spi, values):
    data_to_send = []
    for value in values:
        data_to_send += int_to_bytes(value)
    resp = spi.xfer([0x87] + data_to_send)
    print(resp)


def close(spi):
    spi.close()
=======
#!/usr/bin/env python

import spidev
import time


def init():
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 5000
    spi.mode = 0b01
    return spi


def int_to_bytes(int_value):
    hex_value = hex(int_value)
    values = [hex_value[i:i+2] for i in range(2, len(hex_value), 2)]
    result = []
    for value in values:
        string_value = "0x"+value
        result.append(int(string_value,0))
    return result


def send(spi, values):
    data_to_send = []
    for value in values:
        data_to_send += int_to_bytes(value)
    resp = spi.xfer([0x87] + data_to_send)
    print(resp)

def read(spi):
    while True:
        try:
            # Read N bytes from SPI device
            received = spi.readbytes(5) # n = 3,2 ?
            print(received)
        except KeyboardInterrupt:
            spi.close()
            break



def close(spi):
    spi.close()
>>>>>>> f48946d54450b749ab9df4ad2c00391d22ced699
