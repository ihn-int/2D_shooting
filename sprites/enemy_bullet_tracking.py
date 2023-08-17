import math
import pygame                       # 引用 pygame 模組
from pygame.sprite import Sprite    # 從 pygame.sprite 中引用 Sprite 類別
import settings

class EnemyBulletTracking(Sprite):               # 定義 Bullet 類別

    def __init__(self, enemy_rect, target = None):  # 定義建構函式
        super().__init__()          # 調用父類別的建構函式
        self.v = (0, settings.ENEMY_BULLET_SPEED)
        self.target = target
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
        if self.target != None:
            pos = self.rect.center

            if math.hypot(self.target[1] - pos[1], self.target[0] - pos[0]) < 20:
                self.kill()

            pos_angle = math.atan2(self.target[1] - pos[1], self.target[0] - pos[0])
            v_angle = math.atan2(self.v[1], self.v[0])
            angle = pos_angle - v_angle
            if angle > math.pi:
                angle -= math.pi
            if angle < -math.pi:
                angle += math.pi
            angle /= 20
            angle += v_angle
            v = settings.ENEMY_BULLET_SPEED
            self.v = (v * math.cos(angle), v * math.sin(angle))
        self.rect.move_ip(self.v)