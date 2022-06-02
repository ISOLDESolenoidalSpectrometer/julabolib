#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script to set the working temperature of the JULABO chiller.
# 20190110 - Joonas Konki
import julabolib
from serial.tools import list_ports
import sys

USB_SERIAL_NO = 'FT1UVPTC'

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

if len(sys.argv) != 2:
	print("Usage: ./julabo_set_temp [TEMP]")
	print("where TEMP is the desired working temperature.")
	exit()


new_temp = float(sys.argv[1])

print("Setting working temperature to " + str(new_temp))
val = mychiller.set_work_temperature(new_temp)


val = mychiller.get_work_temperature()
print("Julabo working temperature is: " + str(val) )

val = mychiller.get_temperature()
print("Julabo actual bath temperature is: " + str(val) )

mychiller.close()
