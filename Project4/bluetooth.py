# BLE UART server example for M5Stack AtomS3
# run the BLE UART client example on another AtomS3 board


import os, sys, io
import M5
from hardware import *
from M5 import *
from bleuart import *
import time

ble_server = None
title0 = None
label0 = None
for_module = None

def setup():
  global ble_server
  global for_module, light_module
  global label0, title0
  M5.begin()
  title0 = Widgets.Title("BLE server", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  label0 = Widgets.Label("--", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  ble_server = BLEUARTServer(name='ble-uart')
  for_module = ADC(Pin(1), atten=ADC.ATTN_11DB)
  light_module = ADC(Pin(6), atten=ADC.ATTN_11DB)

def loop():
  global ble_server,light_module
  global for_module
  global label0
  M5.update()
  for_module_value = for_module.read()
  light_module_value = light_module.read()
  #print('write to bleuart..')
  print(str(for_module_value)+ "," +str(light_module_value))
  #ble_server.write('hello M5!')
  ble_server.write(str(for_module_value)+ "," +str(light_module_value))
  label0.setText(str(for_module_value))
  time.sleep_ms(1000)

  
if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")


