from src.Filer.utils import compress, decompress

with open("e.txt", "r", encoding="utf-8") as f:
    lines = [i.split() for i in f.readlines()]

c = compress(lines)

with open("e_compressed.txt", "w", encoding="utf-8") as f:
    f.write(c)



with open("e_compressed.txt", "r", encoding="utf-8") as f:
    lines = [i.split() for i in f.readlines()]

d = decompress(lines)

with open("e_decompressed.txt", "w", encoding="utf-8") as f:
    f.write(d)
