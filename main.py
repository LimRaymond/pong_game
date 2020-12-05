# Simple Pong game using python 3
# Only for learning syntaxes
import turtle

import game_window as wnd
import paddles as paddle
import ball
import score_system

#Global
wd = wnd.window_settings(turtle)
paddle_a = paddle.paddle_a(turtle)
paddle_b = paddle.paddle_b(turtle)
ball = ball.ball(turtle)

#Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

  
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

def main():
  score_a = 0
  score_b = 0
  wnd.keyboard_binding(wd, paddle_a_up, paddle_a_down, paddle_b_up, paddle_b_down)
  pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

  #Main game loop
  while True:
    wd.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
      
    if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
    
    if ball.xcor() > 390:
      ball.goto(0, 0)
      ball.dx *= -1
      score_a += 1
      pen.clear()
      pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
      ball.goto(0, 0)
      ball.dx *= -1
      score_b += 1
      pen.clear()
      pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and  (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
      ball.setx(340)
      ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and  (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
      ball.setx(-340)
      ball.dx *= -1

if __name__ == "__main__":
    main()