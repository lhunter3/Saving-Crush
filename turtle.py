import pygame

class Turtle():
    def __init__(self):
        self.sprite = pygame.image.load('data/gfx/turtle.png')
        self.position = pygame.Vector2()
        self.position.xy = [0,0]
        self.outOfBounds = False
        self.turtleLen = self.sprite.get_width()

    def update(self):

        dist = 1 # distance moved in 1 frame, try changing it to 5
        self.position.xy = [(self.position.x - dist),  self.position.y]

        if self.position.x < 0 - self.turtleLen:
            self.outOfBounds = True

        return self.outOfBounds
