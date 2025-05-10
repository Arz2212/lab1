import numpy as np
import matplotlib.pyplot as plt

def moving_average(signal, window_size=10):
    result = np.zeros_like(signal, dtype=float)
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        result[i] = np.mean(signal[start:i + 1])
    return result

signal = np.loadtxt("signal02.dat")
filtered = moving_average(signal, window_size=10)

plt.figure(figsize=(10, 5))
plt.plot(signal, label='Исходный сигнал', alpha=0.6)
plt.plot(filtered, label='Фильтрованный сигнал (скользящее среднее)', linewidth=2)
plt.title('Сглаживание данных с помощью скользящего среднего')
plt.xlabel('Время (отсчёты)')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
