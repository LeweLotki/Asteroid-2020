import pygame
import random

position=[180, 300, 40, 40]

fire=0
i=0
points=0
backy=-400

size = [400,400]
cometImg=pygame.image.load('images/comet.png')
back=pygame.image.load('images/background2.png')
back=pygame.transform.scale(back, (400,800))
shipImg = pygame.image.load('images/ship.png')
shipImg = pygame.transform.scale(shipImg, (40, 40))
bulletImg=pygame.image.load('images/bullet.png')
bulletImg=pygame.transform.scale(bulletImg,(10,20))
planet1=pygame.image.load('images/planet1.png')
planet1=pygame.transform.scale(planet1,(150,150))
planet2=pygame.image.load('images/planet2.png')
planet2=pygame.transform.scale(planet2,(200,200))
menuImg=pygame.image.load('images/textmenu.png')

def move_right(list):
    if list[0]>=360:
       pass
    else:
       list[0]+=2

def move_left(list):
    if list[0]<=0:
       pass
    else:
       list[0]-=2

class bullet:
   def __init__(self,list):
    self.x=list[0]
    self.y=list[1]
    self.num=1
   def update(self):
    self.y-=5
   def render(self,bulletImg):
    screen.blit(bulletImg,(self.x+15,self.y))
    #pygame.draw.rect(screen, b, [self.x+15, self.y, 10, 10]) 
    if self.num==0:
       self.y-=400
class comet:
    def __init__(self):
        self.x=random.randint(0,400)
        self.y=-100
        self.sizex=random.randint(20,50)
        self.sizey=random.randint(20,50)
        self.vx=random.randint(0,3)
        self.vy=random.randint(1,3)
        self.num=1
        if self.vx==2:
           self.vx=-1
        if self.vx==3:
           self.vx=0
    def update(self):
        if self.x<0 or self.x+self.sizex>400:
           self.vx=-self.vx
        self.y+=self.vy    
        self.x+=self.vx              
    def render(self,cometImg):
        cometImg=pygame.transform.scale(cometImg,(self.sizex,self.sizey))
        screen.blit(cometImg,(self.x,self.y))
        
        if self.num==0:
            self.y+=500      
bulletlist=[]
list_temp=[]

cometlist=[]
list_temp2=[]

bl = (  0,   0,   0)
w = (255, 255, 255)
b =  (  0,   0, 255)
g = (  0, 240,   0)
r =   (255,   0,   0)
gr=(200,200,200)
y=(255,255,0)
o=(255,140,0)

pygame.init()

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Asteroid 2020")

font=pygame.font.SysFont('Courier', 12) 
text=font.render('POINTS:'+str(points), True, w, bl) 
textRect=text.get_rect() 
textRect.center=(30,10)

font2=pygame.font.SysFont('Courier', 30) 
text2=font2.render('GAME OVER', True, r, bl) 
textRect2=text2.get_rect() 
textRect2.center=(200,150)

font3=pygame.font.SysFont('Courier',18)
text3=font3.render('press <<SPACE>> to start',True, r)
textRect3=text3.get_rect()
textRect3.center=(200,220)

done=False
done2=False
done3=False
menu=False
clock=pygame.time.Clock()

while not done:
 while not menu and not done:
  
  font3=pygame.font.SysFont('Courier',18)
  text3=font3.render('press <<SPACE>> to start',True, r)
  textRect3=text3.get_rect()
  textRect3.center=(200,220)

  
  for event in pygame.event.get():
   if event.type == pygame.QUIT: 
     done=True
  
  key=pygame.key.get_pressed() 
  clock.tick(100)
  
  if key[pygame.K_SPACE]: 
     menu=True
  
  text3=font3.render('press <<SPACE>> to start',True, r)
  
  screen.fill(bl)
  screen.blit(back,(0,backy))
  screen.blit(text3,textRect3)
  screen.blit(menuImg,(10,150))
  screen.blit(planet1,(10,-20))
  screen.blit(planet2,(230,250))
  pygame.display.flip()
 while not done2 and not done:
 
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
     done=True
 
  backy+=1
  if backy==0:
     backy=-400
  key=pygame.key.get_pressed() 
 
  k=random.randint(1,50)
 
  if i==100:
      i=0
      points+=1
  clock.tick(100)



  if key[pygame.K_a] or key[pygame.K_LEFT]:
     move_left(position)
  elif key[pygame.K_d] or key[pygame.K_RIGHT]:
     move_right(position)
 
  if key[pygame.K_SPACE]: 
     if i>10:
         bulletlist.append(bullet(position))
         i=0
 
  if k==10:
     cometlist.append(comet())
 
  screen.fill(bl)
  screen.blit(back,(0,backy))
  font=pygame.font.SysFont('Courier', 12)
  textRect.center=(30,10)
  text=font.render('POINTS:'+str(points), True, w, bl) 
  screen.blit(text, textRect)
  screen.blit(shipImg, position)
   
  for n in bulletlist:
     n.update()
     n.render(bulletImg)
     if n.y > -10:
        list_temp.append(n)
  for n in cometlist:
     n.update()
     n.render(cometImg)
     if n.y <450:
        list_temp2.append(n)
    #print(len(bulletlist))
 #print(len(cometlist))
  for n in cometlist:
      if n.y+n.sizey in range(300,300+n.sizey):  #310
        #print('Im here')
         for val in range(n.x,n.x+n.sizex):
             if val in range(position[0],position[0]+40):
                done3=False
                done2=True
               #+m.sizey-30 może być po m.y
  for m in cometlist:
     for n in bulletlist:
         if n.y in range(m.y,m.y+m.sizey):
             for val in range(n.x-10,n.x+20):      #dodałem 10 i odjąłem 10 z lewej
                 if val in range(m.x,m.x+m.sizex):
                    m.num=0
                    n.num=0
                   #fire+=1
                   #print(fire)
                
 
  i+=1
  bulletlist.clear()
  bulletlist=list_temp
  list_temp=[]
  cometlist.clear()
  cometlist=list_temp2
  list_temp2=[]
 #print(points)
  pygame.display.flip()

 while not done3 and not done:
  
  for event in pygame.event.get():
   if event.type == pygame.QUIT: 
     done=True
  key=pygame.key.get_pressed() 
  clock.tick(100)
  
  font3=pygame.font.SysFont('Courier',14)
  text3=font3.render('press << R >> to restart',True, r)
  textRect3=text3.get_rect()
  textRect3.center=(200,250)

  
  if key[pygame.K_r]:
     points=0
     cometlist.clear()
     bulletlist.clear()
     position[0]=180
     font=pygame.font.SysFont('Courier', 12)
     textRect.center=(30,10)
     done2=False
     done3=True
  
  
  screen.fill(bl)
  screen.blit(text2, textRect2)
  screen.blit(text3, textRect3)
  font=pygame.font.SysFont('Courier', 16) 
  text=font.render('POINTS:'+str(points), True, r, bl) 
  textRect.center=(200,200)
  screen.blit(text, textRect)
 
  pygame.display.flip()
 
pygame.quit()

