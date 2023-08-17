import pygame.font

import settings

class Canvas:
    def update(self):
        pass

    def blit_on(self, screen):
        pass

class Button:
    def __init__(self, msg, scale, pos, anchor,
                  button_color = settings.GUI_BUTTON_COLOR,
                  text_color = settings.GUI_BUTTON_TEXT_COLOR,
                  font_size = settings.GUI_BUTTON_FONT_SIZE):   # 定義建構函式
        self.button_color = button_color                        # 設定按鈕底色
        self.text_color = text_color                            # 設定文字顏色
        self.anchor = anchor                                    # 設定錨點
        self.pos = pos                                          # 設定位置
        self.font = pygame.font.SysFont(None, font_size)        # 宣告 font 屬性為 SysFont 物件
        self.image = pygame.Surface(scale)                      # 宣告 image 屬性為 Surface 物件
        self.rect = self.image.get_rect()                       # 宣告 rect 屬性為 image 的 rect
        self._prep_msg(msg)                                     # 調用渲染按鈕的函式

    def _prep_msg(self, msg):                                   # 定義用於渲染按鈕的函式
        self.image.fill(self.button_color)                      # 將 image 填滿顏色
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
                                                            # 宣告 msg_image 屬性為文字的 Surface
        self.msg_image_rect = self.msg_image.get_rect()     # 宣告 msg_image_rect 屬性
        self.msg_image_rect.centerx = self.rect.width / 2   # 將文字置中
        self.msg_image_rect.centery = self.rect.height / 2  # 將文字置中
        if self.anchor == settings.GUI_TOPLEFT:             # 如果錨點位於左上角
            self.rect.topleft = self.pos                    # 就將錨點移到指定位置
        elif self.anchor == settings.GUI_TOPRIGHT:          # 如果錨點位於右上角
            self.rect.topright = self.pos                   # 就將錨點移到指定位置
        elif self.anchor == settings.GUI_BOTTOMLEFT:        # 如果錨點位於左下角
            self.rect.bottomleft = self.pos                 # 就將錨點移到指定位置
        elif self.anchor == settings.GUI_BOTTOMRIGHT:       # 如果錨點位於右下角
            self.rect.bottomright = self.pos                # 就將錨點移到指定位置
        elif self.anchor == settings.GUI_CENTER:            # 如果錨點位於中心
            self.rect.center = self.pos                     # 就將錨點移到指定位置
        self.image.blit(self.msg_image, self.msg_image_rect)# 將 msg_image 繪製到 image 上

    def is_click(self, mouse_action):   # 定義按鈕被按下的函式
        if mouse_action[0] and self.rect.collidepoint(mouse_action[1]):
                                                # 如果滑鼠有被按下，且滑鼠位置位於 rect 中
            return True                         # 回傳 True

class Label:
    def __init__(self, msg, pos, anchor,
                text_color = settings.GUI_SCORE_FONT_COLOR,
                font_size = settings.GUI_LABEL_FONT_SIZE):
                                        # 定義建構函式
        self.msg = msg                  # 設定文字
        self.text_color = text_color    # 設定文字顏色
        self.pos = pos                  # 設定位置
        self.anchor = anchor            # 設定錨點
        self.font = pygame.font.SysFont(None, font_size)
                                        # 宣告 font 屬性為 SysFont 物件
        self._prep_label()              # 調用渲染標籤的函式

    def _prep_label(self):                              # 定義渲染標籤的函式
        self.image = self.font.render(self.msg, True, self.text_color, settings.BACKGROUND_COLOR) # 宣告 image 屬性為文字的 Surface
        self.rect = self.image.get_rect()               # 宣告 rect 屬性為 image 的 rect 屬性
        if self.anchor == settings.GUI_TOPLEFT:         # 如果錨點位於左上角
            self.rect.topleft = self.pos                # 就將錨點移到指定位置
        elif self.anchor == settings.GUI_TOPRIGHT:      # 如果錨點位於右上角
            self.rect.topright = self.pos               # 就將錨點移到指定位置
        elif self.anchor == settings.GUI_BOTTOMLEFT:    # 如果錨點位於左下角
            self.rect.bottomleft = self.pos             # 就將錨點移到指定位置
        elif self.anchor == settings.GUI_BOTTOMRIGHT:   # 如果錨點位於右下角
            self.rect.bottomright = self.pos            # 就將錨點移到指定位置
        elif self.anchor ==settings.GUI_CENTER:         # 如果錨點位於中心
            self.rect.center = self.pos                 # 就將錨點移到指定位置
    
