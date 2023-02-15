import pygame

pygame.init()

#global variable
width = 1024
height = 576
screen = pygame.display.set_mode((width, height))
gameOn = True

# background =  pygame.image.load("assests/images/SKY.gif")
background = pygame.image.load("assets/images/bg.png.mp4")


while gameOn:
    screen.blit(background, (0,0))           

    #taking event
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            gameOn=False


    pygame.display.flip()



