#==========================================================
# initialize

import pygame
import sys
from setting import Settings
from scene import Scene
from GUI import *
from ship import SpaceShip
from enemy import Enemy
pygame.init()
Settings()
Enemy.speed_init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
Scene.running_scene = None


#==========================================================
#==========================================================
# start scene( idle scene )

start_scene = Scene("Start")
start_scene.canvas = Canvas()

start_scene.canvas.play_button = Button("Play", (200, 50), (400, 250), Settings.GUI_CENTER)
start_scene.canvas.quit_button = Button("Quit", (200, 50), (400, 350), Settings.GUI_CENTER)

def start_scene_canvas_update(canvas, mouse_action):
    if canvas.play_button.is_click(mouse_action):
        Scene.change_scene(game_scene)
        game_scene.init(game_scene, True)
    elif canvas.quit_button.is_click(mouse_action):
        print("QUIT")
        pygame.quit()
        sys.quit()

def start_scene_canvas_blit_on(canvas, screen):
    screen.blit(canvas.play_button.image, canvas.play_button.rect)
    screen.blit(canvas.quit_button.image, canvas.quit_button.rect)

def start_scene_update(self, mouse_action):
    self.canvas.update(self.canvas, mouse_action)

def start_scene_blit_on(self, screen):
    screen.fill(Settings.BACKGROUND_COLOR)
    self.canvas.blit_on(self.canvas, screen)

start_scene.canvas.update = start_scene_canvas_update
start_scene.canvas.blit_on = start_scene_canvas_blit_on
start_scene.update = start_scene_update
start_scene.blit_on = start_scene_blit_on

#==========================================================
#==========================================================
# game scene

game_scene = Scene("Game")
game_scene_canvas = Canvas()
game_scene_canvas.score_board = Label("score:", (790, 10), Settings.GUI_TOPRIGHT)
game_scene_canvas.level_board = Label("level: ", (790, 70), Settings.GUI_TOPRIGHT)
game_scene_canvas.lives_bar = Label("lives:", (790, 130), Settings.GUI_TOPRIGHT)
game_scene.score = 0
game_scene.lives = 3
game_scene.level = 1
game_scene.ship = SpaceShip()
game_scene.ship.rect.center = (400, 500)
game_scene.enemies = pygame.sprite.Group()
game_scene.spawn_time = Settings.ENEMY_SPAWN_TIME
game_scene.canvas = game_scene_canvas

def game_scene_init(self, is_clear):
    if is_clear:
        self.lives = 3
        self.level = 1
        self.score = 0
    if self.ship:
        del self.ship
    self.ship = SpaceShip()
    self.ship.rect.center = (400, 500)
    self.enemies.empty()

def create_enemy(self):
    if self.spawn_time > 0:
        self.spawn_time -= 1
    else:
        enemy = Enemy()
        self.enemies.add(enemy)
        self.spawn_time = Settings.ENEMY_SPAWN_TIME

def on_hit(self):
    self.lives -= 1
    if self.lives <= 0:
        print("Game Over")
        Scene.change_scene(gameover_scene)
    self.init(self, False)

def game_scene_canvas_update(self, mouse_action, score, level, lives):
    if pygame.key.get_pressed()[Settings.QUIT]:
        Scene.change_scene(pause_scene)
    _score_board = self.score_board
    _level_board = self.level_board
    _lives_bar = self.lives_bar
    _score_board.msg = "score: " + str(score)
    _level_board.msg = "level: " + str(level)
    _lives_bar.msg = "lives: " + str(lives)
    _score_board._prep_label()
    _level_board._prep_label()
    _lives_bar._prep_label()
    

def game_scene_canvas_blit_on(self, screen):
    _score_board = self.score_board
    _level_board = self.level_board
    _lives_bar = self.lives_bar
    screen.blit(_score_board.image, _score_board.rect)
    screen.blit(_level_board.image, _level_board.rect)
    screen.blit(_lives_bar.image, _lives_bar.rect)

