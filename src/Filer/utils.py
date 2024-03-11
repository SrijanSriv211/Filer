def find_global_index(lst, value_to_find):
    for idx, sublist in enumerate(lst):
        if value_to_find in sublist:
            sublist_index = sublist.index(value_to_find)
            global_index = sum(len(sublist) for sublist in lst[:idx]) + sublist_index

            return global_index

    return None

def compress(lines):
    new_text = []
    text_set = {}

    for line in lines:
        compressed_line = []

        for text in line:
            compressed_line.append(text_set[text] if text in text_set else text)

            if text not in text_set:
                text_set[text] = f"{find_global_index(lines, text)},{len(text)}"

        new_text.append(" ".join(compressed_line))

    return "\n".join(new_text)
