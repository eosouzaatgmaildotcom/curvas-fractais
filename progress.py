# progress.py
import time
import sys

class ProgressTracker:
    def __init__(self, total_steps):
        self.total_steps = total_steps
        self.done_steps = 0
        self.start_time = time.time()

    def step(self):
        self.done_steps += 1
        self._maybe_print()

    def _maybe_print(self):
        # Atualiza apenas a cada 1% concluído
        if self.done_steps % max(1, self.total_steps // 100) != 0:
            return
        
        pct = (self.done_steps / self.total_steps) * 100
        elapsed = time.time() - self.start_time
        if self.done_steps > 0:
            remaining = elapsed * (self.total_steps / self.done_steps - 1)
        else:
            remaining = 0

        sys.stdout.write(
            f"\rProgresso: {pct:5.1f}% | "
            f"Passos: {self.done_steps}/{self.total_steps} | "
            f"Tempo restante: {remaining:6.1f}s"
        )
        sys.stdout.flush()

    def finish(self):
        sys.stdout.write("\nConcluído!\n")
        sys.stdout.flush()