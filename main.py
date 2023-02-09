import pygame

pygame.init()

# global variable
width = 1024
height = 576
screen = pygame.display.set_mode((width, height))
fps = 20
clock = pygame.time.Clock()


background = pygame.image.load("assets/images/basketballbg.gif")
bg_width = background.get_rect().width
bg_height =background.get_rect().height
# background = pygame.transform.scale(background, (bg_width/1.7, bg_height/1.3))

# base = pygame.image.load("assets/images/basketball.png")
# base_width = base.get_rect().width
# base_height = base.get_rect().height
# base = pygame.transform.scale(base, (base_width*2.6, base_height*2.6))
ball = pygame.image.load("assets/images/basketball.png")
ball_width = ball.get_rect().width
ball_height = ball.get_rect().height
ball = pygame.transform.scale(ball, (ball_width/16.5, ball_height/16.5))

def main():
    gameOn = True
    baseX = 0
    baseY = 470
    ballX = 120
    ballY = baseY - 60
    gravity = 10
    bouncing = 25

    while gameOn:
        # taking event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bouncing = 25

        screen.blit(background, (0, 0))
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

if __name__ == "__main__":
    main()
