from enum import Enum

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
        self.running_scene = SceneEnum.START
    
    def change_scene(next_scene: SceneEnum) -> None:
        instance = SceneManager.get_instance()
        instance.running_scene = next_scene
        instance.SCENES[instance.running_scene].init()

    def get_scene() -> Scene:
        instance = SceneManager.get_instance()
        return instance.SCENES[instance.running_scene]