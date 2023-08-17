import sys
import math
import pygame
from pygame.locals import *

import settings
from scene import Scene
from scene_manager import SceneEnum, SceneManager
from GUI import *

from sprites.ship import SpaceShip
from sprites.enemy import Enemy
from sprites.enemy_bullet_tracking import EnemyBulletTracking
Enemy.speed_init()

BLACK = (0, 0, 0)

class GameSceneCanvas(Canvas):
    def __init__(self):
        self.score_board = Label("score:", (790, 10), settings.GUI_TOPRIGHT)
        self.level_board = Label("level: ", (790, 70), settings.GUI_TOPRIGHT)
        self.lives_bar = Label("lives:", (790, 130), settings.GUI_TOPRIGHT)

    def update(self, mouse_action, score, level, lives):
        if pygame.key.get_pressed()[settings.QUIT]: # 如果按下 QUIT 鍵
            SceneManager.push_scene(SceneEnum.PAUSE)         # 就將場景切換為 pause_scene
        self.score_board.msg = "score: " + str(score)   # 將 _score_board 的 msg 設為「score: <分數>」
        self.level_board.msg = "level: " + str(level)   # 將 _level_board 的 msg 設為「level: <等級>」
        self.lives_bar.msg = "lives: " + str(lives)     # 將 _lives_bar 的 msg 設為「lives: <剩餘生命>」
        self.score_board._prep_label()  # 建立 _score_board 的文字渲染
        self.level_board._prep_label()  # 建立 _level_board 的文字渲染
        self.lives_bar._prep_label()    # 建立 _lives_bar 的文字渲染

    def blit_on(self, screen):    # 定義 game_scene 的 Canvas 的繪製函式
        _score_board = self.score_board             # 宣告 _score_board 變數為 score_board 屬性
        _level_board = self.level_board             # 宣告 _level_board 變數為 level_board 屬性
        _lives_bar = self.lives_bar                 # 宣告 _lives_bar 變數為 lives_bat 屬性
        screen.blit(_score_board.image, _score_board.rect)  # 繪製 _score_board
        screen.blit(_level_board.image, _level_board.rect)  # 繪製 _level_board
        screen.blit(_lives_bar.image, _lives_bar.rect)      # 繪製 _lives__bar

def circle_collide_predicate(r):
    return lambda x, y: math.hypot(x.rect.centerx - y.rect.centerx, x.rect.centery - y.rect.centery) < r

