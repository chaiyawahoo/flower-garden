import turtle as t
from flower import Flower
from orchid import Orchid
from tree import Tree
from bush import Bush

screen = t.Screen()
t.ht()
t.speed("fastest")

objects = []
o_index = 0

is_drawing = False
draw_q = []

objects.append(Flower(0, 0, "pink", "orange", 20, 6, 50))
objects.append(Flower(0, 0, "lightblue", "yellow", 15, 8, 30))
objects.append(Orchid(0, 0, "purple", "pink", "yellow", 17.5))
objects.append(Orchid(0, 0, "orange", "magenta", "white", 25))
objects.append(Tree(0, 0, "brown", "green", 75, 150, 4, 75))
objects.append(Bush(0, 0, "green", "red", 50, 15, 5))

def next_object():
    global o_index
    o_index = o_index + 1 if o_index < len(objects) - 1 else 0

def last_object():
    global o_index
    o_index = o_index - 1 if o_index > 0 else len(objects) - 1

def draw_object(x, y):
    draw_q.append({"obj": objects[o_index], "x": x, "y": y})
    if not is_drawing and len(draw_q) == 1:
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

    screen.onclick(draw_object)
    screen.onkeypress(next_object, "Right")
    screen.onkeypress(last_object, "Left")
    screen.onkeypress(next_object, "d")
    screen.onkeypress(last_object, "a")

    screen.mainloop()

main()