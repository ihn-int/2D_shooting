import sys
import pygame
from pygame.locals import *

import settings
from scene_manager import SceneEnum, SceneManager

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.SCREEN_CAPTION)

SceneManager.change_scene(SceneEnum.START)

def check_event():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == MOUSEBUTTONDOWN:
            return True, event.pos
    return False, (-1, -1)

while True:
    clock.tick(settings.FPS)

    running_scene = SceneManager.get_scene()
    running_scene.update(check_event())
    running_scene.blit_on(screen)
    pygame.display.flip()