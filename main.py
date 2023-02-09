import pygame
pygame.init()

# global variable
width = 1024
height = 576
screen = pygame.display.set_mode((width, height))
gameOn = True

#colors
red = (255,0,0)
black = (0,0,0)

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
<<<<<<< HEAD
    baseY = 420
=======
    baseY = 470
    ballX = 120
    ballY = baseY - 60
    gravity = 10
    bouncing = 25
    baseX_vel = 0
    baseY_vel = 0
    gameover= False
    score = 0
    speed = 0
    basket_score = 0
    score = 0
    speed_accelerating = False
    basketX = 0
    basketY = 0
    ScreenText = 0
>>>>>>> 4ccf79c5bd1a455dfe0ea6f1d4e6e46ce67f882f

    while gameOn:
        # taking event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False

        screen.blit(background, (0, 0))
        # screen.blit(base, (baseX, baseY))
        pygame.display.update()

        #ball in basket
        # if(ballX+ball.get_width() >= basketX and ballX <= basketX.basket.get_width and ballY > basketY and ballY <= basketY.basket.get_height()):
        #     basket_score += 100

        speed += 0.001
        #speeding up score
        score += int(speed)

        #displaying text
        # ScreenText(f"Score{score}", black, 10,40,size=20)
        # ScreenText(f"Basket Score{basket_score}")

if __name__ == "__main__":
    main()
