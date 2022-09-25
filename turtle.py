import pygame

class Turtle():
    def __init__(self,path):
        self.sprite = pygame.image.load(path)
        self.rect = self.sprite.get_rect()
        self.position = pygame.Vector2()
        self.position.xy = [0,0]
        self.img_offset = (0,0)

    def update(self,dist):

        self.position.xy = [(self.position.x - dist),  self.position.y]
        self.rect.topleft = self.position.xy
        self.rect.move_ip(self.img_offset)
        return self.position.x < 0 - self.sprite.get_width()



