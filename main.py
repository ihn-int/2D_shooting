#==========================================================
# 初始化 Initialize

import pygame                   # 引用 pygame 模組
import sys                      # 引用 sys 模組（用以結束程式）
import settings
from scene import Scene         # 從 scene 模組引用 Scene 類別
from GUI import *               # 從 GUI 模組引用 所有 類別
from ship import SpaceShip      # 從 ship 模組引用 Spaceship 類別
from enemy import Enemy         # 從 enemy 模組引用 Enemy 類別
from enemy_bullet_tracking import EnemyBulletTracking
pygame.init()                   # pygame 初始化
Enemy.speed_init()              # Enemy 初始化

clock = pygame.time.Clock()     # 宣告 clock 變數為 Clock 物件
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
                                # 建立視窗

#==========================================================
#==========================================================
# 起始場景( start scene )

start_scene = Scene("Start")    # 宣告 start_scene 變數為 Scene 物件，代表起始場景
start_scene.canvas = Canvas()   # 宣告 start_scene 中的 canvas 屬性為 Canvas 物件

start_scene.canvas.play_button = Button("Play", (200, 50), (400, 250), settings.GUI_CENTER)
                                # 宣告 Canvas 物件中的 play_button 按鈕，用以開始遊戲
start_scene.canvas.quit_button = Button("Quit", (200, 50), (400, 350), settings.GUI_CENTER)
                                # 宣告 Canvas 物件中的 quit_button 按鈕，用以結束遊戲

def start_scene_canvas_update(canvas, mouse_action):    # 定義 start_scene 的 Canvas 的更新函式
    if canvas.play_button.is_click(mouse_action):       # 如果 play_button 被按下
        Scene.change_scene(game_scene)                  # 就切換到 game_scene
        game_scene.init(game_scene, True)               # 並且對 game_scene 進行初始化
    elif canvas.quit_button.is_click(mouse_action):     # 否則如果 quit_button 被按下
        print("QUIT")                                   # 列印出 QUIT 文字
        pygame.quit()                                   # 結束 pygame
        sys.exit(0)                                     # 結束程式

def start_scene_canvas_blit_on(canvas, screen):         # 定義 start_scene 的 Canvas 的繪製函式
    screen.blit(canvas.play_button.image, canvas.play_button.rect)
                                                        # 繪製 play_button 按鈕
    screen.blit(canvas.quit_button.image, canvas.quit_button.rect)
                                                        # 繪製 quit_button 按鈕

def start_scene_update(self, mouse_action):             # 定義 start_scene 的更新函式
    self.canvas.update(self.canvas, mouse_action)       # 調用 start_scene 的 Canvas 的更新函式

def start_scene_blit_on(self, screen):                  # 定義 start_scene 的繪製函式 
    screen.fill(settings.BACKGROUND_COLOR)              # 清空畫面中所有內容
    self.canvas.blit_on(self.canvas, screen)            # 調用 start_scene 的 Canvas 的繪製函式

start_scene.canvas.update = start_scene_canvas_update   # 將 start_scene 與其 canvas 的方法賦為
start_scene.canvas.blit_on = start_scene_canvas_blit_on # 前面定義的函式
start_scene.update = start_scene_update                 # 
start_scene.blit_on = start_scene_blit_on               # 

#==========================================================
#==========================================================
# 遊戲場景（game scene）

game_scene = Scene("Game")      # 宣告 game_scene 變數為 Scene 物件，代表遊戲場景
game_scene.canvas = Canvas()    # 宣告 game_scene 中的 canvas 屬性為 Canvas 物件
game_scene.canvas.score_board = Label("score:", (790, 10), settings.GUI_TOPRIGHT)
                                # 宣告 Canvas 中的 score_board 標籤，用以顯示分數
game_scene.canvas.level_board = Label("level: ", (790, 70), settings.GUI_TOPRIGHT)
                                # 宣告 Canvas 中的 level_board 標籤，用以顯示等級
game_scene.canvas.lives_bar = Label("lives:", (790, 130), settings.GUI_TOPRIGHT)
                                # 宣告 Canvas 中的 lives_bar 標籤，用以顯示剩餘生命
game_scene.score = 0            # 宣告 score 變數，用以儲存玩家得分
game_scene.lives = 3            # 宣告 lives 變數，用以儲存玩家剩餘生命
game_scene.level = 1            # 宣告 level 變數，用以儲存玩家當前等級
game_scene.ship = SpaceShip()   # 宣告 ship 變數為 Spaceship 物件，用以儲存玩家操控的自機
game_scene.ship.rect.center = (400, 500)
                                # 宣告 ship 物件的 rect 屬性的 center 為 (400, 500)
game_scene.enemies = pygame.sprite.Group()
                                # 宣告 enemies 為 Group 物件，用以儲存敵人
game_scene.spawn_time = settings.ENEMY_SPAWN_TIME
                                # 宣告 spawn_time 變數，用以產生敵人的時間間隔
