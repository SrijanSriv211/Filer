from src.Filer.utils import compress

with open("e.txt", "r", encoding="utf-8") as f:
    lines = [i.split() for i in f.readlines()]

c = compress(lines)

with open("e_compressed.txt", "w", encoding="utf-8") as f:
    f.write(c)
