import pygame
from tkinter import *


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

        