class GameScene(Scene):
    def __init__(self):
        super().__init__("Game")
        self.canvas = GameSceneCanvas()
        self.score = 0 # 宣告 score 變數，用以儲存玩家得分
        self.lives = 3 # 宣告 lives 變數，用以儲存玩家剩餘生命
        self.level = 1 # 宣告 level 變數，用以儲存玩家當前等級

        self.ship = SpaceShip()
        self.ship.rect.center = (400, 500)
        self.enemies = pygame.sprite.Group()
        self.spawn_time = settings.ENEMY_SPAWN_TIME
        self.enemy_bullets = pygame.sprite.Group()

    def init(self):    # 定義用於 game_scene 初始化的函式
        is_clear = True
        if is_clear:                        # 如果要進行初始化
            self.lives = 3                  # 將剩餘生命設定為 3
            self.level = 1                  # 將等級設定為 1
            self.score = 0                  # 將分數設定為 0
        if self.ship:                       # 如果自己擁有 ship 物件
            del self.ship                   # 則刪除該物件
        self.ship = SpaceShip()             # 宣告新的 ship 物件
        self.ship.rect.center = (400, 500)  # 將 ship 物件的 rect 物件的 center 設定為 (400, 500)
        self.enemies.empty()                # 清空當前敵人
        self.enemy_bullets.empty()

    def pause(self) -> None:
        pass

    def resume(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def update(self, mouse_action):  # 定義 game_scene 的更新函式
        self.create_enemies()                   # 試圖產生一個敵人
        self.ship.update()                      # 調用 ship 屬性的更新函式
        self.enemies.update()                   # 調用 enemies 的更新函式
        self.enemy_bullets.update()
        for enemy in self.enemies:              # 對於所有在 enemies 中的 enemy
            if enemy.rect.top > settings.SCREEN_HEIGHT:
                                                # 如果 enemy 的位置低於視窗底部
                self.enemies.remove(enemy)      # 就把 enemy 刪除
        collisions = pygame.sprite.groupcollide(self.ship.bullets, self.enemies, True, True)
                                                # 宣告 collision 為儲存 bullets 和 enemies 碰撞結果的變數
        if collisions:                          # 如果有碰撞發生
            self.score += settings.ENEMY_SCORE  # 分數增加
            self.canvas.score_board._prep_label()
                                                # 更新一次 score_board 的文字
        collided_enemy = pygame.sprite.spritecollideany(self.ship, self.enemies, circle_collide_predicate(settings.SHIP_COLLIDE_RADIUS + settings.ENEMY_COLLIDE_RADIUS))
        if collided_enemy != None:
            collided_enemy.kill()
            self.on_hit()
        collided_bullet = pygame.sprite.spritecollideany(self.ship, self.enemy_bullets, circle_collide_predicate(settings.SHIP_COLLIDE_RADIUS + settings.BULLET_RADIUS))
        if collided_bullet != None:
            collided_bullet.kill()
            self.on_hit()
        grazed_bullet = pygame.sprite.spritecollideany(self.ship, self.enemy_bullets, circle_collide_predicate(settings.SHIP_GRAZE_RADIUS + settings.BULLET_RADIUS))
        if grazed_bullet != None:
            pass
        if self.score >= self.level * settings.LEVEL_GAP:
                                                # 如果分數足以提升等級
            self.level += 1                     # 等級加 1
            Enemy.level_up()                    # 調用 Enemy 類別的 level_up 函式
        self.canvas.update(mouse_action, self.score, self.level, self.lives)
                                                # 調用 canvas 屬性的更新函式

    def blit_on(self, screen):       # 定義 game_scene 的繪製函式
        screen.fill(settings.BACKGROUND_COLOR)  # 清空畫面中所有內容
        screen.blit(self.ship.image, self.ship.rect)
        if pygame.key.get_pressed()[settings.SLOW]:
            pygame.draw.circle(screen, BLACK, self.ship.rect.center, settings.SHIP_COLLIDE_RADIUS, settings.SHIP_COLLISION_INDICATOR_WIDTH)
            pygame.draw.circle(screen, BLACK, self.ship.rect.center, settings.SHIP_GRAZE_RADIUS, settings.SHIP_COLLISION_INDICATOR_WIDTH)
        self.ship.bullets.draw(screen)          # 繪製 bullets
        self.enemies.draw(screen)               # 繪製 enemies
        self.enemy_bullets.draw(screen)
        self.canvas.blit_on(screen)# 調用 canvas 屬性的繪製函式

    def create_enemies(self):         # 定義用於產生敵人的函式
        if self.spawn_time > 0:     # 如果冷卻時間大於 0
            self.spawn_time -= 1    # 將冷卻時間減 1
        else:                       # 否則
            enemy = Enemy()         # 宣告 enemy 變數為 Enemy 物件
            self.enemies.add(enemy) # 將 enemy 加入 enemies 中
            self.spawn_time = settings.ENEMY_SPAWN_TIME
                                    # 設定產生敵人的冷卻時間
            for e in self.enemies:
                self.enemy_bullets.add(EnemyBulletTracking(e.rect, self.ship.rect.center))

    def on_hit(self):               # 定義當自機被擊中時的函式
        self.lives -= 1             # 剩餘生命減 1 
        if self.lives <= 0:         # 如果剩餘生命小於等於 0
            print("Game Over")      # 列印出 Game Over 字樣
            SceneManager.push_scene(SceneEnum.GAMEOVER)
