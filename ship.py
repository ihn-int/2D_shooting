import pygame                   # 引用 pygame 模組
from setting import Settings    # 從 setting 模組中引用 Settings 類別
from bullet import Bullet       # 從 bullet 模組中引用 Bullet 類別

class SpaceShip:                # 定義 Spaceship 類別

    def __init__(self, pos = (400, 500)):           # 定義建構函式
        self.image = pygame.image.load("spaceship.bmp")     # 載入 spaceship.bmp 作為 image 屬性
        self.rect = self.image.get_rect()                   # 宣告 rect 屬性為 image 的 rect 屬性
        self.rect.center = pos                  # 將 rect 的 center 設定為 pos，預設為 (400, 500)
        self.bullets = pygame.sprite.Group()    # 宣告 bullets 為 Group 物件，儲存發射的子彈
        self.speed = Settings.SHIP_SPEED        # 宣告 speed 屬性為 SHIP_SPEED，代表自機移動速度
        self.firecount = 0                      # 宣告 firecount 變數，代表開火冷卻時間
        self.life = Settings.SHIP_LIVES         # 宣告 life 屬性
    

    def update(self):                           # 定義更新函式
        if self.firecount > 0:                  # 如果開火冷卻大於 0 
            self.firecount -= 1                 # 就將冷卻時間減 1
        self.bullets.update()                   # 調用 Bullet 類別的更新函式
        for bullet in self.bullets:             # 對所有 bullets 中的 bullet
            if bullet.rect.bottom < 0:          # 如果 bullet 的底部碰到視窗上緣
                self.bullets.remove(bullet)     # 就移除掉 bullet


        self.keypress = pygame.key.get_pressed()    # 宣告 keypress 屬性，儲存鍵盤狀態
        if self.keypress[Settings.SLOW]:            # 如果慢速移動鍵被按著
            self.speed = Settings.SHIP_SLOW_SPEED   # 就將移動速度調慢
        else:                                       # 否則
            self.speed = Settings.SHIP_SPEED        # 移動速度調快

        if self.keypress[Settings.RIGHT] and self.rect.right < Settings.SCREEN_WIDTH - Settings.SCREEN_BOARD:                               # 如果向右鍵被按著，且沒有移動到邊界
            self.rect.x += self.speed               # 就將 x 座標增加
            
        if self.keypress[Settings.LEFT] and self.rect.left > Settings.SCREEN_BOARD:
                                                    # 如果向左鍵被按著，且沒有移動到邊界
            self.rect.x -= self.speed               # 就將 x 座標減少

        if self.keypress[Settings.UP] and self.rect.top > 0:
                                                    # 如果向上鍵被按著，且沒有移動到邊界
            self.rect.y -= self.speed               # 就將 y 座標減少

        if self.keypress[Settings.DOWN] and self.rect.bottom < Settings.SCREEN_HEIGHT - Settings.SCREEN_BOARD:                      # 如果向下鍵被按著，且沒有移動到邊界
            self.rect.y += self.speed               # 就將 y 座標增加

        if self.keypress[Settings.FIRE] and self.firecount == 0:
                                                    # 如果攻擊鍵被按著，且開火冷卻為 0
            bullet = Bullet(self.rect)              # 宣告 bullet 變數為 Bullet 物件
            self.bullets.add(bullet)                # 將 bullet 加入到 bullets 當中
            self.firecount = Settings.SHIP_COOLDOWN # 重置開火冷卻