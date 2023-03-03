
import pygame
import random
import math
from spirte import Sprite

black=(0,0,0)


    

testlist=[]
downdrop=False
bouncelvl=250
draglog=False

coordx=0
coordy=0

vertpx=0
vertpy=0

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 244)
WIDTH = 1440
HEIGHT = 900
counter=0
multi=1
movedone=False
reflec_trigger1=True
reflec_trigger2=True
reflec_trigger3=True
stoptrig=False
pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basketball")
pygame.init()
  
RED = (SURFACE_COLOR)
  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basketball")
  
all_sprites_list = pygame.sprite.Group()

hoop=pygame.image.load("assets/images/hoops.png")
hoop_width = hoop.get_rect().width
hoop_height =hoop.get_rect().height
hoop = pygame.transform.scale(hoop, (hoop_width/6, hoop_height/6))

ball = pygame.image.load("assets/images/basketball.png")
ball_width = ball.get_rect().width
ball_height = ball.get_rect().height
ball = pygame.transform.scale(ball, (ball_width/7, ball_height/7))


 




object_ = Sprite(RED,20,20)
object_.rect.x = WIDTH/2
object_.rect.y = HEIGHT/2
myx=0
myy=object_.rect.y-object_.rect.x
WHITE = (255,255,255)
floor_=Sprite(WHITE,HEIGHT/2,WIDTH)
floor_.rect.x=0
floor_.rect.y=HEIGHT/2+20

GREEN = (SURFACE_COLOR)
hoop_=Sprite(GREEN,35,35)
hoop_.rect.x=random.randint(35,1415)
hoop_.rect.y=HEIGHT/2-150
  
all_sprites_list.add(object_)
all_sprites_list.add(floor_)
all_sprites_list.add(hoop_)
  
exit = True
trigger=False
clock = pygame.time.Clock()


intdif=1
 
# create a rectangular object for the


while exit:
    ev = pygame.event.get()
    for event in ev:

    # handle MOUSEBUTTONUP
        if draglog==True and trigger==False:
            coordx,coordy=pygame.mouse.get_pos()
            coordx-=25
            vertpx=object_.rect.x+object_.rect.x-coordx
            vertpy=(HEIGHT/2)-(object_.rect.y-coordy+object_.rect.y)
            
            print(2*vertpx-object_.rect.x)
            
            
            if vertpx-object_.rect.x>=0:
                pygame.draw.arc(screen,black,[object_.rect.x+8,HEIGHT/2-vertpy,2*(vertpx-object_.rect.x+8),HEIGHT-2*(HEIGHT/2-vertpy)],math.pi/2,math.pi,2)
            else:
                pygame.draw.arc(screen,black,[object_.rect.x-2*(object_.rect.x-vertpx)+5.5,HEIGHT/2-vertpy,2*(object_.rect.x-vertpx)+5.5,HEIGHT-2*(HEIGHT/2-vertpy)],0,math.pi/2,2)
           

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("hi")
            draglog=True
            
        elif event.type==pygame.MOUSEBUTTONUP and trigger==False:
            draglog=False
            intdif=1
            
       
            if object_.rect.y-coordy>=0:
                continue
            else:
                
                test=vertpy/4
                thing=vertpx-object_.rect.x
                trigger=True
            


            

            
        


    
   
    screen.blit(ball, (object_.rect.x-8.5,object_.rect.y-15))
    screen.blit(hoop, (hoop_.rect.x-14.5,hoop_.rect.y-15))
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    keys = pygame.key.get_pressed()
   
    
    
    

    if trigger:

        myx+=4
        

        
        
       

        object_.rect.x += intdif*(thing/test)
        
        

        object_.rect.y =(1/vertpy)*((myx-vertpy)**2)+((HEIGHT/2)-vertpy)
        testlist.append(object_.rect.y)
    
    if object_.rect.y==math.floor(HEIGHT/2-vertpy) and hoop_.rect.y>=math.floor(HEIGHT/2-vertpy):
       
        downdrop=True
    


   
    
    if hoop_.rect.x<=object_.rect.x+10<=hoop_.rect.x+35 and 315<=object_.rect.y+10<=340 and stoptrig==False and downdrop==True:

        counter+=1


        stoptrig=True
        hoop_.rect.x=random.randint(0,1415)
        

    reflec_trigger1=True
    reflec_trigger2=True
    

        

    
    if object_.rect.y>=HEIGHT/2 and trigger ==True:
        object_.rect.y=HEIGHT/2
        

        myx=0
        downdrop=False
     
        testlist=[]
        stoptrig=False
        vertpy=vertpy/1.4
        if vertpy<=1:
            trigger=False
            movedone=True
            

        
    if object_.rect.x>=WIDTH-27:
    
        intdif*=-1
        reflec_trigger1=False
    elif object_.rect.x<=7:
     
        intdif*=-1
        reflec_trigger2=False
        object_.rect.x=8
    

  # proceed events
    
    
    
    
        
    pygame.display.update()


 


    


    
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    
    
    clock.tick(60)


  
pygame.quit()