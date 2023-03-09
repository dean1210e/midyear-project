import pygame, sys
import playbutton
import quitbutton
import xbutton
import playagain
import random
import math
from spirte import Sprite
import tkinter as tk
from pygame.locals import *
from pygame import mixer

screen_height = 900
screen_width= 1440

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basketball")

background = pygame.image.load('assets/images/menubg.jpg')
title = pygame.image.load('assets/images/title.png')
names = pygame.image.load('assets/images/names.png')

pygame.mixer.init()
mixer.music.load("backgroundmusic.mp3")
mixer.music.play(-1)

start_img = pygame.image.load('assets/images/playbutton.png').convert_alpha()
quit_img = pygame.image.load('assets/images/quitbutton.png').convert_alpha()

start_button = playbutton.Button(575, 285, start_img, 1)
quit_button = quitbutton.Button(575, 400, quit_img, 1)
entered=True

run = True
while run:
        
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(title,(450,0))
        screen.blit(names,(500,75))

        if start_button.draw(screen):
               
                black=(0,0,0)
                time=9000
                scored=False
                final=False
                testlist=[]
                downdrop=False
                bouncelvl=250
                draglog=False
                pointstop=False

                coordx=0
                coordy=0

                vertpx=0
                vertpy=0

                COLOR = (255, 100, 98)
                SURFACE_COLOR = (167, 255, 244)
                WIDTH = 1440
                HEIGHT = 900
                counter=0
                tcounter=0
                multi=1
                movedone=False
                reflec_trigger1=True
                reflec_trigger2=True
                reflec_trigger3=True
                scorer=200
                tscorer=200
                stoptrig=False
                hoopcount = 0
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

                my_font=pygame.font.SysFont("minecraftia",30)
                text_surface=my_font.render('SCORE:'+str(counter),False,(0,0,0))
                hoopcount_surface = my_font.render('HOOPS:'+str(hoopcount),False,(0,0,0))

                hoop=pygame.image.load("assets/images/hoops.png")
                hoop_width = hoop.get_rect().width
                hoop_height =hoop.get_rect().height
                hoop = pygame.transform.scale(hoop, (hoop_width/6, hoop_height/6))

                ball = pygame.image.load("assets/images/basketball1.png")
                ball_width = ball.get_rect().width
                ball_height = ball.get_rect().height
                ball = pygame.transform.scale(ball, (ball_width/7, ball_height/7))

                x_img = pygame.image.load('assets/images/x_button.png').convert_alpha()
                x_button = xbutton.Button(0, 830, x_img, 0.5)

                background1=pygame.image.load("assets/images/gamebg.jpg")
                background1_width = background1.get_rect().width
                background1_height = background1.get_rect().height
                background1 = pygame.transform.scale(background1, (WIDTH, HEIGHT/2+20))


                


                scorevariable=400

                object_ = Sprite(RED,20,20)
                object_.rect.x = WIDTH/2+scorevariable
                object_.rect.y = HEIGHT/2
                myx=0
                myy=object_.rect.y-object_.rect.x
                WHITE = (255,255,255)
                floor_=Sprite(WHITE,HEIGHT/2,WIDTH)
                floor_.rect.x=0
                floor_.rect.y=HEIGHT/2+20

                GREEN = (SURFACE_COLOR)
                hoop_=Sprite(GREEN,35,35)
                hoop_.rect.x=1400
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
                    if trigger==False:
                        pointstop=False
                    my_font=pygame.font.SysFont('minecraftia',150)
                    my_font1=pygame.font.SysFont('minecraftia',100)
                    
                    

                    if time >0:
                        time-=1
                        text_surface1=my_font.render('TIME: '+str(math.floor(time/3600))+":"+f"{(math.floor((time%3600)/60)):02d}",False,(0,0,0))
                    text_surface = my_font.render('SCORE: '+str(counter),False,(0,0,0))
                    
                    if time<=0:
                        
                        final=True
                        text_surface1=my_font1.render("TIME'S UP! Your final score: "+str(counter),False,(0,0,0) )
                        
                        playagain_img = pygame.image.load('assets/images/playagain.png').convert_alpha()
                        playagain_button = playagain.Button(215, 700, playagain_img, 1)

                        if playagain_button.draw(screen):
                            run = False
                            exit=False


                    ev = pygame.event.get()
                    for event in ev:

                    # handle MOUSEBUTTONUP
                    
                        if draglog==True and trigger==False and final==False:
                            coordx,coordy=pygame.mouse.get_pos()
                            coordx-=10
                            vertpx=object_.rect.x+object_.rect.x-coordx
                            vertpy=(HEIGHT/2)-(object_.rect.y-coordy+object_.rect.y)
       
                        if event.type == pygame.MOUSEBUTTONDOWN and trigger==False and final==False:

                            draglog=True
                            
                        elif event.type==pygame.MOUSEBUTTONUP and trigger==False and final==False:
                            pointstop=False
                            draglog=False
                            intdif=1
                            thingy=True
                            
                            if object_.rect.y-coordy>=0:
                                continue
                            else:
                                
                                test=vertpy/4
                                thing=vertpx-object_.rect.x
                                trigger=True
                            
                    screen.blit(background1,(0,0))
                    if draglog==True and trigger==False:
                        if vertpx-object_.rect.x>=0:
                                    pygame.draw.arc(screen,black,[object_.rect.x+8,HEIGHT/2-vertpy,2*(vertpx-object_.rect.x),HEIGHT-2*(HEIGHT/2-vertpy)],math.pi/2,math.pi,2)
                        else:
                                    pygame.draw.arc(screen,black,[object_.rect.x-2*(object_.rect.x-vertpx)+10,HEIGHT/2-vertpy,2*(object_.rect.x-vertpx),HEIGHT-2*(HEIGHT/2-vertpy)],0,math.pi/2,2)
                    screen.blit(ball, (object_.rect.x-8.5,object_.rect.y-15))
                    
                    screen.blit(hoop, (hoop_.rect.x-14.5,hoop_.rect.y-15))
                    screen.blit(text_surface,(450,525))
                    if time >0:
                        screen.blit(text_surface1,(450,700))
                    else:
                        screen.blit(text_surface1,(200,650))
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit = False
                    keys = pygame.key.get_pressed()
                
                    if trigger:

                        myx+=4

                        if pointstop==False:
                            object_.rect.x += intdif*(thing/test)
                        
                        object_.rect.y =(1/vertpy)*((myx-vertpy)**2)+((HEIGHT/2)-vertpy)
                        testlist.append(object_.rect.y)
                    
                    if object_.rect.y==math.floor(HEIGHT/2-vertpy) and hoop_.rect.y>=math.floor(HEIGHT/2-vertpy):
                    

                        downdrop=True
                    

                    if hoop_.rect.x<=object_.rect.x+10<=hoop_.rect.x+35 and 315<=object_.rect.y+10<=340 and stoptrig==False and downdrop==True:

                        if pointstop==False:
                            counter+=tscorer
                            tcounter+=1
                            scored=True
                            
                            dog = mixer.Sound("swoosh.wav")
                            dog.play()
                                           
                        print(counter)
                        pointstop=True
                        object_.rect.x=hoop_.rect.x+10
                        


                        stoptrig=True
                
                        

                    reflec_trigger1=True
                    reflec_trigger2=True
                    

                        

                    
                    if object_.rect.y>=HEIGHT/2 and trigger ==True:
                        object_.rect.y=HEIGHT/2
                        

                        myx=0
                        downdrop=False

                    
                        testlist=[]
                        stoptrig=False
                        vertpy=vertpy/1.6
                        if scored==True and thingy==True:
                            vertpy=100
                            thingy=False
                        elif thingy==True:
                            thingy=False
                            if tscorer>50:
                                tscorer-=50
                             

                        
                        if vertpy<=1:
                            if scored==True:
                                
                                scorevariable-=60*(1.08**tcounter)
                                scorer+=100
                                tscorer=scorer
                                scored=False
                        
                            trigger=False
                            movedone=True
                            object_.rect.x=WIDTH/2+scorevariable
                            

                        
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

                    if x_button.draw(screen):
                        run = False
                        exit=False


                
                pygame.quit()


        if quit_button.draw(screen):
                exit=False
                run = False

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                        exit=False

        pygame.display.update()

pygame.quit()




