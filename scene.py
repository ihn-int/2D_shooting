import sys
import pygame

class Scene:
    def __init__(self, scene_name):             # 定義建構函式
        self.tag = scene_name                   # 將物件的 tag 屬性設為 scene_name
        self.canvas = None                      # 宣告 canvas 屬性
    
    def init(self) -> None:
        pass

    def pause(self) -> None:
        pass

    def resume(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def update(self) -> None:
        pass

    def blit_on(self, screen: pygame.Surface):
        pass