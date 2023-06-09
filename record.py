import pygame
from setting import Settings
from enemy import *

class GameStatus:

    def __init__(self):
        self.shipLives = Settings.SHIP_LIVES
        self.status = Settings.STATUS_IDLE
        self.score = 0
        self.level = 0

    def OnHit(self, game):
        self.shipLives -= 1
        print("On Hit")
        if self.shipLives <= 0:
            print("Game Over")
            self.ChangeStatus(Settings.STATUS_GAME_OVER)

    def ChangeStatus(self, status):
        if status == Settings.STATUS_IDLE:
            self.status = Settings.STATUS_IDLE
        if status == Settings.STAUTS_RUNNING:
            if not self.status == Settings.STATUS_PUASE:
                self.shipLives = Settings.SHIP_LIVES
                self.score = 0
                self.level = 1
                Enemy.SpeedInit()
            self.status = Settings.STAUTS_RUNNING
        if status == Settings.STATUS_PUASE:
            self.status = Settings.STATUS_PUASE
        if status == Settings.STATUS_GAME_OVER:
            self.status = Settings.STATUS_GAME_OVER
