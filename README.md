# Fractal Curves - Hilbert e Sierpinski

### Retro Fractal Generator: Hilbert & Sierpinski Curves

![Hilbert curve fractal](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Hilbert_curve_1-6.svg/512px-Hilbert_curve_1-6.svg.png)

This project is a modern Python port of a legacy 1990s Turbo Pascal program. It generates **Hilbert** and **Sierpinski** space-filling curves using recursive algorithms. 

The original codebase relied on the synchronous MS-DOS `Graph` (`BGI`) library. This modernization replaces the old blocking rendering with a responsive `Tkinter` Graphical User Interface (GUI). The new architecture calculates the geometric vertices in the background and renders the drawing progressively, allowing users to watch the algorithm unfold in real-time without freezing the interface.

## 🚀 Features

* **Animated Rendering:** Watch the recursive curves being drawn segment by segment.
* **Real-time Analytics:** Tracks rendering progress and calculates the Estimated Time of Arrival (ETA) based on the current frame rate.
* **Interactive Canvas:** Once the drawing is complete, you can **Pan** (click and drag) and **Zoom** (scroll wheel) to explore the deep complexity of the fractals.
* **Dynamic Styling:** Generates a random, high-contrast dark color for the drawing strokes against a clean white background on every run.
* **Modular Architecture:** Strictly maintains the original separation of concerns across three distinct files.

## 📁 Project Structure

* `hilbert.py`: The main orchestrator. Handles the Tkinter GUI, asynchronous frame updates, and user interactions (pan/zoom).
* `hilberts.py`: Encapsulates the mathematical generator and recursive logic for the Hilbert curve.
* `sierpins.py`: Encapsulates the mathematical generator and recursive logic for the Sierpinski curve.

## ⚙️ Requirements & Execution

This project uses only Python's standard libraries. No external dependencies are required.

1. Ensure you have **Python 3** installed.
2. Clone this repository and navigate to the folder containing the three files.
3. Run the main application:
   ```bash
   python3 hilbert.py

Note for MacOS Users: Tkinter handles window management differently on macOS. The script is optimized to force the window to the foreground. If you encounter errors regarding _tkinter, ensure you have the Tkinter module installed (e.g., via Homebrew: brew install python-tk).

## 🎛️ Recommended Parameters for Observation
The GUI allows you to tweak the recursion depth and drawing speed. Here are some great parameter combinations to observe the algorithm's behavior:

1. The "Educational" Mode

* Curve: Sierpinski
* Recursion Level: 4 or 5
* Speed: 5 lines/frame

Why: A slow drawing speed lets you clearly see the recursive "depth-first" path the algorithm takes to fill the space.

2. The "Hypnotic Flow"

* Curve: Hilbert
* Recursion Level: 6
* Speed: 50 lines/frame

Why: The perfect balance. It generates a complex, dense curve, but at a speed that is highly satisfying to watch without taking too long.

3. The "Stress Test & Deep Zoom"

* Curve: Hilbert (or Sierpinski)
* Recursion Level: 8
* Speed: 1000 lines/frame

Why: Level 8 generates a massive amount of coordinate segments. Pumping up the speed allows the application to render it in a reasonable timeframe (watch the ETA tracker!). Once it finishes, use your mouse wheel to zoom deep into the intricate details of the final fractal.

## 📜 License
This project is open-source and available under the MIT License. Feel free to fork, modify, and learn from the code!
