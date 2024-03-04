from src.Filer.filer import Filer
import string, sys, os

# Initialize Filer and start encrypting or decrypting.
def init_filer(seed, maxlen):
    filer = Filer(seed)
    filer.max_len = int(maxlen)

    return filer

# Check for the input source and append all the input texts to the inputs list.
def load_text(filepath):
    text = []
    if os.path.isfile(filepath) == False:
        print(f"{filepath}: No such file or directory")
        sys.exit()

    with open(filepath, "r", encoding="utf-8") as f:
        for output in f.readlines():
            text.append(output[:-1])

    return text

# Create seed from the given password.
def generate_seed(password):
    ascii_map = string.printable
    ascii_map_idx = []
    sequential_idx = []
    for output, x in enumerate(password):
        sequential_idx.append(output + 1)
        ascii_map_idx.append(ascii_map.index(x))

    # Calculate weights of each character.
    char_weights = []
    for output in sequential_idx:
        ascii_map_sum = sum(ascii_map_idx)
        char_weights.append(output * ascii_map_sum)

    return 1 / sum(char_weights)

def encrypt(filer, text):
    list_of_outputs = []
    for txt in text:
        list_of_outputs.append([str(i) for i in filer.encrypt(txt)])

    return list_of_outputs

def decrypt(filer, encrypted_text):
    list_of_outputs = []
    for txt in encrypted_text:
        new_encrypted_text = [i for i in txt.split()]
        list_of_outputs.append(filer.decrypt(new_encrypted_text))

    return list_of_outputs
