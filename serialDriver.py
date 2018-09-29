#!/usr/bin/env python

import serial


class SerialDriver:
	def __init__(self):
		self.ser = serial.Serial(
			port = '/dev/ttyS0',
			baudrate = 9600,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			bytesize = serial.EIGHTBITS,
			timeout = 1
		)
	def write(self, output):
		self.ser.write(output);
		return True


