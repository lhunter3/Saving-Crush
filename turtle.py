import pygame

class Turtle():
    def __init__(self):
        self.sprite = pygame.image.load('data/gfx/turtle.png')
        self.position = pygame.Vector2()
        self.position.xy