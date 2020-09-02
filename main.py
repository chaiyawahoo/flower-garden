import turtle as monkey
import random

screen = monkey.Screen()
monkey.ht()
monkey.speed("fastest")

def draw_flower(x, y, num_petals, petal_size, color, petal_length):
  monkey.goto(x,y)
  monkey.pencolor(color)
  monkey.pensize(petal_size)

  #draw petals
  for _ in range(num_petals):
    monkey.forward(petal_length)
    monkey.backward(petal_length)
    monkey.right(360/num_petals)

  #draw center
  monkey.pencolor("orange")
  monkey.dot(50)


# draw_flower(0,0,6,40,"pink", 100)

class Drawable:
    def __init__(self, x, y, color, line_width):
        self.x = x
        self.y = y
        self.color = color
        self.line_width = line_width
    
    def draw(self, x=None, y=None):
        x_pos, y_pos = x, y
        monkey.penup()
        if x_pos == None:
            x_pos = self.x
        if y_pos == None:
            y_pos = self.y
        monkey.setheading(90)
        monkey.goto(x_pos, y_pos)
        monkey.pencolor(self.color)
        monkey.pensize(self.line_width)
        monkey.pendown()

class Flower(Drawable):
    def __init__(self, x, y, color, center_color, line_width, num_petals, petal_length):
        super().__init__(x, y, color, line_width)
        self.center_color = center_color
        self.num_petals = num_petals
        self.petal_length = petal_length

    def get_turn_degrees(self):
        return 360 / self.num_petals

    def draw_petal(self):
        monkey.forward(self.petal_length)
        monkey.backward(self.petal_length)
        monkey.right(self.get_turn_degrees())
    
    def draw_center(self):
        monkey.pencolor(self.center_color)
        monkey.dot(self.line_width * 1.25)
    
    def draw(self, x=None, y=None):
        super().draw(x, y)
        for _ in range(self.num_petals):
            self.draw_petal()
        self.draw_center()

def rand_x():
    return random.randrange(int(-monkey.window_width() / 2), int(monkey.window_width() / 2))

def rand_y():
    return random.randrange(int(-monkey.window_height() / 2), int(monkey.window_height() / 2))

pinky = Flower(0, 0, "pink", "orange", 40, 6, 100)
blu = Flower(0, 0, "lightblue", "yellow", 30, 8, 60)
orchid = Flower(0, 0, "purple", "white", 35, 5, 35)
flowers = [pinky, blu]
for flower in flowers:
    flower.draw(rand_x(), rand_y())

def draw_orchid(x, y):
    orchid.draw(x, y)

def main():
    monkey.listen()

    screen.onclick(draw_orchid)

    screen.mainloop()

main()

