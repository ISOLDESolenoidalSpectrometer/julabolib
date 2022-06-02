#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Example script to read the status from the julabo unit
# 20190109 - Joonas Konki

import julabolib
from serial.tools import list_ports
import requests

USB_SERIAL_NO = 'FT1UVQPS'

HTTP_TIMEOUT = 10

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

actual_status = mychiller.get_power()
print("Julabo power mode is (1 == ON, 0 == OFF): " + str(actual_status) )
if len(actual_status) > 0:
        actual_status = actual_status[:1]
if '' == actual_status:
        actual_status = '2'

set_temp = mychiller.get_work_temperature()
print("Julabo working temperature is: " + str(set_temp) )

cur_temp = mychiller.get_temperature()
print("Julabo actual bath temperature is: " + str(cur_temp) )

mychiller.close()

# Send data to influx
payload = 'temps,device=chiller,mode=read value=' + ('%.2f' % cur_temp)
payload += '\ntemps,device=chiller,mode=set value=' + ('%.2f' % set_temp)
payload += '\npowerstatus,device=chiller value=' + str(actual_status)
try:
        r = requests.post('https://dbod-iss.cern.ch:8080/write?db=he', auth = ('admin', 'issmonitor'), data=payload, verify=False, timeout=HTTP_TIMEOUT)
except Exception:
        pass

# Write the temperature to a file
filename = '/home/pi/scripts/current_chiller_temp.txt'
f = open(filename,'w+')
f.write( '%.2f' % cur_temp )
f.close()

