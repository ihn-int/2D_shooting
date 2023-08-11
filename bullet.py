import pygame                       # 引用 pygame 模組
from pygame.sprite import Sprite    # 從 pygame.sprite 中引用 Sprite 類別
from setting import Settings        # 從 setting 模組中引用 Settings 類別

class Bullet(Sprite):               # 定義 Bullet 類別

    def __init__(self, ship_rect):  # 定義建構函式
        super().__init__()          # 調用父類別的建構函式
        self.image = pygame.Surface((Settings.BULLET_WIDTH, Settings.BULLET_HEIGHT))
                                                # 宣告 image 屬性為 Surface
        self.rect = self.image.get_rect()       # 宣告 rect 屬性為 image 的 Rect
        self.rect.midbottom = ship_rect.midtop  # 將 rect 的 midbottom 設為 ship_rect 的 midtop
        
    def update(self):                           # 定義更新函式
        self.rect.y -= Settings.BULLET_SPEED    # 將 rect 屬性的 y 減掉移動速度，代表向前移動