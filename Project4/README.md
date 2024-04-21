This is my Github
## FINAL PROJECT - CodeBlock

### Project Brief

A Modular Programming Prototyping Kit that could help users to interact and learn about p5.js. 
The Kit includes Value Modular, Shape Modular, and For Loop Modular. The user could connect Value Modular with SHape Modular to change the position, size. Also Connect Value Moduler and Shape Modular with For Loop Modular to run the for loop

### Project OutCome

### Project Ideation
![Initial Idea](initialidea.jpg)

![approac1](idea2.png)

![approac1](idea3.jpg)

![all imput](input.jpg)

### Hardware
- Atom3 Board * 2
- Potentiometer * 5
- light sensor * 1
- wire * n

Wireconnection of Value Module
![wireconnection of Value Module](Value_Module_Connection.jpg)  

Wireconnection of Shape Module
Specially, due to the limitation of the input on Atom3, I modified the wire and connected to pin1,2,6,8
![wireconnection of Shape Module](Shape_Connection.jpg)  
![wireconnection of Shape Module](Shape_Module_Connection.jpg)  

Wireconnection of For Loop Module
![wireconnection of Shape Module](For_Connection.jpg)  

### Firmware
This project includes bluetooth communication of two atom3 board, and atom3 board send data to the web. 

[Bluetooth Connection](thonny/bluetooth.py)

The bluetooth imported and use .write() method to send data of for_modlue_value, which is a Potentiometer value shows the number of loops. and light sensor value, which tells whether shape module is connected to the for loop module. It sent those 2 datas to other atom 3 board

```
  for_module_value = for_module.read()
  light_module_value = light_module.read()
  #print('write to bleuart..')
  print(str(for_module_value)+ "," +str(light_module_value))
  #ble_server.write('hello M5!')
  ble_server.write(str(for_module_value)+ "," +str(light_module_value))`
```
