from src.Filer.utils import compress, decompress

with open("e.txt", "r", encoding="utf-8") as f:
    lines = [i.split() for i in f.readlines()]

c = compress(lines)

decompress([i.split() for i in c.split("\n")])
