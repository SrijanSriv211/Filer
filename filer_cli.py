from src.Filer import Filer
from pprint import pprint
import argparse, string, sys, os

# Initialize command-line arguments.
parser = argparse.ArgumentParser(description="A powerful text encryption and decryption program.")
encrypt_or_decrypt_group = parser.add_mutually_exclusive_group(required=True)
text_or_file_input_group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument("-p", help="Strong password for better security.", type=str, required=True)
parser.add_argument("-o", help="Place the output into <file>.")
parser.add_argument("-m", help="The maximum length of a string in each chunk.", type=int, default=4)
parser.add_argument("-s", help="The offset to shift chars by.", type=int, default=-1)

encrypt_or_decrypt_group.add_argument("-e", help="Encrypt", action="store_true")
encrypt_or_decrypt_group.add_argument("-d", help="Decrypt", action="store_true")

text_or_file_input_group.add_argument("-t", help="Text input from the command line.")
text_or_file_input_group.add_argument("-f", help="Takes a text file as an input.")

args = parser.parse_args()

# Check for the input source and append all the input texts to the inputs list.
text = []
if args.t:
    text.append(args.t)

elif args.f:
    if os.path.isfile(args.f) == False:
        print(f"{args.f}: No such file or directory")
        sys.exit()

    with open(args.f, "r", encoding="utf-8") as f:
        for i in f.readlines():
            text.append(i[:-1])

# Create seed from the given password.
ascii_map = string.printable
ascii_map_idx = []
sequential_idx = []
for i, x in enumerate(args.p):
    sequential_idx.append(i+1)
    ascii_map_idx.append(ascii_map.index(x))

# Calculate weights of each character.
char_weights = []
for i in sequential_idx:
    ascii_map_sum = sum(ascii_map_idx)
    char_weights.append(i * ascii_map_sum)

seed = 1/sum(char_weights)

# Initialize Filer and start encrypting or decrypting.
list_of_outputs = []
filer = Filer(seed)
filer.max_len = args.m
filer.offset = sum(char_weights) if args.s == -1 else args.s

if args.e:
    for encrypted_text in text:
        output = [str(i) for i in filer.encrypt(encrypted_text)]
        list_of_outputs.append(output)

elif args.d:
    for encrypted_text in text:
        new_encrypted_text = [i for i in encrypted_text.split()]
        list_of_outputs.append(filer.decrypt(new_encrypted_text))

# Print or save the output
if args.o:
    file = open(args.o, "w")

    if args.e:
        for output in list_of_outputs:
            file.write(" ".join(output) + "\n")

    elif args.d:
        for output in list_of_outputs:
            file.write(output + "\n")

    file.close()

else:
    pprint(list_of_outputs)
