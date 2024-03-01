import js as p5
from js import document
import random 
import threading
import time

data_string = None
data_list = None
sensor_val = None
button_val = None
button_state = 'UP'
count = 0
lst_n = set()
score = 0
program_state = "INTRO"
wrong = 0

class Note:
  def __init__(self,x,y,r,str,rc):
    self.x = x
    self.y = y
    self.r = r
    self.str = str 
    self.rc = rc
    self.state = "None"
  
  def draw(self,k):

    p5.push()
    p5.translate(self.x,self.y)

    if(self.str == "quick"):
      p5.noFill()
      
      p5.text("1T", 10, 20)
    if(self.str == "slow"):
      #p5.text("1F", 10, 20)
      p5.fill(255, 255, 255,40)
      

    self.success_rect(k)

    if(self.state == "True"):
      p5.fill(255,204,0)
      
    if(self.state == "False"):
      p5.fill(255,0,0)

    if(self.r < self.rc):
      self.rc = self.rc - 2

    # else:
    #   p5.fill(255,0,0)
    #     #p5.text("2F", 10, 40)
    #     
    #     #p5.text(self.rc, 10, 50)
    #     self.r = 0
    

    #p5.fill(255)
    p5.stroke(255,204,0)
    p5.ellipse(0,0,self.r,self.r)
    p5.ellipse(0,0,self.rc,self.rc)

    #p5.text(self.r, 10, 70)
    p5.pop()
  
  def circle_animation(self):
    #p5.text(self.r, 10, 70)
    if(self.r > 0):
      self.r  = self.r - 1

  def success_rect(self,k):
    #p5.text(self.rc, 10, 30)
    #p5.text(self.state, 10, 50)
    if(self.r - self.rc  < 0 and self.rc > 45):
      if(k == self.str):
        self.state = "True"
      #p5.text("pass", 10, 30)
        if(self.success() and  self.rc > 0):
        #p5.text("2T", 10, 40)
          p5.fill(255,204,0)
          self.rc = self.rc - 2 
          self.r = 0
      elif(self.state == "None"):
        self.state = "False"
    elif(self.r - self.rc  < 0 and self.state == "None"):
      self.state = "False"

      
          

  
  def success(self):
      p5.text("true", 10, 70)
      if(self.r < 2):

        return True
      else:
        return False
    


      
img1 = p5.loadImage('1.png')
img2 = p5.loadImage('2.png')
img3 = p5.loadImage('3.png')
img4 = p5.loadImage('4.png')
img5 = p5.loadImage('5.png')
img6 = p5.loadImage('6.png')
    

# load image data and assign it to variable:
bg_img = p5.loadImage('bg.png')

# load font data and assign it to variable:
jellee_font = p5.loadFont('Jellee.otf')

# load sound data and assign it to variable:
sound = p5.loadSound('knock.wav') 

def setup():
  p5.createCanvas(300, 300)
  # change mode to draw rectangles from center:
  p5.rectMode(p5.CENTER)
  # change mode to draw images from center:
  p5.imageMode(p5.CENTER)
  # change stroke cap to square:
  p5.strokeCap(p5.SQUARE)

