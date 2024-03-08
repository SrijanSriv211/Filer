# Bye-Pair Encoding
text = "aaabdaaabac"
n = 0
t = text[:]

for i in range(2):
    z = {}
    for maxlen in range(2, 10):
        x = set([t[i:i + maxlen] for i in range(0, len(t), maxlen)])
        y = {i: t.count(i) for i in x if t.count(i) > 1}
        if len(y) == 0:
            break

        z[maxlen] = len(y)

    best_len = max([k for k, v in z.items() if v == max(z.values())])

    x = set([t[i:i + best_len] for i in range(0, len(t), best_len)])
    y = {i: t.count(i) for i in x if t.count(i) > 1}

    for i in y.keys():
        new_t = t.replace(i, f"{n}")
        if new_t != t:
            print(f"{n} -> {i}")
            t = new_t
            n += 1

    print(t)
    print()
