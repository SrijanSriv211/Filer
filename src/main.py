from vendor.AND.AND import AND
from utils.shuffle import shuffle
import string

rng = AND(p=0.578239823)

# txt = "Hello world!"
txt = "Steven Paul Jobs (born Abdul Lateef Jandali, February 24, 1955 - October 5, 2011) was an American business magnate, inventor, and investor. He was the co-founder, chairman, and CEO of Apple; the chairman and majority shareholder of Pixar; a member of The Walt Disney Company's board of directors following its acquisition of Pixar; and the founder, chairman, and CEO of NeXT. He was a pioneer of the personal computer revolution of the 1970s and 1980s, along with his early business partner and fellow Apple co-founder Steve Wozniak."

# ascii_chars = [list(string.ascii_letters + string.digits + string.punctuation + " ")]*2
ascii_chars = [string.ascii_letters + string.digits + string.punctuation + " "]*2

random_nums = []
for _ in range(len(list(ascii_chars[1]))):
    random_nums.append(rng.random())

# randomly_packed_ascii_chars = list(zip(list(ascii_chars[0]), shuffle(list(ascii_chars[1]), random_nums)))[:10]
# print(randomly_packed_ascii_chars)

txt = "".join(shuffle(list(ascii_chars[1]), random_nums))

# Split the text into words and calculate word lengths
words = txt.split()
word_lengths = [len(i) for i in words]

# Create a list of (word, length) pairs and sort it by length in descending order
sorted_word_lengths = sorted(zip(words, word_lengths), key=lambda x: x[1], reverse=True)

# Calculate the length of characters to replace with
# len_of_chars_to_replace_with = int(rng.random() * sorted_word_lengths[0][1])

print(list(zip(words, word_lengths))[:5])

# # Split the text into chunks of length 'len_of_chars_to_replace_with'
# chunks = [txt[i:i+len_of_chars_to_replace_with] for i in range(0, len(txt), len_of_chars_to_replace_with)]
# print(chunks)