def game_scene_update(self, mouse_action):
    self.create_enemies(self)
    self.ship.update()
    self.enemies.update()
    for enemy in self.enemies:
        if enemy.rect.top > Settings.SCREEN_HEIGHT:
            self.enemies.remove(enemy)
    collisions = pygame.sprite.groupcollide(self.ship.bullets, self.enemies, True, True)
    if collisions:
        self.score += Settings.ENEMY_SCORE
        self.canvas.score_board._prep_label()
    if pygame.sprite.spritecollideany(self.ship, self.enemies):
        self.on_hit(self)
    if self.score >= self.level * Settings.LEVEL_GAP:
        self.level += 1
        Enemy.level_up()
    self.canvas.update(self.canvas, mouse_action, self.score, self.level, self.lives)

def game_scene_blit_on(self, screen):
    screen.fill(Settings.BACKGROUND_COLOR)
    screen.blit(self.ship.image, self.ship.rect)
    self.ship.bullets.draw(screen)
    self.enemies.draw(screen)
    self.canvas.blit_on(self.canvas, screen)

game_scene_canvas.update = game_scene_canvas_update
game_scene_canvas.blit_on = game_scene_canvas_blit_on
game_scene.update = game_scene_update
game_scene.blit_on = game_scene_blit_on
game_scene.create_enemies = create_enemy
game_scene.on_hit = on_hit
game_scene.init = game_scene_init

#==========================================================
#==========================================================
# pause scene

pause_scene = Scene("Pause")
pause_scene_canvas = Canvas()
pause_scene_canvas.resume_button = Button("Resume", (200, 50), (400, 250), Settings.GUI_CENTER)
pause_scene_canvas.menu_button = Button("Menu", (200, 50), (400, 350), Settings.GUI_CENTER)
pause_scene.canvas = pause_scene_canvas


def pause_scene_canvas_update(self, mouse_action):
    keypress = pygame.key.get_pressed()
    if self.resume_button.is_click(mouse_action):
        Scene.change_scene(game_scene)
    if self.menu_button.is_click(mouse_action):
        Scene.change_scene(start_scene)

def pause_scene_canvas_blit_on(self, screen):
    screen.blit(self.resume_button.image, self.resume_button.rect)
    screen.blit(self.menu_button.image, self.menu_button.rect)

def pause_scene_update(self, mouse_action):
    self.canvas.update(self.canvas, mouse_action)

def pause_scene_blit_on(self, screen):
    self.canvas.blit_on(self.canvas, screen)

pause_scene.canvas.update = pause_scene_canvas_update
pause_scene.canvas.blit_on = pause_scene_canvas_blit_on
pause_scene.update = pause_scene_update
pause_scene.blit_on = pause_scene_blit_on

#==========================================================
#==========================================================
# game over scene

gameover_scene = Scene("Game Over")
gameover_scene_canvas = Canvas()
gameover_scene_canvas.retry_button = Button("Retry", (200, 50), (400, 250), Settings.GUI_CENTER)
gameover_scene_canvas.menu_button = Button("Menu", (200, 50), (400, 350), Settings.GUI_CENTER)
gameover_scene_canvas.gameover_label = Label("Game Over!!!", (400, 100), Settings.GUI_CENTER)

def gameover_scene_canvas_update(self, mouse_action):
    if self.retry_button.is_click(mouse_action):
        game_scene.init(game_scene, True)
        Scene.change_scene(game_scene)
    if self.menu_button.is_click(mouse_action):
        Scene.change_scene(start_scene)

def gameover_scene_canvas_blit_on(self, screen):
    screen.blit(self.retry_button.image, self.retry_button.rect)
    screen.blit(self.menu_button.image, self.menu_button.rect)
    screen.blit(self.gameover_label.image, self.gameover_label.rect)

def gameover_scene_update(self, mouse_action):
    self.canvas.update(self.canvas, mouse_action)

def gameover_scene_blit_on(self, screen):
    self.canvas.blit_on(self.canvas, screen)

gameover_scene.canvas = gameover_scene_canvas
gameover_scene.canvas.update = gameover_scene_canvas_update
gameover_scene.canvas.blit_on = gameover_scene_canvas_blit_on
gameover_scene.update = gameover_scene_update
gameover_scene.blit_on = gameover_scene_blit_on

#==========================================================
#==========================================================
# scene running

Scene.change_scene(start_scene)

while True:
    clock.tick(Settings.FPS)
    _mouse_action = Scene.running_scene.check_event()
    Scene.running_scene.update(Scene.running_scene, _mouse_action)
    Scene.running_scene.blit_on(Scene.running_scene, screen)

    pygame.display.flip()