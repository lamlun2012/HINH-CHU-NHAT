with open("RECT.INP", "r") as f:
    n = int(f.readline())
    xs, ys = [], []
    for _ in range(n):
        x, y = map(int, f.readline().split())
        xs.append(x)
        ys.append(y)

xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)

area = (xmax - xmin) * (ymax - ymin)

with open("RECT.OUT", "w") as f:
    f.write(str(area))
