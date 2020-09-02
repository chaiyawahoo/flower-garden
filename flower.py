from drawable import Drawable

class Flower(Drawable):
    def __init__(self, t, x, y, color, center_color, line_width, num_petals, petal_length):
        super().__init__(t, x, y, color, line_width)
        self.center_color = center_color
        self.num_petals = num_petals
        self.petal_length = petal_length

    def get_turn_degrees(self):
        return 360 / self.num_petals

    def draw_petal(self):
        self.t.forward(self.petal_length)
        self.t.backward(self.petal_length)
        self.t.right(self.get_turn_degrees())
    
    def draw_center(self):
        self.t.pencolor(self.center_color)
        self.t.dot(self.line_width * 1.25)
    
    def draw(self, x=None, y=None):
        super().draw(x, y)
        for _ in range(self.num_petals):
            self.draw_petal()
        self.draw_center()