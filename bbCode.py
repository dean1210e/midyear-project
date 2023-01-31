#CODE FOR THE GAME
#import modules
import turtle 
import random
import time

#set up the screen

wn = turtle.Screen()
wn.setup(700,500)
wn.colormode(255)
wn.bgcolor(0, 180, 90)
wn.tracer(0)
wn.title("Shooting Hoops")

#basket turtle

basket = turtle.Turtle()
basket.showturtle()
basket.penup()
basket.goto(0,150)
wn.register_shape("hoopl.gif")
basket.shape("hoopl.gif")

#ball turtle

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("organge")
ball.shapesize(2.5)
ball.goto(0, -180)

#pen turtle

pen = turtle.Turtle()
ball.penup()
ball.hideturtle()
pen.penup()
pen.goto(-330, -230)
pen.write("Score: 0", font =('Helvetica', 30))

#shots turtle

pen2 = turtle.Turtle()
pen2.penup()
pen2.hideturtle()
pen2.goto(100, -230)
pen2.write("Shots: 0", font=("Helvetica", 30 ))

#accuracy title

pen3 = turtle.Turtle()
pen3.penup()
pen3.hideturtle()
pen.goto(-330,200)
pen3.write("Accuracy: 0", font=("Helvetica", 30))

pen2.goto(100,-230)
pen2.write('Shots:0', font=('Helvetica',24,'bold'))

#accuracy turtle
pen3 = turtle.Turtle()
pen3.penup()
pen3.hideturtle()
pen3.goto(-330,200)
pen3.write('Accuracy:0', font=('Helvetica',24,'bold'))

#Functions
def shoot():
    for s in range(30):
        y=ball.ycor()
        y+=15
        ball.sety(y)
        time.sleep(0.025)
        wn.update()
        #Check for collision
        if (ball.xcor() < basket.xcor() + 30) and (ball.xcor() > basket.xcor()-30) and (ball.ycor() == basket.ycor):
            global score1
            score1+=1
            ball.sety(120)
            wn.update()
            time.sleep(0.025)
            ball.sety(80)
            wn.update()
            pen.clear()
            pen.write('Score:({}'.format(score1),  font=('Helvetica',24,'bold'))
            break
    
    global shots1
    ball.goto(0,-180)
    shots1 +=1
    pen2.clear()
    pen2.write('Shots:{}'.format(shots1), font=('Helvetica',24,'bold'))

    if score1>0:
        accuracy=score1/shots1*100
        pen3.clear()
        pen3.write('Accuracy:{}%', font=('Helvetica',24,'bold'))

def yay1():
    shoot()

# bindings

wn.listen()
wn.onkeypress(yay1, 's')

score1=0
shots1=0


#main game loop!!!

while True:
    wn.update()

    #move the hoop
    x = random.randint(1,150)
    basket.setx(basket.xcor() + x)
    time.sleep(0.11)
    x = random.randint(1,150)
    time.sleep(0.11)
    basket.setx(basket.xcor()-x)

    #checking the borders

    if basket.xcor() > 250:
        basket.setx(220)
        
    if basket.xcor() < -250:
        basket.setx(-220)





