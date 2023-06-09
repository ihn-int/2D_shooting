import pygame

class Settings():
    def __init__(self) -> None:

        Settings.SCREEN_WIDTH = 800
        Settings.SCREEN_HEIGHT = 600
        Settings.BACKGROUND_COLOR = (230, 230, 230)
        Settings.FPS = 60
        Settings.STATUS_IDLE = "IDLE"
        Settings.STAUTS_RUNNING = "RUNNING"
        Settings.STATUS_GAME_OVER = "GAMEOVER"
        Settings.STATUS_PUASE = "PAUSE"
        Settings.LEVEL_GAP = 1000

        Settings.UP = pygame.K_UP
        Settings.DOWN = pygame.K_DOWN
        Settings.RIGHT = pygame.K_RIGHT
        Settings.LEFT = pygame.K_LEFT
        Settings.QUIT = pygame.K_ESCAPE
        Settings.ENTER = pygame.K_RETURN
        Settings.FIRE = pygame.K_SPACE
        Settings.SLOW = pygame.K_LSHIFT

        Settings.SHIP_SPEED = 10
        Settings.SHIP_SLOW_SPEED = 5
        Settings.SHIP_COOLDOWN = 20
        Settings.SHIP_LIVES = 3

        Settings.BULLET_SPEED = 30
        Settings.BULLET_WIDTH = 12
        Settings.BULLET_HEIGHT = 30
        Settings.BULLET_COLOR = (60, 60, 60)

        Settings.ENEMY_SPEED = 3
        Settings.ENEMY_GAP = 30
        Settings.ENEMY_SPAWN_TIME = 40
        Settings.ENEMY_BOARD = 10
        Settings.ENEMY_SCORE = 100

        Settings.GUI_BUTTOM_WIDTH = 250
        Settings.GUI_BUTTOM_HEIGHT = 50
        Settings.GUI_BUTTOM_COLOR = (20, 200, 20)
        Settings.GUI_BUTTOM_TEXT_COLOR = (255, 255, 255)
        Settings.GUI_BUTTOM_FONT_SIZE = 48

        Settings.GUI_SCORE_FONT_COLOR = (30, 30, 30)
        Settings.GUI_SCORE_FONT_SIZE = 48

        Settings.GUI_LABEL_FONT_SIZE = 60