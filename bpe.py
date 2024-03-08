# Bye-Pair Encoding
import string

with open("e.txt", "r", encoding="utf-8") as f:
    text = f.read()[:1000]

idx = 0
text_copy = text[:]
alphabets = string.ascii_letters

for i in range(10):
    z = {}
    for maxlen in range(2, 10):
        x = set([text_copy[i:i + maxlen] for i in range(0, len(text_copy), maxlen)])
        y = {i: text_copy.count(i) for i in x if text_copy.count(i) > 1}
        if not y:
            break

        z[maxlen] = len(y)

    if not any(z.values()):
        break

    best_len = max([k for k, v in z.items() if v == max(z.values())], default=None)

    if best_len is None:
        break

    x = set([text_copy[i:i + best_len] for i in range(0, len(text_copy), best_len)])
    y = {i: text_copy.count(i) for i in x if text_copy.count(i) > 1}

    for i in y.keys():
        replacement = alphabets[idx % len(alphabets)]
        new_t = text_copy.replace(i, replacement)
        if new_t != text_copy:
            # print(f"{replacement} -> {i}")
            text_copy = new_t
            idx += 1

    print(text_copy)
    print(f"{len(text_copy)/len(text)}")
