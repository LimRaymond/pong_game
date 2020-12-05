def ball(turtle):
  ball = turtle.Turtle()
  ball.speed(0) # Animation speed
  ball.shape("square")
  ball.color("white")
  ball.penup()
  ball.goto(0, 0)
  ball.dx = 0.15
  ball.dy = -0.15
  return ball