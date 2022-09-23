import pygame

class Turtle():
    def __init__(self,path):
        self.sprite = pygame.image.load(path)
        self.rect = self.sprite.get_rect()
        self.position = pygame.Vector2()
        self.position.xy = [0,0]
        self.outOfBounds = False
        self.turtleLen = self.sprite.get_width()

    def update(self,dist):

        # distance moved in 1 frame, try changing it to 5
        self.position.xy = [(self.position.x - dist),  self.position.y]
        
        self.rect = pygame.Rect(self.position.x,self.position.y,self.sprite.get_height(),self.sprite.get_width())
        if self.position.x < 0 - self.turtleLen:
            self.outOfBounds = True

        return self.outOfBounds



