#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script to turn the JULABO chiller ON.
# Requires that the remote control has been enabled.
# 20190110 - Joonas Konki
import julabolib
from serial.tools import list_ports

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

print("Sending turn ON command")
val = mychiller.set_power_on()

val = mychiller.get_power()
print("Julabo power is (1 == ON, 0 == OFF): " + str(val))

mychiller.close()
