# hilberts.py
import turtle
from progress import ProgressTracker

progress = None  # definido no main

def count_hilbert(level):
    if level == 0:
        return 0
    return 2 ** level * 2 ** level - 1

def hilbert_A(level, angle, step):
    if level == 0:
        return

    turtle.right(angle)
    hilbert_B(level - 1, -angle, step)

    turtle.forward(step)
    progress.step()

    turtle.left(angle)
    hilbert_A(level - 1, angle, step)

    turtle.forward(step)
    progress.step()

    hilbert_A(level - 1, angle, step)

    turtle.left(angle)
    turtle.forward(step)
    progress.step()

    hilbert_B(level - 1, -angle, step)
    turtle.right(angle)

def hilbert_B(level, angle, step):
    if level == 0:
        return
    
    turtle.left(angle)
    hilbert_A(level - 1, -angle, step)

    turtle.forward(step)
    progress.step()

    turtle.right(angle)
    hilbert_B(level - 1, angle, step)

    turtle.forward(step)
    progress.step()

    hilbert_B(level - 1, angle, step)

    turtle.right(angle)
    turtle.forward(step)
    progress.step()

    hilbert_A(level - 1, -angle, step)
    turtle.left(angle)

def draw_hilbert(order, step, tracker):
    global progress
    progress = tracker
    hilbert_A(order, 90, step)