import math
import time
import pygame
from pygame.locals import *


#define global variable
clicked = False
white = (255, 255, 255)

class Button():
		
	#colours for button and text
	
	button_col = (30, 30, 30)
	hover_col = (106, 106, 106)
	click_col = (144, 144, 144)
	text_col = (255, 255, 255)
	width = 180
	height = 70

	def __init__(self, x, y, text,font):
		self.x = x
		self.y = y
		self.text = text
		self.font = font

	def draw(self, surface, sound):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y + math.sin(time.time()*5)*2.5 - 25, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(surface, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(surface, self.hover_col, button_rect)
		else:
			pygame.draw.rect(surface, self.button_col, button_rect)
		
		
		#add text to button
		text_img = self.font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		text_hi = text_img.get_height()
		surface.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + math.sin(time.time()*5)*2.5 - 25 + int(self.height/2 - int(text_hi/2))))
		return action