import pygame
from pygame.sprite import Sprite
from setting import Settings

class Bullet(Sprite):
    def __init__(self, ship_rect):
        super().__init__()
        self.image = pygame.Surface((Settings.BULLET_WIDTH, Settings.BULLET_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.midbottom = ship_rect.midtop
        
    def update(self):
        self.rect.y -= Settings.BULLET_SPEED