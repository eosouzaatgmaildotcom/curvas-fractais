import math

class KochGenerator:
    def __init__(self):
        self.lines = []
        self.x = 0
        self.y = 0
        self.angle = 0

    def generate(self, start_x, start_y, length, depth):
        self.lines = []
        self.x, self.y = start_x, start_y
        self.angle = 0
        self.draw_koch(length, depth)
        return self.lines

    def draw_koch(self, length, depth):
        if depth == 0:
            nx = self.x + length * math.cos(math.radians(self.angle))
            ny = self.y + length * math.sin(math.radians(self.angle))
            self.lines.append((self.x, self.y, nx, ny))
            self.x, self.y = nx, ny
        else:
            length /= 3
            self.draw_koch(length, depth - 1)
            self.angle -= 60
            self.draw_koch(length, depth - 1)
            self.angle += 120
            self.draw_koch(length, depth - 1)
            self.angle -= 60
            self.draw_koch(length, depth - 1)

class CesaroGenerator(KochGenerator):
    """Uma variante do Koch com ângulos mais agudos."""
    def draw_koch(self, length, depth):
        if depth == 0:
            nx = self.x + length * math.cos(math.radians(self.angle))
            ny = self.y + length * math.sin(math.radians(self.angle))
            self.lines.append((self.x, self.y, nx, ny))
            self.x, self.y = nx, ny
        else:
            length /= 2.5
            self.draw_koch(length, depth - 1)
            self.angle -= 85
            self.draw_koch(length, depth - 1)
            self.angle += 170
            self.draw_koch(length, depth - 1)
            self.angle -= 85
            self.draw_koch(length, depth - 1)

class DragonGenerator:
    def __init__(self):
        self.lines = []
        self.x, self.y = 0, 0
        self.angle = 0

    def generate(self, start_x, start_y, length, depth):
        self.lines = []
        self.x, self.y = start_x, start_y
        self.angle = 0
        self.draw_dragon(length, depth, 1)
        return self.lines

    def draw_dragon(self, length, depth, sign):
        if depth == 0:
            nx = self.x + length * math.cos(math.radians(self.angle))
            ny = self.y + length * math.sin(math.radians(self.angle))
            self.lines.append((self.x, self.y, nx, ny))
            self.x, self.y = nx, ny
        else:
            new_length = length / math.sqrt(2)
            self.angle += sign * 45
            self.draw_dragon(new_length, depth - 1, 1)
            self.angle -= sign * 90
            self.draw_dragon(new_length, depth - 1, -1)
            self.angle += sign * 45