from src.Filer.filer import Filer
from src.Filer.utils import comp, decomp
import argparse, string, sys, os

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

    return comp(list_of_outputs)

def decrypt(filer, encrypted_text):
    list_of_outputs = []
    for txt in decomp([i.split() for i in encrypted_text]):
        new_encrypted_text = [i for i in txt.split()]
        list_of_outputs.append(filer.decrypt(new_encrypted_text))

    return "\n".join(list_of_outputs)

# Initialize command-line arguments.
parser = argparse.ArgumentParser(description="A powerful text encryption and decryption program.")
encrypt_or_decrypt_group = parser.add_mutually_exclusive_group(required=True)
text_or_file_input_group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument("-p", help="Strong password for better security.", type=str, required=True)
parser.add_argument("-o", help="Place the output into <file>.")
parser.add_argument("-m", help="The maximum length of a string in each chunk.", type=int, default=4)

encrypt_or_decrypt_group.add_argument("-e", help="Encrypt", action="store_true")
encrypt_or_decrypt_group.add_argument("-d", help="Decrypt", action="store_true")

text_or_file_input_group.add_argument("-t", help="Text input from the command line.")
text_or_file_input_group.add_argument("-f", help="Takes a text file as an input.")

args = parser.parse_args()

# Load text from the text file.
text = [args.t] if args.t else load_text(args.f) if args.f else None

# Generate seed and init Filer.
seed = generate_seed(args.p)
filer = init_filer(seed, args.m)

# Encrypt/Decrypt
output = encrypt(filer, text) if args.e else decrypt(filer, text) if args.d else ""

# Print or save the output
if args.o:
    with open(args.o, "w", encoding="utf-8") as f:
        f.write(output)

else:
    print(output)
