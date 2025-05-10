import matplotlib.pyplot as plt

with open('2.dat', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

frames = []
for i in range(0, len(lines), 2):
    x = list(map(float, lines[i].split()))
    y = list(map(float, lines[i + 1].split()))
    frames.append((x, y))
num_frames =  len(frames)
frames = frames[:num_frames]
all_x = [x for frame in frames for x in frame[0]]
all_y = [y for frame in frames for y in frame[1]]
x_min, x_max = min(all_x), max(all_x)
y_min, y_max = min(all_y), max(all_y)
x_margin = (x_max - x_min) * 0.1
y_margin = (y_max - y_min) * 0.1

x_lim = (x_min - x_margin, x_max + x_margin)
y_lim = (y_min - y_margin, y_max + y_margin)

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
fig.tight_layout(pad=4.0)

for i, (x, y) in enumerate(frames):
    row = i // 3
    col = i % 3
    ax = axs[row, col]

    ax.plot(x, y, 'bo-', markersize=4, linewidth=1)
    ax.set_title(f'Кадр {i + 1}', fontsize=12)
    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)

    ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

    if row == 1:
        ax.set_xlabel('X координата', fontsize=10)
    if col == 0:
        ax.set_ylabel('Y координата', fontsize=10)


plt.suptitle('Эволюция процесса по кадрам', fontsize=14)
plt.show()