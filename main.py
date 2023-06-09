import pygame
from setting import Settings
from ship import SpaceShip
from enemy import Enemy
from record import GameStatus
from GUI import *

class Game:
    def __init__(self) -> None:
        return None
    
    def Start(self):
        pygame.init()

        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        pygame.display.set_caption("咻咻碰碰碰")
        self.screen.fill(Settings.BACKGROUND_COLOR)

        self.ship = SpaceShip(self)
        self.clock = pygame.time.Clock()

        self.enemies = pygame.sprite.Group()
        self.spawnTime = 0

        self.status = GameStatus()
        self.scoreBoard = ScoreBoard(self)

        self.play_button = Button(self, "Play", 60)
        self.quitButton = Button(self, "Quit", -60)

        self.pauseLabel = Label(self, "Pause")
        self.resumeButton = Button(self, "Resume", 60)
        self.backToMenuButton  = Button(self, "Back to Menu", -60)

        self.gameOverLabel = Label(self, "Game Over")
        self.newGameButton = Button(self, "New Game", 60)
        # self.backToMenu  = Button(self, "Back to Menu", -60)
        

        return None
    
    def RunningCheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == Settings.QUIT:
                    self.status.ChangeStatus(Settings.STATUS_PUASE)
        self.ship.Update()
        self.enemies.update()
        collisions = pygame.sprite.groupcollide(self.ship.bullets, self.enemies, True, True)
        if collisions:
            for enemy in collisions.values():
                self.status.score += Settings.ENEMY_SCORE * len(enemy)
            self.scoreBoard.PrepScore()

        if pygame.sprite.spritecollideany(self.ship, self.enemies):
            self.status.OnHit(self)
            self.scoreBoard.PrepLife()
            self.enemies.empty()
            del self.ship
            self.ship = SpaceShip(self)


    def RunningUpdateScreen(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        
        self.ship.BlitMe()
        for bullet in self.ship.bullets:    
            bullet.BlitMe()

        for enemy in self.enemies:
            if enemy.rect.top > self.screen.get_rect().bottom:
                self.enemies.remove(enemy)
        self.enemies.draw(self.screen)
        self.scoreBoard.ShowScore()
        pygame.display.flip()
        if self.status.score >= self.status.level * Settings.LEVEL_GAP:
            self.status.level += 1
            self.scoreBoard.PrepLevel()
            Enemy.LevelUp()

    def IdleCheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.CheckPlayButton(mouse_pos)
            if event.type == pygame.KEYDOWN:
                if event.key == Settings.QUIT:
                    pygame.quit()
                elif event.key == Settings.ENTER:
                    self.GameInit()
                    self.status.ChangeStatus(Settings.STAUTS_RUNNING)
                    self.scoreBoard.PrepScore()
                    self.scoreBoard.PrepLevel()
                    self.scoreBoard.PrepLife()

    def IdleUpdateScreen(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.play_button.DrawButton()
        self.quitButton.DrawButton()
        pygame.display.flip()

    def PauseCheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == Settings.ENTER:
                    self.status.ChangeStatus(Settings.STAUTS_RUNNING)
                elif event.key == Settings.QUIT:
                    self.status.ChangeStatus(Settings.STATUS_IDLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.CheckPlayButton(mouse_pos)

    def PauseUpdateScreen(self):
        #self.screen.fill(Settings.BACKGROUND_COLOR)
        self.pauseLabel.DrawLabel()
        self.resumeButton.DrawButton()
        self.backToMenuButton.DrawButton()
        pygame.display.flip()

    def GameOverCheckEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == Settings.QUIT:
                    self.status.ChangeStatus(Settings.STATUS_IDLE)
                elif event.key == Settings.ENTER:
                    self.status.ChangeStatus(Settings.STATUS_IDLE)
                    self.status.ChangeStatus(Settings.STAUTS_RUNNING)
                    
                    self.scoreBoard.PrepScore()
                    self.scoreBoard.PrepLevel()
                    self.scoreBoard.PrepLife()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.CheckPlayButton(mouse_pos)
    
    def GameOverUpdateScreen(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.gameOverLabel.DrawLabel()
        self.newGameButton.DrawButton()
        self.backToMenuButton.DrawButton()
        pygame.display.flip()

    def Update(self):
        
        
        while True:
            while self.status.status == Settings.STATUS_IDLE:
                self.clock.tick(Settings.FPS)
                self.IdleCheckEvent()
                self.IdleUpdateScreen()

            while self.status.status == Settings.STAUTS_RUNNING:
                self.clock.tick(Settings.FPS)
                self.RunningCheckEvent()
                self.RunningUpdateScreen()
                self.CreateEnemy()

            while self.status.status == Settings.STATUS_PUASE:
                self.clock.tick(Settings.FPS)
                self.PauseCheckEvent()
                self.PauseUpdateScreen()

            while self.status.status == Settings.STATUS_GAME_OVER:
                self.clock.tick(Settings.FPS)
                self.GameOverCheckEvent()
                self.GameOverUpdateScreen()

    def CreateEnemy(self):
        if self.spawnTime > 0:
            self.spawnTime -= 1
        else:
            enemy = Enemy(self)
            self.enemies.add(enemy)
            self.spawnTime = Settings.ENEMY_SPAWN_TIME

    def GameInit(self):
        self.enemies.empty()
        self.ship.bullets.empty()
        del self.ship
        self.ship = SpaceShip(self)
        self.scoreBoard.PrepScore()
        self.scoreBoard.PrepLevel()
        self.scoreBoard.PrepLife()

    def CheckPlayButton(self, mouse_pos):
        if self.status.status == Settings.STATUS_IDLE:
            if self.play_button.rect.collidepoint(mouse_pos):
                self.status.ChangeStatus(Settings.STAUTS_RUNNING)
                self.GameInit()
            elif self.quitButton.rect.collidepoint(mouse_pos):
                pygame.quit()

        if self.status.status == Settings.STATUS_PUASE:
            if self.resumeButton.rect.collidepoint(mouse_pos):
                self.status.ChangeStatus(Settings.STAUTS_RUNNING)
            elif self.backToMenuButton.rect.collidepoint(mouse_pos):
                self.status.ChangeStatus(Settings.STATUS_IDLE)
        
        if self.status.status == Settings.STATUS_GAME_OVER:
            if self.newGameButton.rect.collidepoint(mouse_pos):
                self.status.ChangeStatus(Settings.STAUTS_RUNNING)
                self.GameInit()
            elif self.backToMenuButton.rect.collidepoint(mouse_pos):
                self.status.ChangeStatus(Settings.STATUS_IDLE)
            


if __name__ == "__main__":
    Settings()
    game = Game()
    game.Start()
    game.Update()