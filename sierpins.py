# sierpins.py
import turtle
from progress import ProgressTracker

progress = None

def count_sierpinski(level):
    if level == 0:
        return 1  # uma linha desenhada
    return 3 * count_sierpinski(level - 1) + 2 * count_sierpinski(level - 1)

def sierpinski_H(level, step):
    if level == 0:
        turtle.forward(step)
        progress.step()
        return

    sierpinski_H(level - 1, step)
    turtle.right(90)
    sierpinski_C(level - 1, step)
    turtle.right(90)
    sierpinski_H(level - 1, step)
    turtle.left(90)
    sierpinski_C(level - 1, step)
    turtle.left(90)
    sierpinski_H(level - 1, step)

def sierpinski_C(level, step):
    if level == 0:
        turtle.forward(step)
        progress.step()
        return

    sierpinski_C(level - 1, step)
    turtle.left(90)
    sierpinski_H(level - 1, step)
    turtle.left(90)
    sierpinski_C(level - 1, step)
    turtle.right(90)
    sierpinski_H(level - 1, step)
    turtle.right(90)
    sierpinski_C(level - 1, step)

def draw_sierpinski(order, step, tracker):
    global progress
    progress = tracker
    sierpinski_H(order, step)