import pygame
from pygame.sprite import Sprite
from setting import Settings
import random

class Enemy(Sprite):

    def SpeedInit():
        Enemy.speed = 1

    def LevelUp():
        Enemy.speed += 0.2

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        self.image = pygame.image.load("enemy.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(Settings.ENEMY_BOARD, self.screen.get_rect().width - self.rect.width - Settings.ENEMY_BOARD)
        self.rect.y = self.rect.height


    def update(self):
        self.rect.y += Settings.ENEMY_SPEED * Enemy.speed