import turtle
import time
wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#instruction
instruction = turtle.Turtle()
instruction.color('white')
instruction.penup()
instruction.hideturtle()
instruction.goto(0, 0)
instruction.write('Player A uses W, S, A, D ', align ='center', font=('courier', 17, 'normal'))
instruction.goto(0, -30)
instruction.write('Player B uses Up, Down, Left, Right for controls',align ='center', font=('courier', 17, 'normal'))
instruction.clear()

#First paddle
first_paddle = turtle.Turtle()
first_paddle.speed(0)
first_paddle.shape('square')
first_paddle.shapesize(stretch_wid=5.,stretch_len=1)
first_paddle.color('white')
first_paddle.penup()
first_paddle.goto(-350, 0)

#Second paddle
second_paddle = turtle.Turtle()
second_paddle.speed(0)
second_paddle.shape('square')
second_paddle.shapesize(stretch_wid=5.,stretch_len=1)
second_paddle.color('white')
second_paddle.penup()
second_paddle.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.shapesize(stretch_wid=0.8,stretch_len= 0.8)
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.8
ball.dy = 0.8
time.sleep(5)

#Scoreboard
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write('Player A: 0 Player B: 0', align = 'center', font=('courier', 24, 'normal'))

#Score counter
first_paddle_score = 0
second_paddle_score = 0

#fuctions for movements
def first_paddle_up():
    y = first_paddle.ycor()
    y += 20
    first_paddle.sety(y)

def first_paddle_down():
    y = first_paddle.ycor()
    y -= 20
    first_paddle.sety(y)

def second_paddle_up():
    y = second_paddle.ycor()
    y += 20
    second_paddle.sety(y)

def second_paddle_down():
    y = second_paddle.ycor()
    y -= 20
    second_paddle.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(first_paddle_up, 'w')
wn.onkeypress(first_paddle_down, 's')
wn.onkeypress(second_paddle_up, 'Up')
wn.onkeypress(second_paddle_down, 'Down')

#Main game loop
while True:
    wn.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1

    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1
    
    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.dx *= -1
        first_paddle_score += 1
        score.clear()
        score.write('Player A: {} Player B: {}'.format(first_paddle_score, second_paddle_score), align = 'center', font=('courier', 24, 'normal'))
    
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx *= -1
        second_paddle_score += 1
        score.clear()
        score.write('Player A: {} Player B: {}'.format(first_paddle_score, second_paddle_score), align = 'center', font=('courier', 24, 'normal'))
        
    # ball brick collision

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < first_paddle.ycor() + 50 and ball.ycor() > first_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < second_paddle.ycor() + 50 and ball.ycor() > second_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    