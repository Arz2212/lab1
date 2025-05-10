import matplotlib.pyplot as plt


with open('001.dat', 'r') as f:
    lines = f.readlines()


n = int(lines[0])
points = []
for line in lines[1:n+1]:
    x, y = map(float, line.strip().split())
    points.append((x, y))


x = [p[0] for p in points]
y = [p[1] for p in points]


plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=50, color='blue', alpha=0.7)


plt.axis('equal')

x_margin = (max(x) - min(x)) * 0.1
y_margin = (max(y) - min(y)) * 0.1

plt.xlim(min(x) - x_margin, max(x) + x_margin)
plt.ylim(min(y) - y_margin, max(y) + y_margin)

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()