import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def build_matrix_A(size):
    A = np.zeros((size, size))
    for i in range(size):
        A[i, i] = 1
        if i > 0:
            A[i, i - 1] = -1
    return A

def simulate_process(u0, steps=255):
    A = build_matrix_A(len(u0))
    U = [u0.copy()]
    for _ in range(steps):
        u_next = U[-1] - 0.5 * A @ U[-1]
        U.append(u_next)
    return np.array(U)

u0 = np.loadtxt("3.dat")
result = simulate_process(u0, steps=255)

fig, ax = plt.subplots()
line, = ax.plot(result[0], lw=2)
ax.set_ylim(result.min() - 1, result.max() + 1)
ax.set_title("Эволюция функции u(x) во времени")
ax.set_xlabel("x")
ax.set_ylabel("u(x)")

def update(frame):
    line.set_ydata(result[frame])
    ax.set_title(f"Шаг времени: {frame}")
    return line,

ani = FuncAnimation(fig, update, frames=len(result), blit=True)

# Сохранение в GIF
ani.save("evolution.gif", writer=PillowWriter(fps=20))
