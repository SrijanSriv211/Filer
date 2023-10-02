from src.Filer import Filer
from pprint import pprint
import argparse, sys, os

# Initialize command-line arguments.
parser = argparse.ArgumentParser(description="A powerful text encryption and decryption program.")
encrypt_or_decrypt_group = parser.add_mutually_exclusive_group(required=True)
text_or_file_input_group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument("-s", help="A random seed in the range (0, 1) that acts like a password", type=float, required=True)
parser.add_argument("-o", help="Place the output into <file>.")
parser.add_argument("-m", help="The maximum length of a string in each chunk.", type=int, default=4)
parser.add_argument("-c", help="The common exponent used with the random encryption key to encrypt or decrypt text", type=int, default=8)

encrypt_or_decrypt_group.add_argument("-e", help="Encrypt", action="store_true")
encrypt_or_decrypt_group.add_argument("-d", help="Decrypt", action="store_true")

text_or_file_input_group.add_argument("-t", help="Text input from the command line.")
text_or_file_input_group.add_argument("-f", help="Takes a text file as an input.")

args = parser.parse_args()

# Check for the input source and append all the input texts to the inputs list.
inputs = []
if args.t:
    inputs.append(args.t)

elif args.f:
    if os.path.isfile(args.f) == False:
        print(f"{args.f}: No such file or directory")
        sys.exit()

    file = open(args.f, "r")
    for i in file.readlines():
        inputs.append(i[:-1])
    file.close()

# Initialize Filer and start encrypting or decrypting.
list_of_outputs = []
filer = Filer(args.s)
filer.max_len = args.m
filer.common_exponent = args.c

if args.e:
    for encrypted_text in inputs:
        output = [str(i) for i in filer.encrypt(encrypted_text)]
        list_of_outputs.append(output)

elif args.d:
    for encrypted_text in inputs:
        new_encrypted_text = [float(i) for i in encrypted_text.split()]
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

