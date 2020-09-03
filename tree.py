from drawable import Drawable

class Tree(Drawable):
    def __init__(self, x, y, trunk_color, leaf_color, line_width, trunk_length, num_branches, branch_length):
        super().__init__(x, y, trunk_color, leaf_color, line_width)
        self.trunk_length = trunk_length
        self.num_branches = num_branches
        self.branch_length = branch_length

    def get_turn_degrees(self):
        return 180 / self.num_branches
    
    def draw_trunk(self):
        self.t.pensize(self.line_width)
        self.t.forward(self.trunk_length)
    
    def draw_branch(self):
        self.t.pencolor(self.color1)
        self.t.pendown()
        if (self.num_branches > 2):
            self.t.pensize(self.line_width / self.num_branches * 2)
        else:
            self.t.pensize(self.line_width / 2)
        self.t.forward(self.branch_length + self.line_width / 2)
        self.t.backward(self.branch_length + self.line_width / 2)
        self.t.right(self.get_turn_degrees())
    
    def draw_leaves(self):
        self.t.pencolor(self.color2)
        self.t.penup()
        self.t.left(self.get_turn_degrees())
        self.t.forward(self.branch_length + self.line_width / 2)
        self.t.dot(self.line_width * (1 + 1 / self.num_branches))
        self.t.backward(self.branch_length + self.line_width / 2)
        self.t.right(self.get_turn_degrees())
    
    def draw_branches(self):
        self.t.setheading(180 - self.get_turn_degrees() / 2)
        for _ in range(self.num_branches):
            self.draw_branch()
            self.draw_leaves()
    
    def draw(self, x=None, y=None):
        super().draw(x, y)
        self.draw_trunk()
        self.draw_branches()
        return False
