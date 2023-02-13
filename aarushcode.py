import pygame
pygame.init()

# global variable
width = 1024
height = 576
screen = pygame.display.set_mode((width, height))
fps = 20
clock = pygame.time.Clock()

#colors
red = (255,0,0)
black = (0,0,0)

basket = pygame.image.load("assets/images/basket.png")
basket_width = basket.get_rect().width
basket_height =basket.get_rect().height

ball = pygame.image.load("assets/images/basketball.png")
ball_width = ball.get_rect().width
ball_height = ball.get_rect().height
ball = pygame.transform.scale(ball, (ball_width/16.5, ball_height/16.5))

bg_img = pygame.image.load("assets/images/bg.png")
bg_img = pygame.transform.scale(bg_img,(700,700))

def main():
    gameOn = True
    baseX = 0
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

    while gameOn:
        # taking event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bouncing = 25

        screen.blit(basket, (0, 0))
        # screen.blit(base, (baseX, baseY))
        screen.blit(ball, (ballX, ballY))

        # bouncing
        ballY -= bouncing
        bouncing -= 1
        ballY += gravity
        if(ballY > baseY - 20):
            bouncing = 25

        pygame.display.update()
        clock.tick(fps)

        #ball in basket
        # if(ballX+ball.get_width() >= basketX and ballX <= basketX.basket.get_width and ballY > basketY and ballY <= basketY.basket.get_height()):
        #     basket_score += 1

        speed += 0.001
        #speeding up score
        score += int(speed)

        #displaying text
        # ScreenText(f"Score{score}", black, 10,40,size=20)
        # ScreenText(f"Basket Score{basket_score}")

if __name__ == "__main__":
    main() 

    