import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("data/gfx/sc.png")
        self.image = pygame.image.load("data/gfx/sc.png")
        self.rect = self.sprite.get_rect()
        self.img_offset = (-50,-40)
        self.highscore = "0"

        with open("data/scores.txt", "r",encoding="utf-8") as f:
            for num in f:
                if num.strip():     
                    self.highscore =  str(num)
        f.close()

    def update(self):
        """move the fist based on the mouse position"""
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.img_offset)

    def collision(self,target):
            hitbox = self.rect.inflate(0,0)
            return hitbox.colliderect(target.rect)  

