import pygame
import playbutton
import quitbutton
import xbutton
import random
import math
from spirte import Sprite
import tkinter as tk

screen_height = 900
screen_width= 1440

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basketball")

background = pygame.image.load('assets/images/menubg.jpg')
title = pygame.image.load('assets/images/title.png')
names = pygame.image.load('assets/images/names.png')

start_img = pygame.image.load('assets/images/playbutton.png').convert_alpha()
quit_img = pygame.image.load('assets/images/quitbutton.png').convert_alpha()
x_img = pygame.image.load('assets/images/x_button.png').convert_alpha()

start_button = playbutton.Button(575, 285, start_img, 1)
quit_button = quitbutton.Button(575, 400, quit_img, 1)
x_button = xbutton.Button(10, 10, x_img, 1)


run = True
while run:
        
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(title,(450,0))
        screen.blit(names,(500,75))


        if start_button.draw(screen):


        if quit_button.draw(screen):
                run = False

        if x_button.draw(screen):
             run = False

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()

pygame.quit()




