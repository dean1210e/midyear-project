import pygame
import button
screen_height = 900
screen_width= 1440
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Demo")

background = pygame.image.load('assets/images/menubg.jpg')
logo = pygame.image.load('assets/images/basketball1.png')
title = pygame.image.load('assets/images/title.png')
names = pygame.image.load('assets/images/names.png')

start_img = pygame.image.load('assets/images/playbutton.png').convert_alpha()
# playhover = pygame.image.load('assets/images/playhover.png').convert_alpha()
#quithover = pygame.image.load('assets/images/quithover.png').convert_alpha()
quit_img = pygame.image.load('assets/images/quitbutton.png').convert_alpha()


start_button = button.Button(575, 300, start_img, 1)
quit_button = button.Button(575, 400, quit_img, 1)


run = True
while run:

        # screen.fill((135, 206, 235))
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(title,(450,0))
        screen.blit(names,(500,75))
        # screen.blit(logo,(0,0))


        if start_button.draw(screen):
                print("START")
                
        if quit_button.draw(screen):
                run = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        pygame.display.update()

pygame.quit()
pygame.quit()
