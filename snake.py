from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()
    self.shape("square")
    self.color("green")
    self.penup()
    self.goto(0,0)
    self.setheading(90)
    self.alive = True
    self.direction("Up", "Down", "Left", "Right")
    screen.onkeypress(self.turn_left, left_key)
    screen.onkeypress(self.turn_right, right_key)
    screen.onkeypress(self.turn_up, up_key)
    screen.onkeypress(self.turn_down, down_key)

  def up(self):
    self.seth(90)
    self.direction("Up")
    if self.direction == "Down":
      self.direction = "Up"
    elif self.direction != "Down":
      self.direction = "Up"

  def down(self):
    self.seth(270)
    self.direction("Down")
    if self.direction == "Up":
      self.direction = "Down"
    elif self.direction != "Up":
      self.direction = "Down"

  def left(self):
    self.seth(180)
    self.direction("Left")

  def right(self):
    self.seth(0)
    self.direction("Right")

  def move(self):
    self.forward(20)
    if self.xcor() > 230 or self.xcor() < -230:
        self.alive = False
        self.ht
    if self.ycor() > 230 or self.ycor() < -230:
        self.alive = False
        self.ht
    
  def die(self):    
    self.alive = False
    self.hideturtle()

class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    pass

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    pass

  def relocate(self):
    pass

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

body = []

while True:
  for i in range(len(body)-1, 0, 1):
    body[i].move(body[i-1])

screen.exitonclick()






screen.exitonclick()