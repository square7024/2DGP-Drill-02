from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

square = 0

x = 400
y = 80
right = 784
top = 560
left = 14
bottom = 80
center = 400

r = 240
x_c = 90
y_c = -90

while (True):
    if square == 0:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        if (x < right and y <= bottom):
            x += 2
        if (x >= right and y < top):
            y += 2
        if (y >= top and x > left):
            x -= 2
        if (x <= left and y > bottom):
            y -= 2

        if x == center and y == bottom and square == 0:
            square = 1
    elif square == 1:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x_c += 1
        x = 400 + r * math.cos(math.radians(x_c))
        y_c += 1
        y = 320 + r * math.sin(math.radians(y_c))

        if (x_c == 90 + 360):
            x_c = 90
            y_c = -90
            square = 0


    delay(0.005)

close_canvas()
