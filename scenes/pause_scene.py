import sys
import pygame
from pygame.locals import *

import settings
from scene import Scene
from scene_manager import SceneEnum, SceneManager
from GUI import *

class PauseSceneCanvas(Canvas):
    def __init__(self) -> None:
        self.resume_button = Button("Resume", (200, 50), (400, 250), settings.GUI_CENTER)
        self.menu_button = Button("Menu", (200, 50), (400, 350), settings.GUI_CENTER)
        self.paused_label = Label("Paused", (400, 100), settings.GUI_CENTER)

    def update(self, mouse_action):
        if self.resume_button.is_click(mouse_action):
            SceneManager.pop_scene()
            return
        if self.menu_button.is_click(mouse_action):
            SceneManager.override_scene(SceneEnum.START)
            return

    def blit_on(self, screen):
        screen.blit(self.resume_button.image, self.resume_button.rect)
        screen.blit(self.menu_button.image, self.menu_button.rect)
        screen.blit(self.paused_label.image, self.paused_label.rect)

class PauseScene(Scene):
    def __init__(self):
        super().__init__("Pause")
        self.canvas = PauseSceneCanvas()
        
    def init(self) -> None:
        pass

    def pause(self) -> None:
        pass

    def resume(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def update(self, mouse_action):
        self.canvas.update(mouse_action)

    def blit_on(self, screen):
        self.canvas.blit_on(screen)
