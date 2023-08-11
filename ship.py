import pygame                   # 引用 pygame 模組
from setting import Settings    # 從 setting 模組中引用 Settings 類別
from bullet import Bullet       # 從 bullet 模組中引用 Bullet 類別

class SpaceShip:                # 定義 Spaceship 類別

    def __init__(self, pos = (400, 500)) -> None:           # 定義建構函式
        self.image = pygame.image.load("spaceship.bmp")     # 載入 spaceship.bmp 作為 image 屬性
        self.rect = self.image.get_rect()                   # 宣告 rect 屬性為 image 的 rect 屬性
        self.rect.center = pos                  # 將 rect 的 center 設定為 pos，預設為 (400, 500)
        self.bullets = pygame.sprite.Group()    # 宣告 bullets 為 Group 物件，儲存發射的子彈
        self.speed = Settings.SHIP_SPEED        # 宣告 speed 屬性為 SHIP_SPEED，代表自機移動速度
        self.firecount = 0                      # 宣告 firecount 變數，代表開火冷卻時間
        self.life = Settings.SHIP_LIVES         # 宣告 life 屬性
    

    def update(self):
        if self.firecount > 0:
            self.firecount -= 1
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


        self.keypress = pygame.key.get_pressed()
        if self.keypress[Settings.SLOW]:
            self.speed = Settings.SHIP_SLOW_SPEED
        else:
            self.speed = Settings.SHIP_SPEED

        if self.keypress[Settings.RIGHT] and self.rect.right < Settings.SCREEN_WIDTH - Settings.SCREEN_BOARD:
            self.rect.x += self.speed
            
        if self.keypress[Settings.LEFT] and self.rect.left > Settings.SCREEN_BOARD:
            self.rect.x -= self.speed

        if self.keypress[Settings.UP] and self.rect.top > 0:
            self.rect.y -= self.speed

        if self.keypress[Settings.DOWN] and self.rect.bottom < Settings.SCREEN_HEIGHT - Settings.SCREEN_BOARD:
            self.rect.y += self.speed

        if self.keypress[Settings.FIRE] and self.firecount == 0:
            bullet = Bullet(self.rect)
            self.bullets.add(bullet)
            self.firecount = Settings.SHIP_COOLDOWN