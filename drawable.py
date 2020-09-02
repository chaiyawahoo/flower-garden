import turtle as t

class Drawable:
    def __init__(self, x, y, color, line_width):
        self.t = t
        self.x = x
        self.y = y
        self.color = color
        self.line_width = line_width
    
    def draw(self, x=None, y=None):
        x_pos = x if not x == None else self.x
        y_pos = y if not y == None else self.y
        self.t.penup()
        self.t.setheading(90)
        self.t.goto(x_pos, y_pos)
        self.t.pencolor(self.color)
        self.t.pensize(self.line_width)
        self.t.pendown()
        return 0