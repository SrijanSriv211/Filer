# Bye-Pair Encoding
text = "aaabdaaabac"

for maxlen in range(len(text)):
    x = list(set([text[i:i+maxlen+1] for i in range(0, len(text), maxlen+1)]))
    y = {i: text.count(i) for i in x}
    print(f"{maxlen+1}.", max(y.values()), len(y))
