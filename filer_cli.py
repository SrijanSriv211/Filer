from colorama import init, Fore, Style
import argparse, random, string, time, sys, os

# Initialize Command-line arguments.
Parser = argparse.ArgumentParser(description="Encrypt or Decrypt files.")
Group = Parser.add_mutually_exclusive_group(required=True)

Parser.add_argument("-o", help="Place the output into <file>.")
Parser.add_argument("-s", help="Set a secure <password>.", type=int, required=True)

Group.add_argument("-e", help="Encrypt the input <file>.")
Group.add_argument("-d", help="Decrypt the input <file>.")

Args = Parser.parse_args()

# Initialize Compiler.
init(autoreset = True)

# Create Log Functions.
class LOG:
    def LOG(message):
        CurrentTime = time.strftime("%d-%m-%Y %H-%M-%S")
        print(f"{CurrentTime}: {message}")

    def INFO(message):
        CurrentTime = time.strftime("%d-%m-%Y %H-%M-%S")
        print(f"{CurrentTime} - INFO: {message}")

    def STATUS(message):
        CurrentTime = time.strftime("%d-%m-%Y %H-%M-%S")
        print(f"{Fore.CYAN}{Style.BRIGHT}{CurrentTime} - STATUS: {message}")

    def ERROR(message):
        CurrentTime = time.strftime("%d-%m-%Y %H-%M-%S")
        print(f"{Fore.RED}{Style.BRIGHT}{CurrentTime} - ERROR: {message}")

    def WARN(message):
        CurrentTime = time.strftime("%d-%m-%Y %H-%M-%S")
        print(f"{Fore.YELLOW}{Style.BRIGHT}{CurrentTime} - WARNING: {message}")

class Filer:
    def __init__(self):
        self.Filename = Args.e if Args.e else Args.d
        if Args.o: self.OutputFilename = str(Args.o)
        else:
            CurrentTime = str(time.strftime("%d-%m-%Y %H-%M-%S"))
            FileList = self.Filename.split("\\")[-1]
            Path = self.Filename.split("\\")
            Path.remove(FileList)
            Path = "\\".join(Path)

            self.OutputFilename = f"{Path}\\{CurrentTime}-{FileList}"

        self.Chars = []
        random.seed(Args.s) # Choose a Seed.

        # Split the List of these String Operations, and Join them to Chars List 2 Times.
        for i in range(2): self.Chars.append(list(string.ascii_letters + string.digits + string.punctuation))
        self.Chars[0].append(" ")
        self.Chars[1].append(" ")

        # Shuffle Chars[1] List.
        random.shuffle(self.Chars[1])
        if Args.e: self.Encrypt()
        elif Args.d: self.Decrypt()

    # Encrypt.
    def Encrypt(self):
        Output = []
        with open(self.Filename, "r") as File:
            for Line in File:
                Line = Line.replace("\n", "")
                for Characters in Line:
                    FindIndex = self.Chars[0].index(Characters)
                    Output.append(self.Chars[1][FindIndex])

                Output.append("\n")

        with open(self.OutputFilename, "w") as File:
            for i in Output: File.writelines(i)

        LOG.INFO(f"Your Encrypted Filename is: {self.OutputFilename}")
        LOG.LOG(f"{Fore.GREEN}{Style.BRIGHT}Encrypted.\n")

    # Decrypt.
    def Decrypt(self):
        Output = []
        with open(self.Filename, "r") as File:
            for Line in File:
                Line = Line.replace("\n", "")
                for Characters in Line:
                    FindIndex = self.Chars[1].index(Characters)
                    Output.append(self.Chars[0][FindIndex])

                Output.append("\n")

        with open(self.OutputFilename, "w") as File:
            for i in Output: File.writelines(i)

        LOG.INFO(f"Your Decrypted Filename is: {self.OutputFilename}")
        LOG.LOG(f"{Fore.GREEN}{Style.BRIGHT}Decrypted.\n")

if __name__ == "__main__":
    LOG.WARN("Initialized Filer.")
    if os.path.isfile(str(Args.e)) == False and os.path.isfile(str(Args.d)) == False: LOG.ERROR("No such file or directory")
    else:
        LOG.STATUS("Generating a File for You.\n")
        Filer()
