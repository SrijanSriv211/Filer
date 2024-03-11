def find_idx(lst, txt):
    for i, x in enumerate(lst):
        if txt in x:
            x_idx = x.index(txt)
            global_idx = sum(len(x) for x in lst[:i]) + x_idx

            return global_idx

    return None

def find_txt(lst, idx):
    # TODO: Re-write this function. It doesn't work.
    # for i, x in enumerate(lst):
    #     x_idx = idx - sum(len(x) for x in lst[:i])
    #     if x_idx < len(x) - 1:
    #         return x[x_idx]

    return None

def compress(lines):
    compressed_text = []
    text_set = {}

    for line in lines:
        compressed_line = []

        for text in line:
            compressed_line.append(text_set[text] if text in text_set else text)

            if text not in text_set:
                text_set[text] = f"{find_idx(lines, text)};"

        compressed_text.append(" ".join(compressed_line))

    return "\n".join(compressed_text)

def decompress(lines):
    decompressed_text = []

    for line in lines:
        decompressed_line = []

        for text in line:
            if text.endswith(";"):
                find_txt(lines, int(text[:-1]))

    return "\n".join(decompressed_text)
