import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)
# CONST
ballVelocity = .2
barVelocity = 30
leftBarUpKey = "w"
leftBarDownKey = "s"
rightBarUpKey = "Up"
rightBarDownKey = "Down"
verticalBorder = 290
horizontalBorder = 390
scoreLeft = 0
scoreRight = 0
# BAR LEFT
leftBar = turtle.Turtle()
leftBar.speed(0)
leftBar.shape("square")
leftBar.color("red")
leftBar.shapesize(stretch_wid=5, stretch_len=1)
leftBar.penup()
leftBar.goto(-350, 0)
# BAR RIGHT
rightBar = turtle.Turtle()
rightBar.speed(0)
rightBar.shape("square")
rightBar.color("blue")
rightBar.shapesize(stretch_wid=5, stretch_len=1)
rightBar.penup()
rightBar.goto(350, 0)
# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ballVelocity
ball.dy = ballVelocity
#PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("0:0", align="center", font=("Courier", 18, "normal"))
#FUNCTIONS
def leftBarUp():
    y = leftBar.ycor()
    y += barVelocity
    leftBar.sety(y)
def leftBarDown():
    y = leftBar.ycor()
    y -= barVelocity
    leftBar.sety(y)
def rightBarUp():
    y = rightBar.ycor()
    y += barVelocity
    rightBar.sety(y)
def rightBarDown():
    y = rightBar.ycor()
    y -= barVelocity
    rightBar.sety(y)
#KEYBOARD
window.listen()
window.onkeypress(leftBarUp, leftBarUpKey)
window.onkeypress(leftBarDown, leftBarDownKey)
window.onkeypress(rightBarUp, rightBarUpKey)
window.onkeypress(rightBarDown, rightBarDownKey)
#MAIN LOOP
while True:
    window.update()

    #BALL MOVEMENT
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BALL BORDERS
    if ball.ycor() > verticalBorder:
        ball.sety(verticalBorder)
        ball.dy *= -1
    elif ball.ycor() < - verticalBorder:
        ball.sety(- verticalBorder)
        ball.dy *= -1
    elif ball.xcor() >  horizontalBorder:
        ball.goto(0,0)
        ball.dx *= -1
        scoreLeft += 1
        pen.clear()
        pen.write("{}:{}".format(scoreLeft, scoreRight), align="center", font=("Courier", 18, "normal"))
    elif ball.xcor() < - horizontalBorder:
        ball.goto(0,0)
        ball.dx *= -1
        scoreRight += 1
        pen.clear()
        pen.write("{}:{}".format(scoreLeft, scoreRight), align="center", font=("Courier", 18, "normal"))
    #BARS COLLISIONS
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < rightBar.ycor() + 40 and ball.ycor() > rightBar.ycor() -40 ):
        ball.color("blue")
        ball.setx(340)
        ball.dx *= -1
    elif ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < leftBar.ycor() + 40 and ball.ycor() > leftBar.ycor() -40 ):
        ball.color("red")
        ball.setx(-340)
        ball.dx *= -1