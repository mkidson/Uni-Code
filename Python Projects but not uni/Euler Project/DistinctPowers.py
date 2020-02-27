
tots = []

for a in range(2, 101):
    for b in range(2, 101):
        c = a**b
        if c in tots:
            pass
        else:
            tots.append(c)

print(len(tots))