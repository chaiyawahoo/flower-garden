import turtle as t
from flower import Flower
from orchid import Orchid

screen = t.Screen()
t.ht()
t.speed("fastest")

flowers = []
f_index = 0

flowers.append(Flower(t, 0, 0, "pink", "orange", 40, 6, 100))
flowers.append(Flower(t, 0, 0, "lightblue", "yellow", 30, 8, 60))
flowers.append(Orchid(t, 0, 0, "purple", "pink", "yellow", 35)) # orchid

def next_flower():
    global f_index
    f_index = f_index + 1 if f_index < len(flowers) - 1 else 0

def last_flower():
    global f_index
    f_index = f_index - 1 if f_index > 0 else len(flowers) - 1

def draw_flower(x, y):
    flowers[f_index].draw(x, y)

def main():
    t.listen()

    screen.onclick(draw_flower)
    screen.onkeypress(next_flower, "Right")
    screen.onkeypress(last_flower, "Left")
    screen.onkeypress(next_flower, "d")
    screen.onkeypress(last_flower, "a")

    screen.mainloop()

main()

