import pygame

pygame.init()

# global variable
width = 700
height = 550
screen = pygame.display.set_mode((width, height))
gameOn = True


background = pygame.image.load("assets/images/basketballbg.gif")
bg_width = background.get_rect().width
bg_height =background.get_rect().height
background = pygame.transform.scale(background, (bg_width/1.7, bg_height/1.3))


# base = pygame.image.load("assets/images/road.png")
# base_width = base.get_rect().width
# base_height = base.get_rect().height
# base = pygame.transform.scale(base, (base_width*2.6, base_height*2.6))

def main():
    gameOn = True
    baseX = 0
    baseY = 420

    while gameOn:
        # taking event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        screen.blit(background, (0, 0))
        screen.blit(base, (baseX, baseY))
        pygame.display.update()

if __name__ == "__main__":
    main()
