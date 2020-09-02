import turtle as t
from flower import Flower
from orchid import Orchid

screen = t.Screen()
t.ht()
t.speed("fastest")

flowers = []
f_index = 0

is_drawing = False
draw_q = []

flowers.append(Flower(0, 0, "pink", "orange", 40, 6, 100))
flowers.append(Flower(0, 0, "lightblue", "yellow", 30, 8, 60))
flowers.append(Orchid(0, 0, "purple", "pink", "yellow", 35))
flowers.append(Orchid(0, 0, "orange", "magenta", "white", 50))

def next_flower():
    global f_index
    f_index = f_index + 1 if f_index < len(flowers) - 1 else 0

def last_flower():
    global f_index
    f_index = f_index - 1 if f_index > 0 else len(flowers) - 1

def draw_flower(x, y):
    draw_q.append({"obj": flowers[f_index], "x": x, "y": y})
    if not is_drawing:
        draw_next()

def draw_next():
    global is_drawing
    if not is_drawing and len(draw_q) > 0:
        is_drawing = True
        is_drawing = draw_q[0]["obj"].draw(draw_q[0]["x"], draw_q[0]["y"])
        del draw_q[0]
        draw_next()

def main():
    screen.listen()

    screen.onclick(draw_flower)
    screen.onkeypress(next_flower, "Right")
    screen.onkeypress(last_flower, "Left")
    screen.onkeypress(next_flower, "d")
    screen.onkeypress(last_flower, "a")

    screen.mainloop()

main()