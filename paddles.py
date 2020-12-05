def paddle_a(turtle):
  paddle_a = turtle.Turtle()
  paddle_a.speed(0) # Animation speed
  paddle_a.shape("square")
  paddle_a.color("white")
  paddle_a.shapesize(stretch_wid=5, stretch_len=1)
  paddle_a.penup()
  paddle_a.goto(-350, 0)
  return paddle_a

def paddle_b(turtle):
  paddle_b = turtle.Turtle()
  paddle_b.speed(0) # Animation speed
  paddle_b.shape("square")
  paddle_b.color("white")
  paddle_b.shapesize(stretch_wid=5, stretch_len=1)
  paddle_b.penup()
  paddle_b.goto(350, 0)
  return paddle_b