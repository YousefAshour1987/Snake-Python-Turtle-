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
    self.speed(0)
    self.setheading(90)
    self.alive = True
    self.direction = "Right"
    self.body = []
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
      self.forward(20)
      if self.xcor() > 230 or self.xcor() < -230:
        self.alive = False
        self.ht()
      elif self.ycor() > 230 or self.ycor() < -230:
        self.alive = False
        self.ht()

  def add_segment(self):
      new_segment = Segment()
      if len(self.body) > 0:
          x = self.body[-1].xcor()
          y = self.body[-1].ycor()
          new_segment.goto(x, y)
      else:
          new_segment.goto(self.xcor(), self.ycor())
      self.body.append(new_segment)
  def die(self):    
    self.alive = False
    self.hideturtle()
    self.body = []

class Segment(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("square")
    self.color("green")
    self.penup()
    self.body = []
    
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
def update():
  if snake_head.alive:
    snake_head.move()
    if snake_head.distance(apple) < 20:
      apple.relocate()
      snake_head.add_segment()
  def move(self):
      if self.alive:
        head_x = self.xcor(Head())
        head_y = self.ycor(Head())
        self.forward(20)
        for i in range(len(self.body)-1, 0, -1):
            x = self.body[i-1].xcor(Head)
            y = self.body[i-1].ycor(Head)
            self.body[i].goto(x, y)
        if len(self.body) > 0:
            self.body[0].goto(head_x, head_y)

        for segment in self.body[3:]:
          if self.distance(segment) < 10:
            self.ht()
            self.alive = False
            break
  screen.ontimer(update, 120)

body = []
playing_area()
snake_head = Head(Screen(), body)
apple = Apple()
screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
screen.listen()
screen.onkey(update, "space")
screen.mainloop()
screen.exitonclick()