from vendor.AND.AND import AND
from utils.shuffle import shuffle
import string

rng = AND(p=0.578239823)
r1 = rng.random()

txt = "Hello world!"
txt2 = "Hi Welcome!"

#* Works perfectly! DO NOT DELETE.
# ascii_chars = [list(string.ascii_letters + string.digits + string.punctuation + " ")]*2

# random_nums = []
# for _ in range(len(ascii_chars[1])):
#     random_nums.append(rng.random())

# randomly_packed_ascii_chars = list(zip(ascii_chars[0], shuffle(ascii_chars[1], random_nums)))[:10]
# print(randomly_packed_ascii_chars)
