# Filer
# These imports will be used for this project.
from colorama import Fore, Style
from colorama import init
import random
import string
import time
import sys
import os

# Initilaze Filer.
os.system('title Filer')
init(autoreset = True)

# Global variables.
Task = ""
Chars = []
Output = []

# Create Log Functions.
class LOG:
	def LOG(message): print(message)
	def ERROR_LOG(message): print(Fore.RED + Style.BRIGHT + f"ERROR: {message}")
	def WARN_LOG(message): print(Fore.YELLOW + Style.BRIGHT + f"WARNING: {message}")

# This funciton will Exit the program.
def Exit():
	os.system("echo|set /p=Done.")
	os.system("pause>nul")
	sys.exit() # Exiting the program successfully.

# Encrypt the file.
def EncryptFile(FilePath):
	Output_Filename = f"Encrypt-{str(time.time())}-{FilePath}"
	with open(FilePath, "r") as File:
		for Line in File:
			Line = Line.replace("\n", "")
			for Characters in Line:
				FindIndex = Chars[0].index(Characters)
				Output.append(Chars[1][FindIndex])

			Output.append("\n")

	with open(Output_Filename, "w") as File:
		for i in Output: File.writelines(i)

	LOG.LOG(f"INFO: Your Encrypted Filename is: {Output_Filename}")
	LOG.LOG(Fore.GREEN + "Encrypted!\n")

# Decrypt the file.
def DecryptFile(FilePath):
	Output_Filename = f"Decrypt-{str(time.time())}-{FilePath}"
	with open(FilePath, "r") as File:
		for Line in File:
			Line = Line.replace("\n", "")
			for Characters in Line:
				FindIndex = Chars[1].index(Characters)
				Output.append(Chars[0][FindIndex])

			Output.append("\n")

	with open(Output_Filename, "w") as File:
		for i in Output: File.writelines(i)

	LOG.LOG(f"INFO: Your Decrypted Filename is: {Output_Filename}")
	LOG.LOG(Fore.GREEN + "Decrypted!\n")

# This will Generate a Strong Password for the User!
def Filer(FilePath, KeySeed):
	random.seed(KeySeed) # Choose a Seed.

	# Split the List of these String Operations, and Join them to Chars List 2 Times.
	for i in range(2):
		Chars.append(list(string.ascii_letters + string.digits + string.punctuation))
	Chars[0].append(" ")
	Chars[1].append(" ")

	# Shuffle Chars[1] List.
	random.shuffle(Chars[1])

	if Task == "Encrypt":
		LOG.WARN_LOG("Encrypting your File.")
		EncryptFile(FilePath)

	elif Task == "Decrypt":
		LOG.WARN_LOG("Decrypting your File.")
		DecryptFile(FilePath)

# Code Logic here.
LOG.WARN_LOG("Initialized Filer!")

# Code what to do here.
LOG.LOG("Note.\n> Type \"encrypt\" (without quotes) to Encrypt a File.")
LOG.LOG("> Type \"decrypt\" (without quotes) to Decrypt a File.")
WhatToDo = input("What task do you want to perform> ")
if WhatToDo.lower() == "encrypt": Task = "Encrypt"
elif WhatToDo.lower() == "decrypt": Task = "Decrypt"
else:
	LOG.ERROR_LOG("Your given Command does not exist as an option.")
	LOG.ERROR_LOG("Please try again later.")
	Exit()

# Code file path here.
LOG.LOG("\nNote.\n> The File path should be proper.")
LOG.LOG("> The File must exist on your device.")
FilePath = input("Enter File Path> ")
if os.path.isfile(FilePath) == False: 
	LOG.ERROR_LOG("Your given File does not exist.")
	LOG.ERROR_LOG("Please try again later.")
	Exit()

# Code encryption key here.
LOG.LOG("\nNote.\n> Encryption Key must be a number.")
LOG.LOG("> To Decrypt an Encrypted File, You must Enter the same Key which was used while Encrypting.")
KeySeed = input("Enter your Encryption Key> ")
if KeySeed.isdigit():
	LOG.LOG("STATUS: Generating a File for You.\n")
	Filer(FilePath, int(KeySeed))

else:
	LOG.ERROR_LOG("Your given Encryption Key is not a number.")
	LOG.ERROR_LOG("Please try again later.")

Exit()
