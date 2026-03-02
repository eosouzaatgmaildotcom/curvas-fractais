# hilberts.py

class HilbertGenerator:
    def __init__(self, proporcao=3):
        self.proporcao = proporcao
        self.incremento = 0
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

    def generate(self, start_x, start_y, incremento, depth):
        self.incremento = incremento
        self.lines = []
        self.move_to(start_x, start_y)
        self.A(depth)
        return self.lines

    def A(self, i):
        if i > 0:
            self.D(i-1)
            self.line_rel(-self.incremento, 0)
            self.A(i-1)
            self.line_rel(0, self.incremento / self.proporcao)
            self.A(i-1)
            self.line_rel(self.incremento, 0)
            self.B(i-1)

    def B(self, i):
        if i > 0:
            self.C(i-1)
            self.line_rel(0, -self.incremento / self.proporcao)
            self.B(i-1)
            self.line_rel(self.incremento, 0)
            self.B(i-1)
            self.line_rel(0, self.incremento / self.proporcao)
            self.A(i-1)

    def C(self, i):
        if i > 0:
            self.B(i-1)
            self.line_rel(self.incremento, 0)
            self.C(i-1)
            self.line_rel(0, -self.incremento / self.proporcao)
            self.C(i-1)
            self.line_rel(-self.incremento, 0)
            self.D(i-1)

    def D(self, i):
        if i > 0:
            self.A(i-1)
            self.line_rel(0, self.incremento / self.proporcao)
            self.D(i-1)
            self.line_rel(-self.incremento, 0)
            self.D(i-1)
            self.line_rel(0, -self.incremento / self.proporcao)
            self.C(i-1)
