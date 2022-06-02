#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Example script to read the status from the julabo unit
# Identify correct USB serial port according to serial number 
# of the USB-to-serial converter
# 20190123 - Joonas Konki

import julabolib
from serial.tools import list_ports

USB_SERIAL_NO = 'FT1UVQPS'

#Find the address of the USB-to-serial converter
ports = list_ports.comports()
myport = ''
for port in ports:
	if USB_SERIAL_NO == port.serial_number:
		myport = port.device
		break

if 0 == len(myport): # port not found
	print("USB-to-serial converter not found")
	exit(1)

mychiller = julabolib.JULABO(myport, baud=4800)

val = mychiller.get_status()
print("Julabo status is: " + val)

val = mychiller.get_version()
print("Julabo version is: " + val)

val = mychiller.get_power()
print("Julabo power mode is (1 == ON, 0 == OFF): " + str(val) )

val = mychiller.get_work_temperature()
print("Julabo working temperature is: " + str(val) )

val = mychiller.get_temperature()
print("Julabo actual bath temperature is: " + str(val) )

mychiller.close()
