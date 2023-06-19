import pygame
from pygame.sprite import Sprite
from setting import Settings
import random

class Enemy(Sprite):

    def speed_init():
        Enemy.speed = 1

    def level_up():
        Enemy.speed += 0.2

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(Settings.ENEMY_BOARD, Settings.SCREEN_WIDTH - self.rect.width - Settings.ENEMY_BOARD)
        self.rect.y = self.rect.height

    def update(self):
        self.rect.y += Settings.ENEMY_SPEED * Enemy.speed