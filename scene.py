import pygame

class Scene:


    def __init__(self, scene_name) -> None:
        self.tag = scene_name
        self.canvas = None

    def change_scene(next_scene):
        Scene.running_scene = next_scene

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return True, pygame.mouse.get_pos()
        return False, (-1, -1)

    def update(self):
        pass

    def blit_on(self, screen):
        pass