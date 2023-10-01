from vendor.AND.AND import AND
from utils.shuffle import shuffle
import string

# rng = AND(p=0.578239823)
rng = AND()
r1 = rng.random()

text = "Hello world!"
text2 = "Hi Welcome!"

ascii_chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
random_nums = []
for _ in range(len(ascii_chars)):
    random_nums.append(rng.random())

print(ascii_chars[:10])
print(shuffle(ascii_chars, random_nums)[:10])
