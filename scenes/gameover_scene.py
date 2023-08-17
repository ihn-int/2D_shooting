import sys
import pygame
from pygame.locals import *

import settings
from scene import Scene
from scene_manager import SceneEnum, SceneManager
from GUI import *

class GameoverSceneCanvas(Canvas):
    def __init__(self) -> None:
        self.retry_button = Button("Retry", (200, 50), (400, 250), settings.GUI_CENTER)
        self.menu_button = Button("Menu", (200, 50), (400, 350), settings.GUI_CENTER)
        self.gameover_label = Label("Game Over!!!", (400, 100), settings.GUI_CENTER)

    def update(self, mouse_action):
        if self.retry_button.is_click(mouse_action):
            SceneManager.change_scene(SceneEnum.GAME)
        if self.menu_button.is_click(mouse_action):
            SceneManager.change_scene(SceneEnum.START)

    def blit_on(self, screen):
        screen.blit(self.retry_button.image, self.retry_button.rect)
        screen.blit(self.menu_button.image, self.menu_button.rect)
        screen.blit(self.gameover_label.image, self.gameover_label.rect)

class GameoverScene(Scene):
    def __init__(self):
        super().__init__("Game Over")
        self.canvas = GameoverSceneCanvas()
        
    def init(self) -> None:
        pass

    def update(self, mouse_action):
        self.canvas.update(mouse_action)

    def blit_on(self, screen):
        self.canvas.blit_on(screen)
