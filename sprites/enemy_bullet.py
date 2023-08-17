import math
import pygame                       # 引用 pygame 模組
from pygame.sprite import Sprite    # 從 pygame.sprite 中引用 Sprite 類別
import settings

class EnemyBullet(Sprite):               # 定義 Bullet 類別

    def __init__(self, enemy_rect, v = (0, settings.ENEMY_BULLET_SPEED)):  # 定義建構函式
        super().__init__()          # 調用父類別的建構函式
        self.v = v
        self.age = 80
        r = settings.BULLET_RADIUS
        self.image = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
                                                # 宣告 image 屬性為 Surface
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, (255, 0, 0, 255), (r, r), r)
        self.rect = self.image.get_rect()       # 宣告 rect 屬性為 image 的 Rect
        self.rect.midtop = enemy_rect.midbottom  # 將 rect 的 midbottom 設為 ship_rect 的 midtop
        
    def update(self):                           # 定義更新函式
        self.age -= 1
        if self.age == 0:
            self.kill()
        self.rect.move_ip(self.v)