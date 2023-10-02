from vendor.AND.AND import AND
from utils.shuffle import shuffle
import string














"""
rng = AND(p=0.578239823)
r1 = rng.random()

# Create a dictionary that maps characters to their corresponding ASCII values+10 to avoid cases like 00, 01 or 02 as it breaks the decryption.
ascii_chars = {char: str(i+10) for i, char in enumerate(string.ascii_letters + string.digits + string.punctuation + " ")}

txt = "Hello world!"

# Split the text into chunks of length 'len_of_chars_to_replace_with'
max_len_of_each_chunk = 8
chunks = []
for i in range(0, len(txt), max_len_of_each_chunk):
    chunks.append(txt[i : max_len_of_each_chunk + i])

# Append the corresponding ASCII value (with leading zeros) to txt_to_num then append txt_to_num to chunks_to_num
chunks_to_num = []
for chunk in chunks:
    txt_to_num = ""
    for char in chunk:
        if char in ascii_chars:
            txt_to_num += ascii_chars[char]

    chunks_to_num.append(txt_to_num)

# Encrypt and Decrypt but operating on the text to numbers string in each chunk.
encrypted_chunks = []
for i in chunks_to_num:
    encrypted_chunks.append(int(i) * r1**max_len_of_each_chunk)

decrypted_chunks = []
for i in encrypted_chunks:
    decrypted_chunks.append(format(i / r1**max_len_of_each_chunk, f".0f"))

print(chunks_to_num)
print()
print()
print(encrypted_chunks)
print()
print()
print(decrypted_chunks)
"""


"""
txt = "Steven Paul Jobs (born Abdul Lateef Jandali, February 24, 1955 - October 5, 2011) was an American business magnate, inventor, and investor. He was the co-founder, chairman, and CEO of Apple; the chairman and majority shareholder of Pixar; a member of The Walt Disney Company's board of directors following its acquisition of Pixar; and the founder, chairman, and CEO of NeXT. He was a pioneer of the personal computer revolution of the 1970s and 1980s, along with his early business partner and fellow Apple co-founder Steve Wozniak."

ascii_chars = [string.ascii_letters + string.digits + string.punctuation + " "]*2

random_nums = []
for _ in range(len(list(ascii_chars[1]))):
    random_nums.append(rng.random())

txt2 = "".join(shuffle(list(ascii_chars[1]), random_nums))

# Split the text into words and calculate word lengths
words = txt.split()
word_lengths = [len(i) for i in words]

# Create a list of (word, length) pairs and sort it by length in descending order
sorted_word_lengths = sorted(zip(words, word_lengths), key=lambda x: x[1], reverse=True)

# Calculate the length of characters to replace with
len_of_chars_to_replace_with = int(rng.random() * sorted_word_lengths[0][1])

# Split the text into chunks of length 'len_of_chars_to_replace_with'
chunks = []
for i in range(0, len(txt2), len_of_chars_to_replace_with):
    chunks.append(txt2[i : len_of_chars_to_replace_with+i])

randomly_packed_ascii_chars = list(zip(list(ascii_chars[0]), chunks))
print(randomly_packed_ascii_chars)
"""
