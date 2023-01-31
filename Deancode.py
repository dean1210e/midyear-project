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





