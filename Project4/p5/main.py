import js as p5
from js import document

data_string = "0,0,0,0,0,0,0,0"
data_list = [0,0,0,0,0,0,0,0]
button_state = 'UP'
value_x = 0
for_value = 0
value_y = 0
for_state = "Off"
shape_value = "Rect"
position_x = 0
position_y =0


def setup():
  p5.createCanvas(1600, 950)
  # change mode to draw rectangles from center:
  p5.rectMode(p5.CENTER)
  # change mode to draw images from center:
  p5.imageMode(p5.CENTER)
  # change stroke cap to square:
  p5.strokeCap(p5.SQUARE)

def draw():
  
  global data_string, data_list, value_x, value_y,for_value, for_state,shape_value,position_x, position_y
  p5.background(position_x/50 +100,position_y/50+100, value_x/50+100)

  # # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # # split data_string by comma, making a list:
  data_list = data_string.split(',')





  if(len(data_list)>3):
    position_x = int(data_list[0])

    position_y = int(data_list[1])

    value_x = int(data_list[2])

    value_y = int(data_list[3])

    shape_value = str(data_list[4])

    for_value = int(data_list[5])

    for_state = data_list[6]

  p5.noFill()
  # position_x = 2344
  # position_y =12
  # for_state = "On"
  # for_value = 200
  # value_x = 2323
  # value_y = 3422
  # shape_value = "Hex"


  p5.translate(800,950/2)

  p5.push()
  p5.strokeWeight(4)
  p5.stroke(0)

 
  if(for_state == "On"):
     for i in range (int(for_value /200)) :
      
      p5.push()
      
      p5.rotate(p5.PI*2 / int(for_value /200) * i)
      
      p5.translate((position_x - 2000)/2,(position_y- 2000)/5)
      if(shape_value == "Rect"):
        p5.rect(0, 0, value_x / 4, value_y / 8)
      elif(shape_value == "Hex"):
        polygon(0, 0, value_x / 4, 6)
      elif(shape_value == "Oct"):
        polygon(0, 0, value_x / 4, 8)
      else:
        p5.ellipse(0,0,value_x /4, value_y / 5) 
 
      p5.pop()
      # elif shape_value == "Hex":
      #   p5.polygon(0, 0, value_x, 6); 
      # elif shape_value == "Oct":
      #   p5.polygon(0, 0, value_x, 8);  
  else:
    p5.translate((position_x - 2000)/2,(position_y- 2000)/5)
    if(shape_value == "Rect"):
      # print(value_x)
      p5.rect(0, 0, value_x / 4, value_y / 8)
    elif(shape_value == "Hex"):
        polygon(0, 0, value_x / 4, 6)
    elif(shape_value == "Oct"):
        polygon(0, 0, value_x / 4, 8)
    else:
        # print(shape_value)
        p5.ellipse(0,0,value_x / 4, value_y / 8) 

        
  
     
  # if shape_value == "Rect":
  #   p5.rect(0, 0, 80, 20)
    
  # elif shape_value == "Hex":
  #   p5.polygon(0, 0, value_x, 6); 
  # elif shape_value == "Oct":
  #   p5.polygon(0, 0, value_x, 8);  


  p5.pop()



  # p5.ellipse(0, 0, value_x/20, value_y/20)

def  polygon(x, y, radius, npoints):
  angle = p5.PI*2 / npoints
  p5.beginShape()
  i = 0
  while(i<p5.PI*2):
   
    sx = x + p5.cos(i) * radius
    sy = y + p5.sin(i) * radius
    p5. vertex(sx, sy)
    i += angle
  
  p5.endShape(p5.CLOSE)
