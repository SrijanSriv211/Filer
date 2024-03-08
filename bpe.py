# Bye-Pair Encoding
text = "aaabdaaabac"

maxlen = 2
x = set([text[i:i + maxlen] for i in range(0, len(text), maxlen)])
y = {i: text.count(i) for i in x if text.count(i) > 1}

print(y)
