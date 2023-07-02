import pygame.font
from setting import Settings

Settings()

class Canvas:

    def __init__(self):
        pass

    def update(self):
        pass

    def blit_on(self, screen):
        pass


class Button:

    def __init__(self, msg, scale, pos, anchor,
                  button_color = Settings.GUI_BUTTON_COLOR,
                  text_color = Settings.GUI_BUTTON_TEXT_COLOR,
                  font_size = Settings.GUI_BUTTON_FONT_SIZE):
        self.button_color = button_color
        self.text_color = text_color
        self.anchor = anchor
        self.pos = pos
        self.font = pygame.font.SysFont(None, font_size)
        self.image = pygame.Surface(scale)
        self.rect = self.image.get_rect()
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.image.fill(self.button_color)
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.width / 2
        self.msg_image_rect.centery = self.rect.height / 2
        if self.anchor == Settings.GUI_TOPLEFT:
            self.rect.topleft = self.pos
        elif self.anchor == Settings.GUI_TOPRIGHT:
            self.rect.topright = self.pos
        elif self.anchor == Settings.GUI_BOTTOMLEFT:
            self.rect.bottomleft = self.pos
        elif self.anchor == Settings.GUI_BOTTOMRIGHT:
            self.rect.bottomright = self.pos
        elif self.anchor == Settings.GUI_CENTER:
            self.rect.center = self.pos
        self.image.blit(self.msg_image, self.msg_image_rect)

    def is_click(self, mouse_action) -> bool:
        if mouse_action[0] and self.rect.collidepoint(mouse_action[1]):
            return True


class Label:

    def __init__(self, msg, pos, anchor,
                text_color = Settings.GUI_SCORE_FONT_COLOR,
                font_size = Settings.GUI_LABEL_FONT_SIZE):
        self.msg = msg
        self.text_color = text_color
        self.pos = pos
        self.anchor = anchor
        self.font = pygame.font.SysFont(None, font_size)
        self._prep_label()

    def _prep_label(self):
        self.image = self.font.render(self.msg, True, self.text_color, Settings.BACKGROUND_COLOR)
        self.rect = self.image.get_rect()
        if self.anchor == Settings.GUI_TOPLEFT:
            self.rect.topleft = self.pos
        elif self.anchor == Settings.GUI_TOPRIGHT:
            self.rect.topright = self.pos
        elif self.anchor == Settings.GUI_BOTTOMLEFT:
            self.rect.bottomleft = self.pos
        elif self.anchor == Settings.GUI_BOTTOMRIGHT:
            self.rect.bottomright = self.pos
        elif self.anchor ==Settings.GUI_CENTER:
            self.rect.center = self.pos
    
