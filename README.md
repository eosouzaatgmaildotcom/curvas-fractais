# curvas-fractais
Curvas Fractais - Hilbert e Sierpinski

### Visualizador Interativo de Fractais (Hilbert & Sierpinski) com Interface Gráfica

**Compatível com macOS, Windows e Linux**

Este projeto oferece um visualizador interativo das curvas fractais **Hilbert** e **Sierpinski**, permitindo explorar essas estruturas geométricas de forma dinâmica e intuitiva.
Foi especialmente projetado para funcionar de forma **estável no macOS**, onde Tkinter + Turtle exigem cuidados adicionais.

---

# 📌 Recursos

### ✔ Interface gráfica completa (Tkinter)

O programa possui uma janela inicial onde você pode escolher:

* Tipo de curva: **Hilbert** ou **Sierpinski**
* Ordem da curva (nível do fractal)
* Tamanho do passo (step)
* Iniciar desenho
* Salvar como PNG

---

### ✔ Execução passo-a-passo (sem threads)

O desenho é realizado de forma incremental usando:

```python
root.after(...)
```

Isso garante:

* Interface sempre responsiva
* Nenhum travamento
* Total compatibilidade com macOS

---

### ✔ Barra de progresso gráfica

A execução do fractal é exibida com uma barra de progresso dinâmica.

---

### ✔ Zoom funcional (macOS-friendly)

O zoom é implementado corretamente no macOS através de uma estratégia geométrica:

* Aumenta/diminui o passo durante o redesenho
* **Scroll do mouse** aumenta/diminui o zoom
* Rápido e seguro — sem `canvas.scale()`

---

### ✔ Movimento da “câmera” com WASD

Somente após o desenho estar 100% concluído, você pode navegar pela curva com:

| Tecla | Ação                |
| ----- | ------------------- |
| **W** | mover para cima     |
| **A** | mover para esquerda |
| **S** | mover para baixo    |
| **D** | mover para direita  |

---

### ✔ Alternância automática de cores

Cada curva desenhada utiliza uma cor diferente, rotacionada a partir de uma paleta.

---

### ✔ Exportação como PNG

A curva pode ser salva via botão:

```
Salvar PNG
```

ou manualmente a qualquer momento.

---

# 🧩 Curvas disponíveis

## 🔷 Curva de Hilbert

Um fractal espaço-preenchido que mapeia 1D para 2D continuamente.

## 🔺 Curva de Sierpinski (versão H/C do Pascal original)

Uma variação labiríntica inspirada no triângulo de Sierpinski, modelada a partir do algoritmo dos anos 90 em Pascal.

---

# 🛠 Como executar

## 1. Instale o Python

Recomendado: **Python 3.10+**

## 2. Instale dependências

Somente o Pillow é necessário:

```bash
pip install pillow
```

## 3. Execute o programa

```bash
python3 hilbert.py
```

---

# 🗂 Estrutura do projeto

```
/ (raiz)
├── hilbert.py        # Interface gráfica e motor principal
├── hilberts.py       # Implementação original da curva de Hilbert
├── sierpins.py       # Implementação original da curva de Sierpinski
├── progress.py       # Sistema de progresso no terminal
└── README.md         # Este arquivo
```

---

# ⚙ Detalhes técnicos

### 🔸 Execução sem threads

Essencial para evitar erro `mutated while enumerated` no macOS.

### 🔸 Zoom geométrico

Cada comando `"forward"` é multiplicado por `zoom_factor`.

### 🔸 Movimento de câmera

Após o desenho, redesenha usando novos offsets (`camera_dx`, `camera_dy`).

### 🔸 Captura de tela (PNG)

Usa `PIL.ImageGrab` para salvar a janela Turtle.

### 🔸 Geradores para curvas

As recursões Hilbert/Sierpinski são convertidas em sequências iteráveis de passos:

```python
("forward", step)
("left", angle)
("right", angle)
```

---

# 🎯 Objetivo do Projeto

Este programa nasceu a partir da necessidade de:

* Reviver código legado dos anos 90 escrito em **Pascal**, usando **Graph** da Borland.
* Converter essas curvas para **Python moderno**.
* Acrescentar funcionalidades interativas inexistentes na época:

  * Menu gráfico
  * Zoom
  * Movimento de câmera
  * Salvamento em PNG
  * Cores dinâmicas
  * Barra de progresso
  * Interface responsiva

O resultado é uma ferramenta educacional e visualmente rica para quem deseja:

* Estudar recursão
* Explorar fractais
* Comparar implementações modernas e legadas
* Criar arte generativa

---

# 🤝 Contribuições

Pull requests são bem-vindos!
Sugestões de melhorias no zoom, rotação ou novos fractais também.

---

# 📜 Licença

MIT — livre para uso, edição e distribuição.
