# import pygame

# pygame.init()

# width = 1024
# height = 576

# background = pygame.image.load("assets/images/background.gif")


# screen = pygame.display.set_mode((width,height))
# base = pygame.image.load("assets/images/base.png")
# basketball = pygame.image.load("assets/images/basketball.png")


# def main():
#     gameOn = True
#     baseX= 0
#     baseY= height-60
#     ballX = 120
#     ballY = baseY - 60
#     gravity = 10
#     bouncing = 25


#     while gameOn:

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 gameOn = False

        
#         screen.blit(background, (0,0))
#         screen.blit (base, (baseX,baseY))
#         screen.blit(basketball, (ballX,ballY))

#         ballY -= bouncing
#         bouncing -= 1
#         ballY += gravity

#         pygame.display.update()

# if __name__ == "__main__":
#     main()


