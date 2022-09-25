import pygame
from tkinter import *
import os




class Util():

    @staticmethod
    def hexcolor(value, range, reverse=False):

        min = 0
        max = abs(range[1]-range[0])
        value -= range[0]

        if value <= int((min+max)/2):
            r = 255
            g = int(255*value/int((min+max)/2))
            b = 0
        else:
            r = int(255*(max-value)/int((min+max)/2))
            g = 255
            b = 0

        if reverse:
            r, g = g, r

        return "#%s%s%s" % tuple([hex(c)[2:].rjust(2, "0") for c in (r, g, b)])

    @staticmethod   
    def update(surface,lastX,lastY,dist,value):
        position = pygame.Vector2()
        position.xy = [(lastX - dist),  lastY]
        surface.blit(value, (position.x,position.y))

    
class Board(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((640, 480))
        self.image.fill((13,13,13))
        self.image.set_colorkey((13,13,13))
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("monospace", 18)

    def add(self, letter, pos):
        s = self.font.render(letter, 1, (255, 255, 0))
        self.image.blit(s, pos)

class Cursor(pygame.sprite.Sprite):
    def __init__(self, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill((0,255,0))
        self.text_height = 17
        self.text_width = 10
        self.rect = self.image.get_rect(topleft=(self.text_width, self.text_height))
        self.board = board
        self.text = ''
        self.cooldown = 0
        self.cooldowns = {'.': 12,
                        '[': 18,
                        ']': 18,
                        ' ': 5,
                        '\n': 30}

    def write(self, text):
        self.text = list(text)

    def update(self):
        if not self.cooldown and self.text:
            letter = self.text.pop(0)
            if letter == '\n':
                self.rect.move_ip((0, self.text_height))
                self.rect.x = self.text_width
            else:
                self.board.add(letter, self.rect.topleft)
                self.rect.move_ip((self.text_width, 0))
            self.cooldown = self.cooldowns.get(letter, 8)

        if self.cooldown:
            self.cooldown -= 1
