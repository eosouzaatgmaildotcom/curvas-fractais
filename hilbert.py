import tkinter as tk
from tkinter import ttk
import turtle
from PIL import ImageGrab

from hilberts import *
from sierpins import *
from progress import ProgressTracker


# =======================================================
# CONFIGURAÇÃO GLOBAL
# =======================================================
COLOR_LIST = ["red", "blue", "green", "purple", "orange", "black"]
color_index = 0

zoom_factor = 1.0
camera_dx = 0
camera_dy = 0

progressbar = None
root = None

current_steps = []
current_index = 0

drawing_finished = False


# =======================================================
# FUNÇÕES AUXILIARES
# =======================================================
def save_png(filename="curva.png"):
    cv = turtle.getcanvas()
    x1 = cv.winfo_rootx()
    y1 = cv.winfo_rooty()
    x2 = x1 + cv.winfo_width()
    y2 = y1 + cv.winfo_height()

    img = ImageGrab.grab((x1, y1, x2, y2))
    img.save(filename)
    print(f"PNG salvo como: {filename}")


# =======================================================
# ZOOM
# =======================================================
def zoom_in(event=None):
    global zoom_factor
    if not drawing_finished:
        return
    zoom_factor *= 1.1
    redraw_with_zoom()


def zoom_out(event=None):
    global zoom_factor
    if not drawing_finished:
        return
    zoom_factor *= 0.9
    redraw_with_zoom()


# =======================================================
# MOVIMENTO WASD
# =======================================================
def move_up(event=None):
    global camera_dy
    if not drawing_finished:
        return
    camera_dy += 20
    redraw_with_zoom()


def move_down(event=None):
    global camera_dy
    if not drawing_finished:
        return
    camera_dy -= 20
    redraw_with_zoom()


def move_left(event=None):
    global camera_dx
    if not drawing_finished:
        return
    camera_dx -= 20
    redraw_with_zoom()


def move_right(event=None):
    global camera_dx
    if not drawing_finished:
        return
    camera_dx += 20
    redraw_with_zoom()


def apply_view_transform():
    pass  # no macOS, não usamos canvas.scale()


# =======================================================
# EXECUÇÃO PASSO-A-PASSO
# =======================================================
def execute_steps():
    global current_index, drawing_finished

    if current_index >= len(current_steps):
        finish_drawing()
        return

    cmd, value = current_steps[current_index]

    if cmd == "forward":
        turtle.forward(value * zoom_factor)
    elif cmd == "left":
        turtle.left(value)
    elif cmd == "right":
        turtle.right(value)

    current_index += 1

    pct = current_index / len(current_steps) * 100
    progressbar["value"] = pct
    progressbar.update_idletasks()

    root.after(1, execute_steps)


def finish_drawing():
    global drawing_finished
    drawing_finished = True
    progressbar["value"] = 100
    progressbar.update_idletasks()
    print("\nDesenho concluído.")


# =======================================================
# REDESENHO (aplica zoom e WASD)
# =======================================================
def redraw_with_zoom():
    global current_index

    if not drawing_finished:
        return

    turtle.clearscreen()
    turtle.speed(0)
    turtle.hideturtle()

    turtle.penup()
    turtle.goto(camera_dx, camera_dy)
    turtle.pendown()

    current_index = 0
    root.after(1, execute_steps)


# =======================================================
# CAPTAÇÃO DOS PASSOS (GERADORES)
# =======================================================
def record_forward(step):
    yield ("forward", step)


def record_left(angle):
    yield ("left", angle)


def record_right(angle):
    yield ("right", angle)


# ------------------- HILBERT --------------------------
def generate_hilbert_A(level, angle, step):
    if level == 0:
        return

    yield from record_right(angle)
    yield from generate_hilbert_B(level - 1, -angle, step)

    yield from record_forward(step)
    yield from record_left(angle)
    yield from generate_hilbert_A(level - 1, angle, step)

    yield from record_forward(step)
    yield from generate_hilbert_A(level - 1, angle, step)

    yield from record_left(angle)
    yield from record_forward(step)
    yield from generate_hilbert_B(level - 1, -angle, step)

    yield from record_right(angle)


