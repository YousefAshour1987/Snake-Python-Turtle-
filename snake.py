from turtle import *
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.listen()

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
    self.speed(0)
    self.setheading(90)
    self.alive = True
    self.direction = "Right"
    screen.onkeypress(self.left, "Left")
    screen.onkeypress(self.right, "Right")
    screen.onkeypress(self.up, "Up")
    screen.onkeypress(self.down, "Down")

  def up(self):
    if self.direction != "Down":
      self.direction = "Up"
      self.seth(90)

  def down(self):
    if self.direction != "Up":
      self.direction = "Down"
      self.seth(270)
  def left(self):
    if self.direction != "Right":
      self.direction = "Left"
      self.seth(180)

  def right(self):
    if self.direction != "Left":
      self.direction = "Right"
      self.seth(0)

  def move(self):
    if self.alive:
      self.forward(4)
      if self.xcor() > 230 or self.xcor() < -230:
        self.alive = False
        self.ht()
      elif self.ycor() > 230 or self.ycor() < -230:
        self.alive = False
        self.ht()
    
  def die(self):    
    self.alive = False
    self.hideturtle()

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("red")
    self.penup()
    self.speed(0)
    self.relocate()

  def relocate(self):
    x = random.randint(-230, 230)
    y = random.randint(-230, 230)
    self.goto(x, y)

body = []
playing_area()

snake_head = Head(screen, body)
apple = Apple()
while snake_head.alive:
  snake_head.move()
  if snake_head.distance(apple) < 20:
    apple.relocate()

screen.mainloop()

screen.exitonclick()