# Beginning of python learning

import turtle
import os

# Set up the screen
screen = turtle.Screen()
screen.title("Pong by @chetanchopra03")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Player A
player_a = turtle.Turtle()
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("white")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)

# Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("white")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25  # type: ignore
ball.dy = 0.25  # type: ignore


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# Function


def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)


def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)


def player_b_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)


def player_b_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)


# Keyboard binding
screen.listen()
screen.onkeypress(player_a_up, "w")
screen.onkeypress(player_a_down, "s")
screen.onkeypress(player_b_up, "Up")
screen.onkeypress(player_b_down, "Down")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # type: ignore
    ball.sety(ball.ycor() + ball.dy)  # type: ignore

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # type: ignore
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # type: ignore
        os.system("aplay bounce.wav&")
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  # type: ignore
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("aplay border.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  # type: ignore
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("aplay border.wav&")

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1  # type: ignore
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1  # type: ignore
        os.system("aplay bounce.wav&")

# git init
# git add .
# git commit -m "Initial commit"
# git remote add origin https://github.com/chetanchopra03/pong_game.git
# git add .gitignore
# git push -u origin master
# To remove the already uploaded files on github repository
# git rm -r --cached
# git add .
# git commit -m "Remove ignored files from repository"
# git push origin master
