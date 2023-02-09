import pygame

pygame.init()

width=700
height=550

background = pygame.image.load("assets/images/background.gif")


screen = pygame.display.set_mode((width,height))
base = pygame.image.load("assets/images/base.png")
basketball = pygame.image.load("assets/images/basketball.png")


def main():
    gameOn = True
    baseX=0
    baseY=heigth-60 
    while gameOn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        screen.blit(background, (0,0))
        screen.blit (base, (baseX,baseY))
        pygame.display.update()




