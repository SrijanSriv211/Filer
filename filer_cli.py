from src.utils import *
import argparse, sys

if len(sys.argv) > 1:
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

    text = []
    if args.t: text.append(args.t)
    elif args.f: text = load_text(args.f)

    seed = generate_seed(args.p)
    filer = init_filer(seed, args.m)

    if args.e: list_of_outputs = encrypt(filer, text)
    elif args.d: list_of_outputs = decrypt(filer, text)

    # Print or save the output
    if args.o:
        file = open(args.o, "w")

        if args.e:
            for i in list_of_outputs:
                file.write(" ".join(i) + "\n")

        elif args.d:
            for i in list_of_outputs:
                file.write(i + "\n")

        file.close()

    else:
        for i in list_of_outputs:
            print("".join(i))

else:
    filepath = input("Enter a file path: ").strip()
    if filepath == "":
        text = [input("Enter a text: ").strip()]
        if text == "":
            print("No file path or plain text found")
            sys.exit()

    else:
        text = load_text(filepath)

    password = input("Enter a password: ").strip()
    if password == "":
        print("No password found")
        sys.exit()

    seed = generate_seed(password)
    outpath = input("Enter the output file path (optional): ").strip()

    maxlen = input("Enter the maximum length of a string in each chunk (optional): ").strip()
    if maxlen == "" or maxlen.isdigit() == False:
        maxlen = 4

    filer = init_filer(seed, maxlen)

    method = input("Type the index number to select your preferred method.\n1. Encrypt\n2. Decrypt\n> ").strip()
    if method == "":
        print("No processing method found")
        sys.exit()

    elif method == "1":
        list_of_outputs = encrypt(filer, text)

        if outpath == "":
            for i in list_of_outputs:
                print("".join(i))

        else:
            with open(outpath, "w") as f:
                for i in list_of_outputs:
                    f.write(" ".join(i) + "\n")

    elif method == "2":
        list_of_outputs = decrypt(filer, text)

        if outpath == "":
            for i in list_of_outputs:
                print(" ".join(i))

        else:
            with open(outpath, "w") as f:
                for i in list_of_outputs:
                    f.write(i + "\n")

    else:
        print(f"{method}: Invalid method index")
        sys.exit()
