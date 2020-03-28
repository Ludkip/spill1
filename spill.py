import turtle

win = turtle.Screen() #lager en skjerm
win.title("Pong av Lucas") #tittel
win.bgcolor("black") #bakgrunnsfarge
win.setup(width=800, height=600) # skjerm størrelse
win.tracer(0)  #vinduet oppdateres ikke automatisk

#paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") #form
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #standard er 20x20
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") #form
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #standard er 20x20
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") #form
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.1
ball.dy = 0.1

#function
def paddle_a_up():
    y = paddle_a.ycor() #finner y kordinatene
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #finner y kordinatene
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor() #finner y kordinatene
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #finner y kordinatene
    y -= 20
    paddle_b.sety(y)

#keyboard binding
win.listen() #hører etter tastatur input
win.onkeypress(paddle_a_up, "w") #hvis w så skal paddle a å opp
win.listen()
win.onkeypress(paddle_a_down, "s")


win.listen() #hører etter tastatur input
win.onkeypress(paddle_b_up, "Up") #hvis w så skal paddle a å opp
win.listen() 
win.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    win.update() #hver gang loopen går


    #beveg ballen
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


#Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    if ball.xcor() > 390:
        ball.goto(0, 0)

    if ball.xcor() < -390:
       ball.goto(0, 0)