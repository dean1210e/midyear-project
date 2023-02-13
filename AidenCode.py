
import pygame
import random
import math
from spirte import Sprite
testlist=[]
downdrop=False
bouncelvl=250


COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 244)
WIDTH = 1440
HEIGHT = 900
counter=0
multi=1
reflec_trigger1=True
reflec_trigger2=True
stoptrig=False
pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basketball")
pygame.init()
  
RED = (167, 255, 244)
  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basketball")
  
all_sprites_list = pygame.sprite.Group()

  
ball = pygame.image.load("assets/images/basketball.png")
ball_width = ball.get_rect().width
ball_height = ball.get_rect().height
ball = pygame.transform.scale(ball, (ball_width/20, ball_height/20))

object_ = Sprite(RED,20,20)
object_.rect.x = WIDTH/2
object_.rect.y = HEIGHT/2
myx=0
myy=object_.rect.y-object_.rect.x
WHITE = (255,255,255)
floor_=Sprite(WHITE,HEIGHT/2,WIDTH)
floor_.rect.x=0
floor_.rect.y=HEIGHT/2+20

GREEN = (90,250,20)
hoop_=Sprite(GREEN,35,35)
hoop_.rect.x=random.randint(35,1415)
hoop_.rect.y=HEIGHT/2-150
  
all_sprites_list.add(object_)
all_sprites_list.add(floor_)
all_sprites_list.add(hoop_)
  
exit = True
trigger=False
clock = pygame.time.Clock()



 
# create a rectangular object for the


while exit:
    screen.blit(ball, (object_.rect.x-8.5,object_.rect.y-16))
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and reflec_trigger2:
        trigger=True
        intdif=-1
    elif keys[pygame.K_RIGHT] and reflec_trigger1:
        trigger = True
        intdif=1
    elif keys[pygame.K_UP]:
        trigger=True
        intdif=0
    
    
    

    if trigger:
        myx+=4
        

        object_.rect.x += intdif*2
        

        object_.rect.y =(1/bouncelvl)*((myx-bouncelvl)**2)+((HEIGHT/2)-bouncelvl)
        testlist.append(object_.rect.y)
    
    if object_.rect.y==math.floor(HEIGHT/2-bouncelvl) and hoop_.rect.y>=math.floor(HEIGHT/2-bouncelvl):
        print(bouncelvl)
        downdrop=True
    


   
    
    if hoop_.rect.x<=object_.rect.x+10<=hoop_.rect.x+35 and 315<=object_.rect.y+10<=340 and stoptrig==False and downdrop==True:

        counter+=1

        print(counter)
        stoptrig=True
        hoop_.rect.x=random.randint(35,1415)

    reflec_trigger1=True
    reflec_trigger2=True
    

        

    
    if object_.rect.y>=HEIGHT/2 and trigger ==True:
        object_.rect.y=HEIGHT/2
        

        myx=0
        downdrop=False
        print(min(testlist))
        testlist=[]
        stoptrig=False
        bouncelvl=bouncelvl/1.4
        if bouncelvl<=1:
            trigger=False
            bouncelvl=250
        
    if object_.rect.x>=WIDTH-27:
    
        intdif*=-1
        reflec_trigger1=False
    elif object_.rect.x<=7:
     
        intdif*=-1
        reflec_trigger2=False
    
    
    
        
       


 


    


    pygame.display.update()
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    
    
    clock.tick(60)


  
pygame.quit()