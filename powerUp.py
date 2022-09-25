import pygame

class PowerUp():
    def __init__(self,path):
        self.sprite = pygame.image.load(path)
        self.rect = self.sprite.get_rect()
        self.position = pygame.Vector2()
        self.position.xy = (0,0) 
        self.price = 5
        self.level = 0
        
    def update(self):
        self.rect.topleft = self.position.xy


