# This import blocks pygame from printing it's startup text.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *

# All engine featues
class GUI:
	class Label:
		def __init__(self, Graphics, Colors, Posx, Posy, Sizex, Sizey):
			self.Posx = Posx
			self.Posy = Posy
			self.Sizex = Sizex
			self.Sizey = Sizey
			self.Colors = Colors
			self.Graphics = Graphics

		def draw(self):
			pygame.draw.rect(self.Graphics, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))

	class Button:
		def __init__(self, Graphics, Colors, NewColor, Pressed, Posx, Posy, Sizex, Sizey):
			self.Posx = Posx
			self.Posy = Posy
			self.Sizex = Sizex
			self.Sizey = Sizey
			self.Colors = Colors
			self.Pressed = Pressed
			self.NewColor = NewColor
			self.Graphics = Graphics

		def draw(self):
			self.Hover_On_Rect = pygame.Rect(self.Posx, self.Posy, self.Sizex, self.Sizey)
			self.Mouse_Pos = pygame.mouse.get_pos()
			self.Hover_On = self.Hover_On_Rect.collidepoint(self.Mouse_Pos)

			pygame.draw.rect(self.Graphics, self.Colors, self.Hover_On_Rect)
			if self.Hover_On:
				pygame.draw.rect(self.Graphics, self.NewColor, self.Hover_On_Rect)
				if pygame.mouse.get_pressed()[0]:
					pygame.draw.rect(self.Graphics, self.Pressed, self.Hover_On_Rect)
					pygame.time.delay(100)
					return 1

				else: return 0
			else: pygame.draw.rect(self.Graphics, self.Colors, self.Hover_On_Rect)

	class Text:
		def __init__(self, Graphics, Text, Colors, Font_Pos, Font_size):
			self.Text = Text
			self.Colors = Colors
			self.Graphics = Graphics
			self.Font_Pos = Font_Pos
			self.Font_size = Font_size

		def draw(self):
			self.font = pygame.font.SysFont("calibri", self.Font_size)
			self.text = self.font.render(self.Text, True, self.Colors)
			self.Graphics.blit(self.text, self.Font_Pos)