game_scene.enemy_bullets = pygame.sprite.Group()

def game_scene_init(self, is_clear):    # 定義用於 game_scene 初始化的函式
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

def create_enemy(self):         # 定義用於產生敵人的函式
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
        Scene.change_scene(gameover_scene)
                                # 場景切換到 gameover_scene
    self.init(self, False)      # 進行一次場景的初始化，但不重設分數等等數據

def game_scene_canvas_update(self, mouse_action, score, level, lives):
                                                # 定義 game_scene 的 Canvas 的更新函式
    if pygame.key.get_pressed()[settings.QUIT]: # 如果按下 QUIT 鍵
        Scene.change_scene(pause_scene)         # 就將場景切換為 pause_scene
    _score_board = self.score_board             # 宣告 _score_board 變數為 score_board 屬性
    _level_board = self.level_board             # 宣告 _level_board 變數為 level_board 屬性
    _lives_bar = self.lives_bar                 # 宣告 _lives_bar 變數為 lives_bat 屬性
    _score_board.msg = "score: " + str(score)   # 將 _score_board 的 msg 設為「score: <分數>」
    _level_board.msg = "level: " + str(level)   # 將 _level_board 的 msg 設為「level: <等級>」
    _lives_bar.msg = "lives: " + str(lives)     # 將 _lives_bar 的 msg 設為「lives: <剩餘生命>」
    _score_board._prep_label()  # 建立 _score_board 的文字渲染
    _level_board._prep_label()  # 建立 _level_board 的文字渲染
    _lives_bar._prep_label()    # 建立 _lives_bar 的文字渲染
    

def game_scene_canvas_blit_on(self, screen):    # 定義 game_scene 的 Canvas 的繪製函式
    _score_board = self.score_board             # 宣告 _score_board 變數為 score_board 屬性
    _level_board = self.level_board             # 宣告 _level_board 變數為 level_board 屬性
    _lives_bar = self.lives_bar                 # 宣告 _lives_bar 變數為 lives_bat 屬性
    screen.blit(_score_board.image, _score_board.rect)  # 繪製 _score_board
    screen.blit(_level_board.image, _level_board.rect)  # 繪製 _level_board
    screen.blit(_lives_bar.image, _lives_bar.rect)      # 繪製 _lives__bar

def game_scene_update(self, mouse_action):  # 定義 game_scene 的更新函式
    self.create_enemies(self)               # 試圖產生一個敵人
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
    if pygame.sprite.spritecollideany(self.ship, self.enemies):
                                            # 如果 ship 碰到了 enemies 中的任一物件
        self.on_hit(self)                   # 調用自己的 on_hit 函式
    if pygame.sprite.spritecollideany(self.ship, self.enemy_bullets):
        self.on_hit(self)
    if self.score >= self.level * settings.LEVEL_GAP:
                                            # 如果分數足以提升等級
        self.level += 1                     # 等級加 1
        Enemy.level_up()                    # 調用 Enemy 類別的 level_up 函式
    self.canvas.update(self.canvas, mouse_action, self.score, self.level, self.lives)
                                            # 調用 canvas 屬性的更新函式

def game_scene_blit_on(self, screen):       # 定義 game_scene 的繪製函式
    screen.fill(settings.BACKGROUND_COLOR)  # 清空畫面中所有內容
    screen.blit(self.ship.image, self.ship.rect)
                                            # 繪製 ship 
    self.ship.bullets.draw(screen)          # 繪製 bullets
    self.enemies.draw(screen)               # 繪製 enemies
    self.enemy_bullets.draw(screen)
    self.canvas.blit_on(self.canvas, screen)# 調用 canvas 屬性的繪製函式

game_scene.canvas.update = game_scene_canvas_update     # 將 game_scene 與其 canvas 屬性的方法賦為
game_scene.canvas.blit_on = game_scene_canvas_blit_on   # 前面定義的函式
game_scene.update = game_scene_update                   # 
game_scene.blit_on = game_scene_blit_on
game_scene.create_enemies = create_enemy    # 將剩餘方法賦為對應的函式
game_scene.on_hit = on_hit                  # 
game_scene.init = game_scene_init           # 

#==========================================================
#==========================================================
# 暫停場景（pause_scene）

pause_scene = Scene("Pause")            # 宣告 pause_scene 變數為 Scene 物件，代表暫停場景
pause_scene.canvas = Canvas()           # 宣告 pause_scene 中的 canvas 屬性為 Canvas 物件
pause_scene.canvas.resume_button = Button("Resume", (200, 50), (400, 250), settings.GUI_CENTER)
                                        # 宣告 Canvas 物件中的 resume_button 按鈕
pause_scene.canvas.menu_button = Button("Menu", (200, 50), (400, 350), settings.GUI_CENTER)
                                        # 宣告 Canvas 物件中的 menu_button 按鈕
pause_scene.canvas.paused_label = Label("Paused", (400, 100), settings.GUI_CENTER)
                                        # 宣告 Canvas 物件中的 paused_label 標籤

