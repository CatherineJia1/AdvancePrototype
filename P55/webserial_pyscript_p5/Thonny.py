import os, sys, io
import M5
from M5 import *
import time

title0 = None
label0 = None
label1 = None
label2 = None
one_time = 0
up_time = 0
last_move=0
down_time = 0
imu_val = None
play_state = "UP"

imu_x_val = 0
imu_x_last = 0
imu_x_diff = 0
imu_timer = 0

def setup():
  global title0, label0, label1, label2

  M5.begin()
  title0 = Widgets.Title("IMU test", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  label0 = Widgets.Label("--", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label1 = Widgets.Label("--", 3, 40, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label2 = Widgets.Label("--", 3, 60, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)


def loop():
  global title0, label0, label1, label2
  global imu_val,down_time,one_time,play_state,down_time,last_move
  global imu_x_val, imu_x_last, imu_x_diff
  global imu_timer
  M5.update()
  
  # read the IMU accelerometer values:
  imu_val = Imu.getAccel()
  

  imu_x_last = imu_x_val
  imu_x_val = imu_val[1]
  imu_x_diff = abs(imu_x_val - imu_x_last)
  imu_timer = time.ticks_ms()
  
    # print all IMU values (X, Y, Z):
    #print(imu_val)
    # print the first IMU value (X) only:
    # print(imu_val)
  
    # format each IMU value with 2 points precision:

  imu_str = 'acc x: {:0.2f}'.format(imu_val[0])
  label0.setText(imu_str)
  
  imu_str = 'x diff: {:0.2f}'.format(imu_x_diff)
  label1.setText(imu_str)
  
    

  
  #imu_str = 'acc y: {:0.2f}'.format(imu_val[1])
  #label1.setText(imu_str)
  #imu_str = 'acc z: {:0.2f}'.format(imu_val[2])
  #label2.setText(imu_str)
  
  time_note = 0
  
  #print(imu_val[0])
  
  if(abs(imu_val[0]) < 0.005):
      time_note = time.ticks_ms() - last_move
      #print(time_note)
      last_move = time.ticks_ms()
      
  if(imu_x_diff > 0.60):
      print("quick")
  elif(imu_x_diff > 0.05):
      print("slow")
  else:
      print("note")
  time.sleep_ms(100)
  
#   if imu_x_diff > 0.5 and time_note > 50 and time_note < 700 :
#     print("quarter note")
#   if time_note > 700 and time_note < 1300:
#     print("half note")
#   if time_note > 1300:
#     print("note")
  
#   if(time_note > 1400):
#       print("note")
#   if(time_note < 800 and time_note > 1300):
#       
#   if(time_note > 100 and time_note < 700 ):
#       
#       
  #⬅️
#   if(imu_val[0] > 0.15):
#       
#      # print(last_move)
#       
#       if( +4000):
#           print("note")
#       elif(time.ticks_ms() > last_move +2000):
#           print("half note")
#       elif(time.ticks_ms() > last_move +1000):
#           print("quater note")
#       #⬅️
#           
#   if(imu_val[0] < -0.15):
      
     # print(last_move)
#       
#       if(time.ticks_ms() > last_move +4000):
#           print("note")
#       elif(time.ticks_ms() > last_move +2000):
#           print("half note")
#       elif(time.ticks_ms() > last_move +1000):
#           print("quater note")
# 
        
#   if(abs(imu_val[0])<0.15):
#       print("note")
#   if(abs(imu_val[0])<0.25 and abs(imu_val[0])>0.15):
#       print("half note")
#   if(abs(imu_val[0])<0.35 and abs(imu_val[0])>0.25):
#       print("quater note")

      
#     
#   
#   
#   time_array = []
#   
#   if(abs(imu_val[0])>=0.10):
#       time_array.append(one_time)
#       print(one_time)
#       one_time=0
      
#   if(imu_val[0]<0):
#       play_state == "UP"
#   else:
#       play_state == "DOWN"
#   
#   while(play_state == "UP"):
#       down_time = down_time +1
#       time.sleep_ms(100)
#   
#   print(down_time)

#   if(time.ticks_ms() > one_time +4000):
#       
#   elif(time.ticks_ms()> one_time +2000):
#       print("half note")
#   elif(time.ticks_ms()> one_time +1000):
#       print("quater note")
#       


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
