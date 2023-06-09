import pygame
from pygame.sprite import Sprite
from setting import Settings

class Bullet(Sprite):
    def __init__(self, ship):
        super().__init__()
        self.screen = ship.screen
        
        self.rect = pygame.Rect(0, 0, Settings.BULLET_WIDTH, Settings.BULLET_HEIGHT)
        self.rect.midbottom = ship.rect.midtop
        
    def update(self):
        self.rect.y -= Settings.BULLET_SPEED

    def BlitMe(self):
        pygame.draw.rect(self.screen, Settings.BULLET_COLOR, self.rect)
