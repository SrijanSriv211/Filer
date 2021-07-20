from colorama import Fore, Back, Style
from colorama import init
import sys, os
import json

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *

from GUI import GUI
import LOG

pygame.init()
init(autoreset = True)
os.system('title Filer')
LOG.FILER_LOG(Fore.GREEN + "Filer")
LOG.FILER_LOG(Fore.GREEN + "NOTE: Change \"Input_File\" in \"Options.json\"\n")
LOG.FILER_LOG("Filer is an Open-Source Project can be found on \"github.com/Light-Lens/Filer\"\n")

Loop = True
clock = pygame.time.Clock()
Logo = pygame.image.load("Logo.png")
Encryption_Pattern = [
"a", "b", "c", "d", "e",
"f", "g", "h", "i", "j",
"k", "l", "m", "n", "o",
"p", "q", "r", "s", "t",
"u", "v", "w", "x", "y",
"z", " ", ".", ",", "?",
"!", "@", "#", "$", "%",
"&", "*", "(", ")", "_",
"-", "+", "=", "{", "}",
"[", "]", ";", ":", "<",
">"
]

Decryption_Pattern = [
"!", "@", "#", "$", "^",
"&", "*", "(", ")", "_",
"-", "=", "+", "{", "}",
"[", "]", "<", ">", "/",
";", ":", "'", "|", "~",
"`", "%", "a", "b", "c",
"1", "3", "2", "5", "4",
"6", "7", "9", "8", "0",
"d", "e", "f", "g", "h",
"i", "j", "k", "l", "m",
"n"
]

Display = pygame.display.set_mode((400, 575), pygame.NOFRAME)
pygame.display.set_caption("Filer")
pygame.display.set_icon(Logo)

Title_BAR = GUI.Label(Display, (40, 40, 40), 0, 0, 400, 30)
Title_BAR_Text = GUI.Text(Display, "Filer", (255, 255, 255), (175, 5), 21)
Title_BAR_Logo = pygame.transform.scale(Logo, (30, 30))
Title_BAR_Quit_Text = GUI.Text(Display, "x", (255, 255, 255), (375, 3), 21)
Title_BAR_Quit_Button = GUI.Button(Display, (40, 40, 40), (255, 89, 89), (255, 59, 59), 360, 0, 40, 30)

In_Window_Title_BAR = GUI.Label(Display, (45, 45, 45), 0, 30, 400, 100)
In_Window_Title_BAR_Text = GUI.Text(Display, "Filer", (75, 75, 75), (145, 35), 70)
In_Window_Title_BAR_Text2 = GUI.Text(Display, "File Encrypter and Decrypter", (150, 150, 150), (55, 100), 25)

Encrypt_Text = GUI.Text(Display, "Encrypt", (255, 255, 255), (167, 257), 21)
Encrypt_Info = GUI.Text(Display, "> Encrypt your desired File.", (255, 255, 255), (125, 290), 15)
Encrypt_Button = GUI.Button(Display, (25, 25, 25), (20, 20, 20), (10, 10, 10), 150, 250, 100, 35)

Decrypt_Text = GUI.Text(Display, "Decrypt", (255, 255, 255), (167, 357), 21)
Decrypt_Info = GUI.Text(Display, "> Decrypt your desired File.", (255, 255, 255), (125, 390), 15)
Decrypt_Button = GUI.Button(Display, (25, 25, 25), (20, 20, 20), (10, 10, 10), 150, 350, 100, 35)

Info_Text = GUI.Text(Display, "NOTE: Change \"Input_File\" in \"Options.json\"", (255, 255, 90), (50, 550), 17)
def encrypt():
	LOG.FILER_LOG(Fore.GREEN + "Encrypting...")
	LOG.FILER_LOG("This may take some time.")
	with open("Options.json", "r") as File:
		Output = []
		Content = json.load(File)
		for Data in Content["Encrypt"]:
			if Data["Input_File"] == "": LOG.FILER_ERROR_LOG("No Input File in \"Options.json\" for Encryption.")
			else:
				with open(Data["Input_File"], "r") as Lines:
					for Line in Lines:
						Line = Line.replace("\n", "")
						Line = Line.lower()
						for Chars in Line:
							if Chars in Encryption_Pattern:
								Count = Encryption_Pattern.index(Chars)
								Output.append(Decryption_Pattern[Count])
						Output.append("\n")

				with open(Data["Output_File"] + Data["Input_File"], "w") as File:
					for Chars in Output:
						File.writelines(Chars)
					LOG.FILER_LOG("Your Encrypted Filename is: " + Data["Output_File"] + Data["Input_File"])
					LOG.FILER_LOG(Fore.GREEN + "Encrypted.\n")

def decrypt():
	LOG.FILER_LOG(Fore.GREEN + "Decrypting...")
	LOG.FILER_LOG("This may take some time.")
	with open("Options.json", "r") as File:
		Output = []
		Content = json.load(File)
		for Data in Content["Decrypt"]:
			if Data["Input_File"] == "": LOG.FILER_ERROR_LOG("No Input File in \"Options.json\" for Decryption.")
			else:
				with open(Data["Input_File"], "r") as Lines:
					for Line in Lines:
						Line = Line.replace("\n", "")
						Line = Line.lower()
						for Chars in Line:
							if Chars in Decryption_Pattern:
								Count = Decryption_Pattern.index(Chars)
								Output.append(Encryption_Pattern[Count])
						Output.append("\n")

				with open(Data["Output_File"] + Data["Input_File"], "w") as File:
					for Chars in Output:
						File.writelines(Chars)
					LOG.FILER_LOG("Your Decrypted Filename is: " + Data["Output_File"] + Data["Input_File"])
					LOG.FILER_LOG(Fore.GREEN + "Decrypted.\n")

def main():
	while Loop:
		clock.tick(120)
		Display.fill((25, 25, 25))
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		Title_BAR.draw()
		Title_BAR_Text.draw()
		QUIT = Title_BAR_Quit_Button.draw()
		Title_BAR_Quit_Text.draw()
		Display.blit(Title_BAR_Logo, (0, 0))
		if QUIT: sys.exit()
		else: pass

		In_Window_Title_BAR.draw()
		In_Window_Title_BAR_Text.draw()
		In_Window_Title_BAR_Text2.draw()

		encrypt_pressed = Encrypt_Button.draw()
		Encrypt_Text.draw()
		Encrypt_Info.draw()
		if encrypt_pressed: encrypt()

		decrypt_pressed = Decrypt_Button.draw()
		Decrypt_Text.draw()
		Decrypt_Info.draw()
		if decrypt_pressed: decrypt()

		Info_Text.draw()

		pygame.display.update()
	pygame.quit()

if __name__ == '__main__':
	main()
