import os, sys, io
import M5
from M5 import *
from bleuart import *
from hardware import *
import time

ble_client = None
pin41 = None
button_timer = 0
shape_value = "Rect"
for_switch = "Off"
for_value = 0

def setup():
  global ble_client,x_position, y_position, x_size, y_size,pin41
  M5.begin()
  ble_client = BLEUARTClient()
  ble_client.connect('ble-uart', timeout=2000)
  print('connected =', ble_client.is_connected())
  x_position = ADC(Pin(6), atten=ADC.ATTN_11DB)
  y_position = ADC(Pin(1), atten=ADC.ATTN_11DB)
  x_size = ADC(Pin(8), atten=ADC.ATTN_11DB)
  y_size = ADC(Pin(2), atten=ADC.ATTN_11DB)
  pin41 = Pin(41, mode=Pin.IN)
    
def loop():
  global ble_client,x_position,y_position,x_size,y_size,for_switch,pin41,for_value
  global button_timer,shape_value
  
  M5.update()
  data = ble_client.read()
  

  button_value = pin41.value()
  
  if time.ticks_ms() > button_timer + 200:
    button_timer = time.ticks_ms()  # update button_timer
 # update button_timer
    if button_value == 0:
      if shape_value == "Rect":
        shape_value = "Hex"
      elif shape_value == "Hex":
        shape_value = "Oct"
      elif shape_value == "Oct":
        shape_value = "Cir"
      else:
        shape_value = "Rect"

  
  
  #if(data != ''):
    #print('data =', data.decode())
  
  
  x_position_val = x_position.read()
  y_position_val = y_position.read()
  x_size_val = x_size.read()
  y_size_val = y_size.read()
  
  data_list = data.decode().split(',')
  
  if(len(data_list) > 1 ):
      if(int(data_list[1]) > 3900 ):
          for_switch = "On"
      else:
          for_switch = "Off" 
      
      for_value = int(data_list[0])
  print(str(x_position_val) + "," +str(y_position_val) + "," + str(x_size_val) + "," + str(y_size_val) + "," +str(shape_value)+"," + str(for_value) + "," + for_switch)
  time.sleep_ms(100)
  
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
