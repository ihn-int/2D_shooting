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
        self.spawn_time = 0

        self.status = GameStatus()
        self.score_board = ScoreBoard(self)

        self.play_button = Button(self, "Play", 60)
        self.quit_button = Button(self, "Quit", -60)

        self.pause_label = Label(self, "Pause")
        self.resume_button = Button(self, "Resume", 60)
        self.back_to_menu_button  = Button(self, "Back to Menu", -60)

        self.game_over_label = Label(self, "Game Over")
        self.new_game_button = Button(self, "New Game", 60)
        
        return None
    
    def running_check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == Settings.QUIT:
                    self.status.change_status(Settings.STATUS_PUASE)
        self.ship.update()
        self.enemies.update()
        collisions = pygame.sprite.groupcollide(self.ship.bullets, self.enemies, True, True)
        if collisions:
            for enemy in collisions.values():
                self.status.score += Settings.ENEMY_SCORE * len(enemy)
            self.score_board._prep_score()

        if pygame.sprite.spritecollideany(self.ship, self.enemies):
            self.status.on_hit(self)
            self.score_board._prep_life()
            self.enemies.empty()
            del self.ship
            self.ship = SpaceShip(self)


    def running_update_screen(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        
        self.ship.blit_me()
        for bullet in self.ship.bullets:    
            bullet.BlitMe()

        for enemy in self.enemies:
            if enemy.rect.top > self.screen.get_rect().bottom:
                self.enemies.remove(enemy)
        self.enemies.draw(self.screen)
        self.score_board.show_score()
        pygame.display.flip()
        if self.status.score >= self.status.level * Settings.LEVEL_GAP:
            self.status.level += 1
            self.score_board._prep_level()
            Enemy.level_up()

    def idle_check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
            if event.type == pygame.KEYDOWN:
                if event.key == Settings.QUIT:
                    pygame.quit()
                elif event.key == Settings.ENTER:
                    self.game_init()
                    self.status.change_status(Settings.STAUTS_RUNNING)
                    self.score_board._prep_score()
                    self.score_board._prep_level()
                    self.score_board._prep_life()

    def idle_update_screen(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.play_button.draw_button()
        self.quit_button.draw_button()
        pygame.display.flip()

    def pause_check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == Settings.ENTER:
                    self.status.change_status(Settings.STAUTS_RUNNING)
                elif event.key == Settings.QUIT:
                    self.status.change_status(Settings.STATUS_IDLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def pause_update_screen(self):
        self.pause_label.draw_label()
        self.resume_button.draw_button()
        self.back_to_menu_button.draw_button()
        pygame.display.flip()

    def game_over_check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == Settings.QUIT:
                    self.status.change_status(Settings.STATUS_IDLE)
                elif event.key == Settings.ENTER:
                    self.status.change_status(Settings.STATUS_IDLE)
                    self.status.change_status(Settings.STAUTS_RUNNING)
                    
                    self.score_board._prep_score()
                    self.score_board._prep_level()
                    self.score_board._prep_life()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
    
    def game_over_update_screen(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.game_over_label.draw_label()
        self.new_game_button.draw_button()
        self.back_to_menu_button.draw_button()
        pygame.display.flip()

    def update(self):
        
        
        while True:
            while self.status.status == Settings.STATUS_IDLE:
                self.clock.tick(Settings.FPS)
                self.idle_check_event()
                self.idle_update_screen()

            while self.status.status == Settings.STAUTS_RUNNING:
                self.clock.tick(Settings.FPS)
                self.running_check_event()
                self.running_update_screen()
                self.create_enemy()

            while self.status.status == Settings.STATUS_PUASE:
                self.clock.tick(Settings.FPS)
                self.pause_check_event()
                self.pause_update_screen()

            while self.status.status == Settings.STATUS_GAME_OVER:
                self.clock.tick(Settings.FPS)
                self.game_over_check_event()
                self.game_over_update_screen()

    def create_enemy(self):
        if self.spawn_time > 0:
            self.spawn_time -= 1
        else:
            enemy = Enemy(self)
            self.enemies.add(enemy)
            self.spawn_time = Settings.ENEMY_SPAWN_TIME

    def game_init(self):
        self.enemies.empty()
        self.ship.bullets.empty()
        del self.ship
        self.ship = SpaceShip(self)
        self.score_board._prep_score()
        self.score_board._prep_level()
        self.score_board._prep_life()

    def check_play_button(self, mouse_pos):
        if self.status.status == Settings.STATUS_IDLE:
            if self.play_button.rect.collidepoint(mouse_pos):
                self.status.change_status(Settings.STAUTS_RUNNING)
                self.game_init()
            elif self.quit_button.rect.collidepoint(mouse_pos):
                pygame.quit()

        if self.status.status == Settings.STATUS_PUASE:
            if self.resume_button.rect.collidepoint(mouse_pos):
                self.status.change_status(Settings.STAUTS_RUNNING)
            elif self.back_to_menu_button.rect.collidepoint(mouse_pos):
                self.status.change_status(Settings.STATUS_IDLE)
        
        if self.status.status == Settings.STATUS_GAME_OVER:
            if self.new_game_button.rect.collidepoint(mouse_pos):
                self.status.change_status(Settings.STAUTS_RUNNING)
                self.game_init()
            elif self.back_to_menu_button.rect.collidepoint(mouse_pos):
                self.status.change_status(Settings.STATUS_IDLE)
            


if __name__ == "__main__":
    Settings()
    game = Game()
    game.Start()
    game.update()