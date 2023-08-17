import sys
import pygame
from pygame.locals import *

import settings
from scene import Scene
from scene_manager import SceneEnum, SceneManager
from GUI import *

class StartSceneCanvas(Canvas):
    def __init__(self):
        self.play_button = Button("Play", (200, 50), (400, 250), settings.GUI_CENTER)
        self.quit_button = Button("Quit", (200, 50), (400, 350), settings.GUI_CENTER)

    def update(self, mouse_action):
        if self.play_button.is_click(mouse_action):       # 如果 play_button 被按下
            SceneManager.change_scene(SceneEnum.GAME)
        elif self.quit_button.is_click(mouse_action):     # 否則如果 quit_button 被按下
            print("QUIT")                                   # 列印出 QUIT 文字
            pygame.quit()                                   # 結束 pygame
            sys.exit(0)                                     # 結束程式

    def blit_on(self, screen):
        screen.blit(self.play_button.image, self.play_button.rect)
        screen.blit(self.quit_button.image, self.quit_button.rect)

class StartScene(Scene):
    def __init__(self):
        super().__init__("Start")
        self.canvas = StartSceneCanvas()

    def init(self) -> None:
        pass

    def update(self, mouse_action):             # 定義 start_scene 的更新函式
        self.canvas.update(mouse_action)       # 調用 start_scene 的 Canvas 的更新函式

    def blit_on(self, screen):                  # 定義 start_scene 的繪製函式 
        screen.fill(settings.BACKGROUND_COLOR)              # 清空畫面中所有內容
        self.canvas.blit_on(screen)            # 調用 start_scene 的 Canvas 的繪製函式
