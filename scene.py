import pygame   # 引用 pygame 模組
import sys      # 引用 sys 模組
class Scene:    # 定義 Scene 類別

    def __init__(self, scene_name):             # 定義建構函式
        self.tag = scene_name                   # 將物件的 tag 屬性設為 scene_name
        self.canvas = None                      # 宣告 canvas 屬性
        Scene.running_scene = None              # 宣告 running_scene 屬性，代表當下運行場景

    def change_scene(next_scene):               # 定義場景切換的函式
        Scene.running_scene = next_scene        # 將當下運行的場景切換為 next_scene

    def check_event(self):                      # 定義用於檢查 event 的函式
        for event in pygame.event.get():        # 對所有事件佇列中的事件
            if event.type == pygame.QUIT:       # 如果事件類型是 pygame.QUIT
                pygame.quit()                   # 結束 pygame
                sys.exit(0)                     # 結束程式
            elif event.type == pygame.MOUSEBUTTONDOWN:
                                                # 否則如果事件類型是 pygame.MOUSEBUTTONDOWN
                return True, pygame.mouse.get_pos()
                                                # 回傳滑鼠行為：True, <滑鼠位置>
        return False, (-1, -1)                  # 如果沒有按下滑鼠，則回傳：False, (-1, -1)

    def update(self):           # 定義用於場景更新的函式
        pass                    # pass

    def blit_on(self, screen):  # 定義用於場景繪製的函式
        pass                    # pass