import pygame.font
from setting import Settings
class Button:

    def __init__(self, game, msg, deltaY) -> None:
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = Settings.GUI_BUTTOM_WIDTH, Settings.GUI_BUTTOM_HEIGHT
        self.button_color = Settings.GUI_BUTTOM_COLOR
        self.text_color = Settings.GUI_BUTTOM_TEXT_COLOR
        self.font = pygame.font.SysFont(None, Settings.GUI_BUTTOM_FONT_SIZE)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y -= deltaY
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
class ScoreBoard:
    
    def __init__(self, game) -> None:
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.status = game.status

        self.textColor = Settings.GUI_SCORE_FONT_COLOR
        self.font = pygame.font.SysFont(None, Settings.GUI_SCORE_FONT_SIZE)

        self._prep_score()
        self._prep_level()
        self._prep_life()

    def _prep_score(self):
        scoreText = "{:,}".format(self.status.score)
        self.scoreImage = self.font.render(scoreText, True, self.textColor, Settings.BACKGROUND_COLOR)

        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screen_rect.right - 20
        self.scoreRect.top = 20

    def _prep_level(self):
        levelText = "Level: " + str(self.status.level)
        self.levelImage = self.font.render(levelText, True, self.textColor, Settings.BACKGROUND_COLOR)

        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom + 10

    def _prep_life(self):
        lifeText = "Life: " + str(self.status.shipLives)
        self.lifeImage = self.font.render(lifeText, True, self.textColor, Settings.BACKGROUND_COLOR)

        self.lifeRect = self.lifeImage.get_rect()
        self.lifeRect.right = self.scoreRect.right
        self.lifeRect.top = self.levelRect.bottom + 10

    def show_score(self):
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.levelImage, self.levelRect)
        self.screen.blit(self.lifeImage, self.lifeRect)

class Label:

    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.labelText = msg
        self.textColor = Settings.GUI_SCORE_FONT_COLOR
        self.font = pygame.font.SysFont(None, Settings.GUI_LABEL_FONT_SIZE)

        self.PrepLabel()

    def PrepLabel(self):
        self.labelImage = self.font.render(self.labelText, True, self.textColor, Settings.BACKGROUND_COLOR)

        self.labelRect = self.labelImage.get_rect()
        self.labelRect.center = self.screen.get_rect().center
        self.labelRect.y -= 150
    
    def draw_label(self):
        self.screen.blit(self.labelImage, self.labelRect)
