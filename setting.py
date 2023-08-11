import pygame           # 引用 pygame 模組

class Settings():       # 定義 Settings 類別

    def __init__(self):                             # 定義建構函式
        Settings.SCREEN_WIDTH = 800                 # 視窗寬度設為 800px
        Settings.SCREEN_HEIGHT = 600                # 視窗高度設為 600px
        Settings.SCREEN_BOARD = 10                  # 與視窗邊緣間隔 10px
        Settings.BACKGROUND_COLOR = (230, 230, 230) # 背景顏色設為淺灰色（230, 230, 230）
        Settings.FPS = 60                           # FPS 設為 60
        Settings.STATUS_IDLE = "IDLE"               # 宣告 STATUS_IDLE 常數
        Settings.STAUTS_RUNNING = "RUNNING"         # 宣告 STATUS_RUNNING 常數
        Settings.STATUS_GAME_OVER = "GAMEOVER"      # 宣告 STATUS_GAME_OVER 常數
        Settings.STATUS_PUASE = "PAUSE"             # 宣告 STATUS_PAUSE 常數
        Settings.LEVEL_GAP = 1000                   # 每 1000 分提升 1 等

        Settings.UP = pygame.K_UP                   # 向上鍵設定為方向鍵上
        Settings.DOWN = pygame.K_DOWN               # 向下鍵設定為方向鍵下
        Settings.RIGHT = pygame.K_RIGHT             # 向右鍵設定為方向鍵右
        Settings.LEFT = pygame.K_LEFT               # 向左鍵設定為方向鍵左
        Settings.QUIT = pygame.K_ESCAPE             # 終止鍵設定為 esc
        Settings.ENTER = pygame.K_RETURN            # 確認鍵設定為 enter
        Settings.FIRE = pygame.K_SPACE              # 攻擊鍵設定為空白鍵
        Settings.SLOW = pygame.K_LSHIFT             # 慢速鍵設定為左側 shift

        Settings.SHIP_SPEED = 10                    # 自機移動速度 10
        Settings.SHIP_SLOW_SPEED = 5                # 自機慢速移動速度 10
        Settings.SHIP_COOLDOWN = 20                 # 自機開火冷卻 20
        Settings.SHIP_LIVES = 3                     # 自機初始生命值 3

        Settings.BULLET_SPEED = 30                  # 子彈飛行速度 30
        Settings.BULLET_WIDTH = 12                  # 子彈寬度 12px
        Settings.BULLET_HEIGHT = 30                 # 子彈高度 30px
        Settings.BULLET_COLOR = (60, 60, 60)        # 子彈顏色深灰色（60, 60, 60）

        Settings.ENEMY_SPEED = 3                            # 敵人移動速度 3
        Settings.ENEMY_SPAWN_TIME = 40                      # 產生敵人的時間間隔
        Settings.ENEMY_BOARD = 10                           # 產生敵人的範圍的左右兩側與視窗邊緣距離
        Settings.ENEMY_SCORE = 100                          # 敵人被命中的分數

        Settings.GUI_TOPLEFT = "TOPLEFT"                    # 宣告 TOPLEFT 常數
        Settings.GUI_TOPRIGHT = "TOPRIGHT"                  # 宣告 TOPRIGHT 常數
        Settings.GUI_BOTTOMLEFT = "BOTTOMLEFT"              # 宣告 BOTTOMLEFT 常數
        Settings.GUI_BOTTOMRIGHT = "BOTTOMRIGHT"            # 宣告 BOTTOMRIGHT 常數
        Settings.GUI_CENTER = "CENTER"                      # 宣告 CENTER 常數

        Settings.GUI_BUTTON_WIDTH = 250                     # 宣告按鈕寬度 250
        Settings.GUI_BUTTON_HEIGHT = 50                     # 宣告按鈕高度 50
        Settings.GUI_BUTTON_COLOR = (20, 200, 20)           # 宣告按鈕顏色為綠色（20, 200, 20）
        Settings.GUI_BUTTON_TEXT_COLOR = (255, 255, 255)    # 宣告按鈕文字顏色為黑色（255, 255, 255）
        Settings.GUI_BUTTON_FONT_SIZE = 48                  # 宣告按鈕文字大小 48

        Settings.GUI_SCORE_FONT_COLOR = (30, 30, 30)        # 宣告分數的文字顏色為深灰色（30, 30, 30）
        Settings.GUI_SCORE_FONT_SIZE = 48                   # 宣告分數的文字大小 48

        Settings.GUI_LABEL_FONT_SIZE = 60                   # 宣告標籤文字大小 60