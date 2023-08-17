import os
import pygame

def load_image(path):
    base_path = os.path.dirname(__file__)
    path = os.path.join(base_path, "assets", path)
    return pygame.image.load(path)