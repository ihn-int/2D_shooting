from pygame.locals import *

SCREEN_WIDTH = 800                 # 視窗寬度設為 800px
SCREEN_HEIGHT = 600                # 視窗高度設為 600px
SCREEN_CAPTION = "咻咻碰碰碰"
SCREEN_BOARD = 10                  # 與視窗邊緣間隔 10px
BACKGROUND_COLOR = (230, 230, 230) # 背景顏色設為淺灰色（230, 230, 230）
FPS = 60                           # FPS 設為 60
STATUS_IDLE = "IDLE"               # 宣告 STATUS_IDLE 常數
STAUTS_RUNNING = "RUNNING"         # 宣告 STATUS_RUNNING 常數
STATUS_GAME_OVER = "GAMEOVER"      # 宣告 STATUS_GAME_OVER 常數
STATUS_PUASE = "PAUSE"             # 宣告 STATUS_PAUSE 常數
LEVEL_GAP = 1000                   # 每 1000 分提升 1 等

UP = K_UP                          # 向上鍵設定為方向鍵上
DOWN = K_DOWN                      # 向下鍵設定為方向鍵下
RIGHT = K_RIGHT                    # 向右鍵設定為方向鍵右
LEFT = K_LEFT                      # 向左鍵設定為方向鍵左
QUIT = K_ESCAPE                    # 終止鍵設定為 esc
ENTER = K_RETURN                   # 確認鍵設定為 enter
FIRE = K_SPACE                     # 攻擊鍵設定為空白鍵
SLOW = K_LSHIFT                    # 慢速鍵設定為左側 shift

SHIP_SPEED = 10                    # 自機移動速度 10
SHIP_SLOW_SPEED = 5                # 自機慢速移動速度 10
SHIP_COOLDOWN = 5                  # 自機開火冷卻 20
SHIP_LIVES = 3                     # 自機初始生命值 3
SHIP_COLLIDE_RADIUS = 25
SHIP_GRAZE_RADIUS = 45
SHIP_COLLISION_INDICATOR_WIDTH = 1

BULLET_SPEED = 30                  # 子彈飛行速度 30
ENEMY_BULLET_SPEED = 6
BULLET_RADIUS = 6                  # 子彈半徑 6px
BULLET_COLOR = (60, 60, 60)        # 子彈顏色深灰色（60, 60, 60）

ENEMY_SPEED = 2                            # 敵人移動速度 2
ENEMY_SPAWN_TIME = 40                      # 產生敵人的時間間隔
ENEMY_BOARD = 10                           # 產生敵人的範圍的左右兩側與視窗邊緣距離
ENEMY_SCORE = 100                          # 敵人被命中的分數
ENEMY_COLLIDE_RADIUS = 30

GUI_TOPLEFT = "TOPLEFT"                    # 宣告 TOPLEFT 常數
GUI_TOPRIGHT = "TOPRIGHT"                  # 宣告 TOPRIGHT 常數
GUI_BOTTOMLEFT = "BOTTOMLEFT"              # 宣告 BOTTOMLEFT 常數
GUI_BOTTOMRIGHT = "BOTTOMRIGHT"            # 宣告 BOTTOMRIGHT 常數
GUI_CENTER = "CENTER"                      # 宣告 CENTER 常數

GUI_BUTTON_WIDTH = 250                     # 宣告按鈕寬度 250
GUI_BUTTON_HEIGHT = 50                     # 宣告按鈕高度 50
GUI_BUTTON_COLOR = (20, 200, 20)           # 宣告按鈕顏色為綠色（20, 200, 20）
GUI_BUTTON_TEXT_COLOR = (255, 255, 255)    # 宣告按鈕文字顏色為黑色（255, 255, 255）
GUI_BUTTON_FONT_SIZE = 48                  # 宣告按鈕文字大小 48

GUI_SCORE_FONT_COLOR = (30, 30, 30)        # 宣告分數的文字顏色為深灰色（30, 30, 30）
GUI_SCORE_FONT_SIZE = 48                   # 宣告分數的文字大小 48

GUI_LABEL_FONT_SIZE = 60                   # 宣告標籤文字大小 60