randiii = random.random()*6
def draw():
  
  p5.background(125)

  global data_string, data_list,randiii
  global sensor_val, button_val,img1,img2,img3,img5,img4,img6
  global button_state,count,random,count,score,bg_img,program_state,wrong

  p5.tint(255, 127)

  p5.image(bg_img,150,150,300,300)


  # assign content of "data" div on index.html page to variable:
  text1 = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  #data_list = data_string.split(',')

  # assign 1st item of data_list to sensor_val:
  #rrr = (data_list[0])
  # assign 2nd item of data_list to sensor_val:
  #button_val = int(data_list[1])
  p5.text(text1,10,20)

  if(program_state == "INTRO"):
    p5.noFill()
    p5.stroke(255,204,0)
    p5.ellipse(100,150,50,50)
    p5.text("hard & quick", 65,200)

    p5.fill(255,255,255,50)
    p5.stroke(255,204,0)
    p5.ellipse(200,150,50,50)
    p5.text("slow & soft", 165,200)
    if(text1 == "quick"):
        program_state = "PLAY"
  
  p5.text(wrong,10,60)
  
  if(wrong >= 5):
    program_state = "END"

  if(program_state == "END"):
    if(score >5):
      p5.tint(255, 255)
      p5.text("Your Luck Today",10,70)
      if(randiii < 1):
        
        p5.image(img1,150,150,120,250)
      elif(randiii < 2):
        p5.image(img2,150,150,120,250)
      elif(randiii < 3):
        p5.image(img3,150,150,120,250)
      elif(randiii < 4):
        p5.image(img4,150,150,120,250)
      elif(randiii < 5):
        p5.image(img5,150,150,120,250)
      else:
        p5.image(img6,150,150,120,250)
    else:
      p5.text("try again",100,150)

    if(text1 == "quick"):
        program_state = "PLAY"
    




  if(program_state == "PLAY"):
    if(count <2):

      randx = random.random() * 200 +50  
      randy = random.random()*200 +50
      p5.text(randy,10,10)
      randk = random.random()
      randr = random.random() * 250+40
      if(randk < 0.5):
        str = "quick"
      else:
        str ="slow"

      n = Note(randx, randy, randr , str, 50)
      lst_n.add(n)  

      count = count +1
      #t = "f"
      
  

    p5.text(score, 10, 40)
    notes_to_remove = set()
    for n in lst_n:
    # t = "f"
      n.draw(text1)
      n.circle_animation()
      if(n.rc <2):
        if(n.state == "True"):
          score = score +1
          sound.play()
        if(n.state == "False"):
          wrong = wrong +1
          
        notes_to_remove.add(n)
    
        count = count -1 

    
    lst_n.difference_update(notes_to_remove)


      


      





    


  # p5.noStroke()  # disable stroke
  # # fill function can take 1 argument (gray)
  # p5.fill(0)  # black fill
  
  # # draw circle changing size with sensor data:
  # # ellipse function takes (x, y, width, height)
  # # map function takes (value, in_min, in_max, out_min, out_max)
  # circle_size = p5.map(sensor_val, 0, 255, 25, 100)
  # p5.ellipse(75, 75, circle_size, circle_size)
  
  # # draw square changing color with sensor data:
  # # fill function can take (red, green, blue)
  # p5.fill(sensor_val, 0, 255 - sensor_val)  
  # # rectangle function takes (x, y, width, height)
  # p5.rect(225, 75, 100, 100)

  # # draw text:
  # p5.fill(255)  # white fill
  # # use font installed on computer:
  # p5.textFont('Courier')
  # p5.textSize(18)
  # p5.text(sensor_val, 190, 65)
  # # use font from loaded font file:
  # p5.textFont(jellee_font)
  # p5.textSize(24)
  # p5.text(button_val, 190, 100)

  # # draw lines responding to button data:
  # for i in range(8):
  #   if(button_val == 0): 
  #     p5.strokeWeight(i+1)
  #   else: 
  #     p5.strokeWeight(8-i)
  #   p5.stroke(0)
  #   # line function takes (x1, y1, x2, y2)
  #   x1 = x2 = 25 + i * 14
  #   y1 = 175
  #   y2 = 275
  #   p5.line(x1, y1, x2, y2)

  # # play sound when button is pressed:
  # if(button_val == 1) and (button_state == 'UP'):
  #   sound.play()
  #   button_state = 'DOWN'
  # elif(button_val == 0):
  #   button_state = 'UP'

  # # fill function can take (r, g, b, alpha):
  # p5.fill(0, 255, 0, 150)  # transparent green
  # # change color mode to HSB with transparency:
  # p5.colorMode(p5.HSB, 255, 255, 255, 255) 
  # # fill function can take (h, s, b, alpha):
  # p5.fill(255, 255, 255, 150)  # transparent red
  # p5.noStroke()
  # p5.rect(200, 200, 50, 50)
  # # change mode back to RGB:
  # p5.colorMode(p5.RGB)

  # # draw image rotating with sensor data:
  # p5.push()  # save transformation coordinates
  # p5.translate(225, 225)  # move coordinates by (x, y)
  # # use sensor_val as degrees converted to radians:
  # angle = p5.radians(sensor_val)  
  # p5.rotate(angle)  # rotate coordinates
  # # tint function can change transparency of image
  # # fint function takes (r, g, b, alpha)
  # p5.tint(255, 255, 255, 150)
  # # image function takes (image, x, y, width, height)
  # p5.image(swirl_img, 0, 0, 100, 100)
  # p5.pop()  # restore transformation coordinates
