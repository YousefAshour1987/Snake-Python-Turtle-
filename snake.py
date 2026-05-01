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
    self.ht()
    self.speed(0)
    self.hue = color
    self.color(color)
    self.penup()
    self.goto(x,y)
    self.setheading(90)
    self.shape("square")
    self.alive = True
    self.st()
    screen.onkeypress(self.turn_left, left_key)
    screen.onkeypress(self.turn_right, right_key)
    screen.onkeypress(self.turn_up, up_key)
    screen.onkeypress(self.turn_down, down_key)

  def up(self):
    self.seth(90)

  def down(self):
    self.seth(270)

  def left(self):
    self.seth(180)

  def right(self):
    self.seth(0)

  def move(self):
    self.forward(4)
    if self.xcor() > 230 or self.xcor() < -230:
        self.setheading(180 - self.heading())
    if self.ycor() > 230 or self.ycor() < -230:
        self.setheading(-self.heading())
    
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


screen.exitonclick()






screen.exitonclick()
