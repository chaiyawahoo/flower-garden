from flower import Flower

class Orchid(Flower):
    def __init__(self, x, y, color1, color2, center_color, line_width):
        super().__init__(x, y, color1, center_color, line_width, 5, line_width)
        self.color2 = color2

    def draw_center(self):
        self.t.pencolor(self.center_color)
        self.t.dot(self.line_width * 0.75)
    
    def draw_petals(self):
        super().draw_petals()
        self.t.pencolor(self.color2)
        self.t.pensize(self.line_width * 0.25)
        super().draw_petals()