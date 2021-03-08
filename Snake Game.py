#Printing Hello, World!
print("Hello World!")

#Importing module/ libraries
import turtle
import time
import random

#Variables
delay = 0.1
segments = []
score = 0
hi_score = 0

#Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Snake Game")
wn.setup(width=600, height=600)
wn.tracer(0)

#Player
gamer = turtle.Turtle()
gamer.color("white")
gamer.shape("square")
gamer.penup()
gamer.goto(0, 0)
gamer.direction = "stop"
gamer.speed(0)

#Food
food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.penup()
food.speed(0)
food.goto(0, 150)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#Functions
def move_up():
    if gamer.direction != "down":
        gamer.direction = "up"

def move_down():
    if gamer.direction != "up":
        gamer.direction = "down"

def move_right():
    if gamer.direction != "left":
        gamer.direction = "right"

def move_left():
    if gamer.direction != "right":
        gamer.direction = "left"


def move():
    if gamer.direction == "up":
        y = gamer.ycor()
        gamer.sety(y+20)

    if gamer.direction == "down":
        y = gamer.ycor()
        gamer.sety(y-20)

    if gamer.direction == "right":
        x = gamer.xcor()
        gamer.setx(x+20)

    if gamer.direction == "left":
        x = gamer.xcor()
        gamer.setx(x-20)

#Keyboard Support
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_right, "d")
wn.onkeypress(move_left, "a")


#Main Loop
while True:
    wn.update()

    if gamer.xcor()>290 or gamer.xcor()<-290 or gamer.ycor()>290 or gamer.ycor()<-290:
        time.sleep(1)
        gamer.goto(0, 0)
        gamer.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, hi_score), align="center", font=("Courier", 24, "normal"))


    if gamer.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y )

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

        if score > hi_score:
            hi_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, hi_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments)-1, 0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = gamer.xcor()
        y = gamer.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(gamer) <20:
            time.sleep(1)
            gamer.goto(0, 0)
            gamer.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, hi_score), align="center", font=("Courier", 24, "normal"))

    
    

    time.sleep(delay)

#Done Statement
turtle.done()

