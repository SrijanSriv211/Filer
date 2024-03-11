# Bye-Pair Encoding
import string

def find_global_index(lst, value_to_find):
    for i, sublist in enumerate(lst):
        if value_to_find in sublist:
            sublist_index = sublist.index(value_to_find)
            global_index = sum(len(sublist) for sublist in lst[:i]) + sublist_index

            return global_index

    return None

def compress(lines):
    new_text = []
    text_set = {}
    replacement_num_idx = 0
    ascii_letters = string.ascii_letters

    for line_no, line in enumerate(lines):
        compressed_line = []

        for text in line:
            compressed_line.append(text_set[text] if text in text_set else text)

            if text not in text_set:
                char_idx = line_no % len(ascii_letters)
                if char_idx == 0:
                    replacement_num_idx += 1

                # text_set[text] = f"{replacement_num_idx}{ascii_letters[char_idx]}"
                text_set[text] = f"{find_global_index(lines, text)},{len(text)}"

        new_text.append(" ".join(compressed_line))

    return "\n".join(new_text)

with open("e.txt", "r", encoding="utf-8") as f:
    lines = [i.split() for i in f.readlines()]

c = compress(lines)

with open("e_compressed.txt", "w", encoding="utf-8") as f:
    f.write(c)



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
