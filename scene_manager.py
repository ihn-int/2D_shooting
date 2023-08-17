import sys
from enum import Enum
import pygame

from scene import Scene

class SceneEnum(Enum):
    START = 0
    GAME = 1
    PAUSE = 2
    GAMEOVER = 3

class SceneManager:
    instance = None

    def get_instance():
        if SceneManager.instance == None:
            SceneManager.instance = SceneManager()
        return SceneManager.instance
    
    def __init__(self) -> None:
        from scenes.start_scene import StartScene
        from scenes.game_scene import GameScene
        from scenes.pause_scene import PauseScene
        from scenes.gameover_scene import GameoverScene
        self.SCENES: dict[SceneEnum, Scene] = {
            SceneEnum.START: StartScene(),
            SceneEnum.GAME: GameScene(),
            SceneEnum.PAUSE: PauseScene(),
            SceneEnum.GAMEOVER: GameoverScene()
        }

    def init(scene: SceneEnum) -> None:
        instance = SceneManager.get_instance()
        instance.state_stack = [scene]
        SceneManager.get_scene().init()

    def push_scene(scene: SceneEnum) -> None:
        instance = SceneManager.get_instance()
        SceneManager.get_scene().pause()
        instance.state_stack.append(scene)
        SceneManager.get_scene().init()

    def pop_scene() -> None:
        instance = SceneManager.get_instance()
        SceneManager.get_scene().exit()
        instance.state_stack.pop()
        if len(instance.state_stack) == 0:
            pygame.quit()
            sys.exit(0)
        SceneManager.get_scene().resume()

    def override_scene(scene: SceneEnum) -> None:
        instance = SceneManager.get_instance()
        SceneManager.get_scene().exit()
        instance.state_stack.pop()
        while len(instance.state_stack) != 0:
            s = SceneManager.get_scene()
            s.resume()
            s.exit()
            instance.state_stack.pop()
        instance.state_stack = [scene]
        SceneManager.get_scene().init()

    def restart_scene() -> None:
        SceneManager.get_scene().exit()
        SceneManager.get_scene().init()

    def get_scene() -> Scene:
        instance = SceneManager.get_instance()
        return instance.SCENES[instance.state_stack[-1]]