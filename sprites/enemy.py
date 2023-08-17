import pygame
from pygame.sprite import Sprite
import random

import settings
from asset_loader import load_image

class Enemy(Sprite):                # 定義 Enemy 類別

    def speed_init():               # 定義初始化速度的函式
        Enemy.speed = 1             # 將移動速度設為 1

    def level_up():                 # 定義等級提升的函式
        Enemy.speed += 0.2          # 將移動速度增加 0.2

    def __init__(self):             # 定義建構函式
        super().__init__()          # 調用父類別的建構函式
        self.image = load_image("enemy.bmp")
                                    # 載入 enemy.bmp 檔案作為 image 屬性
        self.rect = self.image.get_rect()
                                    # 宣告 rect 屬性為 image 的屬性

        self.rect.x = random.randrange(settings.ENEMY_BOARD, settings.SCREEN_WIDTH - self.rect.width - settings.ENEMY_BOARD)
                                    # 將 rect 屬性的 x 設定為介於視窗大小之間的隨機數
        self.rect.y = self.rect.height
                                    # 將 rect 屬性的 y 設定為 height

    def update(self):               # 定義更新函式
        self.rect.y += settings.ENEMY_SPEED * Enemy.speed
                                    # 將 rect 屬性的 y 增加 <ENEMY_SPEED * speed 屬性>