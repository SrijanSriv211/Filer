def find_idx(lst, txt):
    for i, x in enumerate(lst):
        if txt in x:
            x_idx = x.index(txt)
            global_idx = sum(len(x) for x in lst[:i]) + x_idx

            return global_idx

    return None

def find_txt(lst, idx):
    count = 0
    for i in lst:
        # Check if the current sub-list contains the text corresponding to the global_idx.
        if count + len(i) > idx:
            return i[idx - count] # Calculate the local index within the current sub-list and return it's text.

        count += len(i)

    return None

# Compress
def comp(lines):
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

# Decompress
def decomp(lines):
    decompressed_text = []

    for line in lines:
        decompressed_line = []

        for text in line:
            decompressed_line.append(find_txt(lines, int(text[:-1])) if text.endswith(";") else text)

        decompressed_text.append(" ".join(decompressed_line))

    return decompressed_text
