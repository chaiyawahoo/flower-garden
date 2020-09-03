from drawable import Drawable

class Flower(Drawable):
    def __init__(self, x, y, petal_color, center_color, line_width, num_petals, petal_length):
        super().__init__(x, y, petal_color, center_color, line_width)
        self.num_petals = num_petals
        self.petal_length = petal_length

    def get_turn_degrees(self):
        return 360 / self.num_petals

    def draw_petal(self):
        self.t.forward(self.petal_length)
        self.t.backward(self.petal_length)
        self.t.right(self.get_turn_degrees())
    
    def draw_petals(self):
        for _ in range(self.num_petals):
            self.draw_petal()
    
    def draw_center(self):
        self.t.pencolor(self.color2)
        self.t.dot(self.line_width * 1.25)
    
    def draw(self, x=None, y=None):
        super().draw(x, y)
        self.draw_petals()
        self.draw_center()
        return False