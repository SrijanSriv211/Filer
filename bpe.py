# Bye-Pair Encoding
import string

text = "aaabdaaabac"

maxlen = 3
n_gram = list(set([text[i:i + maxlen] for i in range(0, len(text), maxlen)]))

vocab = {}
num_idx = 0
letters = string.ascii_letters
for i, x in enumerate(n_gram):
    if text.count(x) <= 1:
        continue

    if i + 1 % len(letters) == 0:
        num_idx += 1

    letter_idx = i % len(letters)
    replacement = f"{num_idx}{letters[letter_idx]}"
    vocab[x] = replacement

for i, x in enumerate(n_gram):
    if x in vocab:
        n_gram[i] = vocab[x]

print(n_gram)
