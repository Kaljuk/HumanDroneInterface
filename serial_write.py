#!/usr/bin/env python

import serialDriver
import time



serDrv = serialDriver.SerialDriver()
 
while True:
	serDrv.write("[1500 1500 1500 1500 1500 1500] \n")