def generate_hilbert_B(level, angle, step):
    if level == 0:
        return

    yield from record_left(angle)
    yield from generate_hilbert_A(level - 1, -angle, step)

    yield from record_forward(step)
    yield from record_right(angle)
    yield from generate_hilbert_B(level - 1, angle, step)

    yield from record_forward(step)
    yield from generate_hilbert_B(level - 1, angle, step)

    yield from record_right(angle)
    yield from record_forward(step)
    yield from generate_hilbert_A(level - 1, -angle, step)

    yield from record_left(angle)


# ------------------- SIERPINSKI --------------------------
def generate_sierpinski_H(level, step):
    if level == 0:
        yield from record_forward(step)
        return

    yield from generate_sierpinski_H(level - 1, step)
    yield from record_right(90)
    yield from generate_sierpinski_C(level - 1, step)
    yield from record_right(90)
    yield from generate_sierpinski_H(level - 1, step)
    yield from record_left(90)
    yield from generate_sierpinski_C(level - 1, step)
    yield from record_left(90)
    yield from generate_sierpinski_H(level - 1, step)


def generate_sierpinski_C(level, step):
    if level == 0:
        yield from record_forward(step)
        return

    yield from generate_sierpinski_C(level - 1, step)
    yield from record_left(90)
    yield from generate_sierpinski_H(level - 1, step)
    yield from record_left(90)
    yield from generate_sierpinski_C(level - 1, step)
    yield from record_right(90)
    yield from generate_sierpinski_H(level - 1, step)
    yield from record_right(90)
    yield from generate_sierpinski_C(level - 1, step)


# =======================================================
# INICIAR DESENHO
# =======================================================
def start_drawing():
    global current_steps, current_index, color_index, drawing_finished
    drawing_finished = False

    curve_type = selected_curve.get()
    order = order_var.get()
    step = float(step_var.get())

    turtle.clearscreen()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pencolor(COLOR_LIST[color_index])
    color_index = (color_index + 1) % len(COLOR_LIST)

    if curve_type == "hilbert":
        current_steps = list(generate_hilbert_A(order, 90, step))
    else:
        current_steps = list(generate_sierpinski_H(order, step))

    current_index = 0
    progressbar["value"] = 0

    root.after(1, execute_steps)


# =======================================================
# INTERFACE TKINTER
# =======================================================
root = tk.Tk()
root.title("Curvas Fractais - Hilbert e Sierpinski")

selected_curve = tk.StringVar(value="hilbert")

ttk.Label(root, text="Escolha a curva:").pack()
ttk.Radiobutton(root, text="Hilbert", variable=selected_curve, value="hilbert").pack()
ttk.Radiobutton(root, text="Sierpinski", variable=selected_curve, value="sierpinski").pack()

ttk.Label(root, text="\nOrdem:").pack()
order_var = tk.IntVar(value=4)
ttk.Scale(root, from_=1, to=8, orient="horizontal", variable=order_var).pack()

ttk.Label(root, text="\nPasso (step):").pack()
step_var = tk.DoubleVar(value=10)
ttk.Scale(root, from_=1, to=30, orient="horizontal", variable=step_var).pack()

progressbar = ttk.Progressbar(root, orient="horizontal", length=300)
progressbar.pack(pady=10)

ttk.Button(root, text="Desenhar", command=start_drawing).pack(pady=5)
ttk.Button(root, text="Salvar PNG", command=save_png).pack(pady=5)
ttk.Button(root, text="Sair", command=root.quit).pack(pady=5)

# Bindings (scroll + WASD)
canvas = turtle.getcanvas()
canvas.bind("<Button-4>", zoom_in)
canvas.bind("<Button-5>", zoom_out)

root.bind("w", move_up)
root.bind("s", move_down)
root.bind("a", move_left)
root.bind("d", move_right)

root.mainloop()