# Bye-Pair Encoding
import string

def compress(filepath, outpath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [i.split() for i in f.readlines()]

    txt = []
    new_text = []
    text_set = {}
    replacement_num_idx = 0
    ascii_letters = string.ascii_letters
    for idx, line in enumerate(lines):
        for text in line:
            if text not in text_set:
                char_idx = idx % len(ascii_letters)
                if char_idx == 0:
                    replacement_num_idx += 1

                text_set[text] = f"{replacement_num_idx}{ascii_letters[char_idx]}"
                txt.append(text)

            else:
                txt.append(text_set[text])

        new_text.append(" ".join(txt))
        txt = []

    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_text))

compress("e.txt", "e_compressed.txt")



# n_iters = 4
# idx, idx2 = 0, 0
# lst = []
# for t in list(set(text.split())):
#     txt = t[:]

#     for idx3 in range(n_iters):
#         z = {}
#         for maxlen in range(2, 10):
#             x = set([txt[i:i + maxlen] for i in range(0, len(txt), maxlen)])
#             y = {i: txt.count(i) for i in x if txt.count(i) > 1}
#             if not y:
#                 break

#             z[maxlen] = len(y)

#         if not any(z.values()):
#             break

#         best_len = max([k for k, v in z.items() if v == max(z.values())], default=None)

#         if best_len is None:
#             break

#         x = set([txt[i:i + best_len] for i in range(0, len(txt), best_len)])
#         y = {i: txt.count(i) for i in x if txt.count(i) > 1}

#         for i in y.keys():
#             replacement = f"{idx2}{alphabets[idx % len(alphabets)]}"
#             new_t = txt.replace(i, replacement)

#             if new_t != txt:
#                 # print(f"{replacement} -> {i}")
#                 txt = new_t
#                 idx += 1

#                 if idx3 == n_iters - 1:
#                     lst.append(txt)

#                 if idx % len(alphabets) == 0:
#                     idx2 += 1

# print(lst)
# print(len(lst))
# print(len(list(set(text.split()))))
