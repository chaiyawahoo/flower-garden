import turtle as t

class Drawable:
    def __init__(self, x, y, color1, color2, line_width):
        self.t = t
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.line_width = line_width
    
    def get_turn_degrees(self, degrees=360, count=1):
        assert (degrees >= 0), "Degrees must be greater than or equal to 0!"
        assert (count != 0), "Count must not be 0!"
        return degrees / count

    def repeater(self, count, fun):
        for _ in range(count):
            fun()
    
    def draw(self, x=None, y=None):
        x_pos = x if not x == None else self.x
        y_pos = y if not y == None else self.y
        self.t.penup()
        self.t.setheading(90)
        self.t.goto(x_pos, y_pos)
        self.t.pencolor(self.color1)
        self.t.pensize(self.line_width)
        self.t.pendown()
        return 0