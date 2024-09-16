import pyray as rl
from pyray import WHITE,VIOLET
import src.game as ga


rl.init_window(800, 450, "Hello")

c = ga.Car(100,100,100)
while not rl.window_should_close():
    rl.begin_drawing()

    c.draw()

    rl.clear_background(WHITE)
    rl.draw_text("Hello world", 190, 200, 20, VIOLET)

    rl.end_drawing()
rl.close_window()

