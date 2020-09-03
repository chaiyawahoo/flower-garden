from drawable import Drawable

class Bush(Drawable):
    def __init__(self, x, y, bush_color, berry_color, leaf_size, berry_size, num_leaves):
        super().__init__(x, y, bush_color, berry_color, leaf_size)
        self.berry_size = berry_size
        self.num_leaves = num_leaves
    
    def get_turn_degrees(self):
        return 180 / (self.num_leaves - 1)

    def draw_base(self):
        self.t.forward(self.line_width * 0.25)
        self.t.dot(self.line_width * 1.5)
        self.t.backward(self.line_width * 0.25)
    
    def draw_leaf(self):
        self.t.forward(self.line_width)
        self.t.dot(self.line_width)
        self.t.backward(self.line_width)
        self.t.right(self.get_turn_degrees())
    
    def draw_berry(self):
        self.t.forward(self.line_width * 0.875)
        self.t.dot(self.berry_size)
        self.t.backward(self.line_width * 0.875)
        self.t.right(self.get_turn_degrees())
    
    def draw_leaves(self):
        self.t.setheading(180)
        self.t.pencolor(self.color1)
        self.repeater(self.num_leaves, self.draw_leaf)
    
    def draw_berries(self):
        self.t.setheading(180)
        self.t.pencolor(self.color2)
        self.repeater(self.num_leaves, self.draw_berry)

    def draw(self, x=None, y=None):
        super().draw(x, y)
        self.t.penup()
        self.draw_base()
        self.draw_leaves()
        self.draw_berries()
        return False