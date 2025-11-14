s, n, d = 0.0, 1.0, 1.0

while n <= 39:
    s += n / d
    n += 2
    d *= 2

print(f'{s:.2f}')
