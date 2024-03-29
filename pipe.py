import pygame

pygame.init()

class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, isTop = False):
        super().__init__()
        self.image=pygame.image.load('pipe.png')
        self.image = pygame.transform.smoothscale(self.image, (100,400))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(-5,0)
        if isTop:
            self.image = pygame.transform.rotate(self.image, 180)

    def update(self):
        self.rect.move_ip(self.speed)