def pause_scene_canvas_update(self, mouse_action):  # 定義 pause_scene 的 Canvas 的更新函式
    if self.resume_button.is_click(mouse_action):   # 如果 resume_button 被按下
        Scene.change_scene(game_scene)              # 場景切換為 game_scene
    if self.menu_button.is_click(mouse_action):     # 如果 menu_button 被按下
        Scene.change_scene(start_scene)             # 場景切換為 start_scene

def pause_scene_canvas_blit_on(self, screen):       # 定義 pause_scene 的 Canvas 的繪製函式
    screen.blit(self.resume_button.image, self.resume_button.rect)
                                                    # 繪製 resume_button
    screen.blit(self.menu_button.image, self.menu_button.rect)
                                                    # 繪製 menu_button
    screen.blit(self.paused_label.image, self.paused_label.rect)
                                                    # 繪製 paused_label

def pause_scene_update(self, mouse_action):         # 定義 pause_scene 的更新函式
    self.canvas.update(self.canvas, mouse_action)   # 調用 canvas 屬性的更新函式

def pause_scene_blit_on(self, screen):              # 定義 pause_scene 的繪製函式
    self.canvas.blit_on(self.canvas, screen)        # 調用 canvas 屬性的繪製函式

pause_scene.canvas.update = pause_scene_canvas_update   # 將 game_scene 與其 canvas 屬性的方法賦為
pause_scene.canvas.blit_on = pause_scene_canvas_blit_on # 前面定義的函式
pause_scene.update = pause_scene_update                 # 
pause_scene.blit_on = pause_scene_blit_on               # 

#==========================================================
#==========================================================
# 遊戲結束場景（game over scene）

gameover_scene = Scene("Game Over") # 宣告 gameover_scene 為 Scene 物件的變數，代表遊戲結束場景
gameover_scene.canvas = Canvas()    # 宣告 gameover_scene 的 canvas 為 Canvas 物件的變數
gameover_scene.canvas.retry_button = Button("Retry", (200, 50), (400, 250), settings.GUI_CENTER)
                                    # 宣告 canvas 屬性的 retry_button 按鈕
gameover_scene.canvas.menu_button = Button("Menu", (200, 50), (400, 350), settings.GUI_CENTER)
                                    # 宣告 canvas 屬性的 menu_button 按鈕
gameover_scene.canvas.gameover_label = Label("Game Over!!!", (400, 100), settings.GUI_CENTER)
                                    # 宣告 canvas 屬性的 gameover__label 標籤

def gameover_scene_canvas_update(self, mouse_action): # 定義 gameover_scene 的 Canvas 的更新函式
    if self.retry_button.is_click(mouse_action):      # 如果 retry_button 被按下
        game_scene.init(game_scene, True)             # 就將 game_scene 進行初始化
        Scene.change_scene(game_scene)                # 場景切換為 game_scene
    if self.menu_button.is_click(mouse_action):       # 如果 menu_button 被按下
        Scene.change_scene(start_scene)               # 場景切換為 start_scene

def gameover_scene_canvas_blit_on(self, screen):    # 定義 gameover_scene 的 Canvas 的繪製函式 
    screen.blit(self.retry_button.image, self.retry_button.rect)
                                                    # 繪製 retry_button 
    screen.blit(self.menu_button.image, self.menu_button.rect)
                                                    # 繪製 menu_button
    screen.blit(self.gameover_label.image, self.gameover_label.rect)
                                                    # 繪製 gameover_label

def gameover_scene_update(self, mouse_action):      # 定義 gameover_scene 的更新函式
    self.canvas.update(self.canvas, mouse_action)   # 調用 canvas 屬性的更新函式

def gameover_scene_blit_on(self, screen):           # 定義 gameover_scene 的繪製函式
    self.canvas.blit_on(self.canvas, screen)        # 調用 canvas 屬性的繪製函式

gameover_scene.canvas.update = gameover_scene_canvas_update     # 將 gameover_scene 與其 Canvas
gameover_scene.canvas.blit_on = gameover_scene_canvas_blit_on   # 的方法賦為前面定義的函式
gameover_scene.update = gameover_scene_update                   # 
gameover_scene.blit_on = gameover_scene_blit_on                 #

#==========================================================
#==========================================================
# scene running

Scene.change_scene(start_scene) # 將當下運作的場景設定為 start_scene

while True:
    clock.tick(settings.FPS)    # 將遊戲設定為 60 FPS
    _mouse_action = Scene.running_scene.check_event()
                                # 宣告 _mouse_action 變數為調用 running_scene 檢查事件函式的回傳值
    Scene.running_scene.update(Scene.running_scene, _mouse_action)
                                # 調用 running_scene 的更新函式
    Scene.running_scene.blit_on(Scene.running_scene, screen)
                                # 調用 running_scene 的繪製函式
    pygame.display.flip()       # 讓視窗顯示畫面