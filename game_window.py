def window_settings(turtle):
  wn = turtle.Screen()
  wn.title("Pong games by @RaySoju")
  wn.bgcolor("black")
  wn.setup(width=800, height=600)
  wn.tracer(0) # Stop the window from updating so we have to update it manually (makes the game faster)
  return wn

def keyboard_binding(window, paddle_a_up, paddle_a_down, paddle_b_up, paddle_b_down):
  window.listen()
  window.onkeypress(paddle_a_up, "z")
  window.onkeypress(paddle_a_down, "s")
  window.onkeypress(paddle_b_up, "Up")
  window.onkeypress(paddle_b_down, "Down")