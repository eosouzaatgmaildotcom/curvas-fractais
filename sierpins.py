# sierpins.py

class SierpinskiGenerator:
    def __init__(self, proporcao=3):
        self.proporcao = proporcao
        self.u = 0
        self.x = 0.0
        self.y = 0.0
        self.lines = []

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def line_rel(self, dx, dy):
        x_new = self.x + dx
        y_new = self.y + dy
        self.lines.append((self.x, self.y, x_new, y_new))
        self.x = x_new
        self.y = y_new

    def generate(self, start_x, start_y, u, depth):
        self.u = u
        self.lines = []
        self.move_to(start_x, start_y)
        
        self.E(depth)
        self.line_rel(self.u, self.u / self.proporcao)
        self.F(depth)
        self.line_rel(-self.u, self.u / self.proporcao)
        self.G(depth)
        self.line_rel(-self.u, -self.u / self.proporcao)
        self.H(depth)
        self.line_rel(self.u, -self.u / self.proporcao)
        
        return self.lines

    def E(self, i):
        if i > 0:
            self.E(i-1)
            self.line_rel(self.u, self.u / self.proporcao)
            self.F(i-1)
            self.line_rel(2*self.u, 0)
            self.H(i-1)
            self.line_rel(self.u, -self.u / self.proporcao)
            self.E(i-1)

    def F(self, i):
        if i > 0:
            self.F(i-1)
            self.line_rel(-self.u, self.u / self.proporcao)
            self.G(i-1)
            self.line_rel(0, 2*self.u / self.proporcao)
            self.E(i-1)
            self.line_rel(self.u, self.u / self.proporcao)
            self.F(i-1)

    def G(self, i):
        if i > 0:
            self.G(i-1)
            self.line_rel(-self.u, -self.u / self.proporcao)
            self.H(i-1)
            self.line_rel(-self.u*2, 0)
            self.F(i-1)
            self.line_rel(-self.u, self.u / self.proporcao)
            self.G(i-1)

    def H(self, i):
        if i > 0:
            self.H(i-1)
            self.line_rel(self.u, -self.u / self.proporcao)
            self.E(i-1)
            self.line_rel(0, -self.u*2 / self.proporcao)
            self.G(i-1)
            self.line_rel(-self.u, -self.u / self.proporcao)
            self.H(i-1)