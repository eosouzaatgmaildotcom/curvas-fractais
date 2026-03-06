# hilbert.py
import tkinter as tk
from tkinter import ttk
import time
import platform
import os
import sys
import random
from outros_fractais import KochGenerator, CesaroGenerator, DragonGenerator
import webbrowser

try:
    from hilberts import HilbertGenerator
    from sierpins import SierpinskiGenerator
except ImportError as e:
    print(f"Erro de importação: {e}")
    print("Certifique-se de que 'hilberts.py' e 'sierpins.py' estão na mesma pasta que este arquivo.")
    sys.exit(1)

class FractalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Fractais - Hilbert & Sierpinski")
        
        # Forçar a janela para o primeiro plano no MacOS
        if platform.system() == 'Darwin':
            try:
                os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
            except:
                pass
            self.root.lift()
            self.root.attributes('-topmost', True)
            self.root.after_idle(self.root.attributes, '-topmost', False)
        
        # Controles de estado
        self.is_drawing = False
        self.drawing_complete = False
        self.lines_to_draw = []
        self.current_line_index = 0
        self.start_time = 0
        self.current_color = "#000000" # Cor inicial padrão
        
        self.setup_ui()
        
        self.root.update_idletasks()
        self.root.eval('tk::PlaceWindow . center')
        
    def setup_ui(self):
        control_frame = ttk.LabelFrame(self.root, text="Parâmetros do Fractal")
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        ttk.Label(control_frame, text="Curva:").grid(row=0, column=0, padx=5, pady=5)
        self.fractal_type = tk.StringVar(value="Hilbert")
        ttk.Combobox(control_frame, textvariable=self.fractal_type, 
             values=["Hilbert", "Sierpinski", "Koch", "Cesaro", "Dragon"], 
             state="readonly", width=12).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Recursão:").grid(row=0, column=2, padx=5, pady=5)
        self.iterations = tk.IntVar(value=4)
        ttk.Spinbox(control_frame, from_=1, to=28, textvariable=self.iterations, width=3).grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Velocidade:").grid(row=0, column=4, padx=5, pady=5)
        self.speed = tk.IntVar(value=50)
        ttk.Spinbox(control_frame, from_=1, to=2000, textvariable=self.speed, width=5).grid(row=0, column=5, padx=5, pady=5)
        
        self.btn_draw = ttk.Button(control_frame, text="Executar", command=self.start_drawing)
        self.btn_draw.grid(row=0, column=6, padx=10, pady=5)

        # Botão para abrir a Wikipedia
        self.btn_wiki = ttk.Button(control_frame, text="O que são Fractais?", command=self.open_wikipedia)
        self.btn_wiki.grid(row=0, column=7, padx=10, pady=5)

        # Canvas ajustado para fundo branco
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white", highlightthickness=0)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Binds para Zoom e Pan (Navegação)
        self.canvas.bind("<ButtonPress-1>", self.start_pan)
        self.canvas.bind("<B1-Motion>", self.pan)
        self.canvas.bind("<MouseWheel>", self.zoom)  
        self.canvas.bind("<Button-4>", self.zoom)    
        self.canvas.bind("<Button-5>", self.zoom)    
        
        status_frame = ttk.Frame(self.root)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(status_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.status_label = ttk.Label(status_frame, text="Pronto.")
        self.status_label.pack(side=tk.RIGHT)

    # --- Funções de Navegação e Zoom ---
    def start_pan(self, event):
        if not self.drawing_complete: return
        self.canvas.scan_mark(event.x, event.y)

    def pan(self, event):
        if not self.drawing_complete: return
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def zoom(self, event):
        if not self.drawing_complete: return
        
        if event.num == 4 or getattr(event, 'delta', 0) > 0:
            scale_factor = 1.1 
        elif event.num == 5 or getattr(event, 'delta', 0) < 0:
            scale_factor = 0.9 
        else:
            return
            
        self.canvas.scale("all", event.x, event.y, scale_factor, scale_factor)

    # --- Funções de Desenho ---
    def start_drawing(self):
        if self.is_drawing:
            return
            
        self.canvas.delete("all")
        self.is_drawing = True
        self.drawing_complete = False
        self.btn_draw.config(state=tk.DISABLED)
        
        # Gera cor aleatória a cada execução (garantindo que seja legível no branco)
        r = random.randint(0, 200)
        g = random.randint(0, 200)
        b = random.randint(0, 200)
        self.current_color = f'#{r:02x}{g:02x}{b:02x}'
        
        fractal = self.fractal_type.get()
        depth = self.iterations.get()
        
        self.root.update()
        width = int(self.canvas.winfo_width())
        height = int(self.canvas.winfo_height())
        
        if width <= 1: width = 800
        if height <= 1: height = 600
            
        x0 = width / 2
        y0 = height / 2
        proporcao = 3
        
        if fractal == "Hilbert":
            gen = HilbertGenerator(proporcao=proporcao)
            incremento = 300
            for _ in range(1, depth):
                incremento /= 2
                
            start_x = x0 + (incremento / 2)
            start_y = y0 - (incremento / (2 * proporcao))
            self.lines_to_draw = gen.generate(start_x, start_y, incremento, depth)
            
        elif fractal == "Sierpinski":
            gen = SierpinskiGenerator(proporcao=proporcao)
            square_size = 300
            u = square_size / 4
            for _ in range(1, depth):
                u /= 2
                
            start_x = x0 - 2 * u
            start_y = y0 - u - (u / (2 * proporcao))
            self.lines_to_draw = gen.generate(start_x, start_y, u, depth)
        elif fractal == "Koch":
            gen = KochGenerator()
            self.lines_to_draw = gen.generate(x0 - 200, y0 + 100, 400, depth)
        elif fractal == "Cesaro":
            gen = CesaroGenerator()
            self.lines_to_draw = gen.generate(x0 - 200, y0 + 100, 400, depth)
        elif fractal == "Dragon":
            gen = DragonGenerator()
            # Ajuste de escala para o dragão não sumir da tela
            self.lines_to_draw = gen.generate(x0 - 100, y0, 300, depth)

        self.current_line_index = 0
        self.start_time = time.time()
        self.update_drawing()

    def open_wikipedia(self):
        """Abre o artigo da Wikipedia sobre fractais no navegador."""
        url = "https://pt.wikipedia.org/wiki/Fractal"
        webbrowser.open(url)

    def update_drawing(self):
        if not self.is_drawing:
            return
            
        speed = self.speed.get()
        end_index = min(self.current_line_index + speed, len(self.lines_to_draw))
        
        # Utiliza a cor aleatória gerada para preencher as linhas
        for i in range(self.current_line_index, end_index):
            x1, y1, x2, y2 = self.lines_to_draw[i]
            self.canvas.create_line(x1, y1, x2, y2, fill=self.current_color, width=1)
        
        self.current_line_index = end_index
        total_lines = len(self.lines_to_draw)
        progress = (self.current_line_index / total_lines) * 100 if total_lines > 0 else 100
        
        self.progress_var.set(progress)
        elapsed_time = time.time() - self.start_time
        
        if self.current_line_index > 0:
            lines_per_sec = self.current_line_index / elapsed_time
            remaining_lines = total_lines - self.current_line_index
            eta = remaining_lines / lines_per_sec if lines_per_sec > 0 else 0
            self.status_label.config(text=f"{progress:.1f}% | Total: {total_lines} | ETA: {eta:.1f}s")
        
        if self.current_line_index < total_lines:
            self.root.after(16, self.update_drawing)
        else:
            self.is_drawing = False
            self.drawing_complete = True
            self.btn_draw.config(state=tk.NORMAL)
            self.status_label.config(text=f"Concluído em {elapsed_time:.2f}s! (Arraste e use o scroll para zoom)")

if __name__ == "__main__":
    root = tk.Tk()
    app = FractalApp(root)
    root.mainloop()