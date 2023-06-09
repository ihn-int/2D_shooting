import pygame
from setting import Settings
from bullet import Bullet

class SpaceShip:
    def __init__(self, game) -> None:
        self.image = pygame.image.load(".\\spaceship.bmp")
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.bullets = pygame.sprite.Group()

        self.speed = Settings.SHIP_SPEED
        self.firecount = 0
        self.life = Settings.SHIP_LIVES
    
    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.firecount > 0:
            self.firecount -= 1
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


        self.keypress = pygame.key.get_pressed()
        if self.keypress[Settings.SLOW]:
            self.speed = Settings.SHIP_SLOW_SPEED
        else:
            self.speed = Settings.SHIP_SPEED

        if self.keypress[Settings.RIGHT] and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
            
        if self.keypress[Settings.LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if self.keypress[Settings.UP] and self.rect.top > 0:
            self.rect.y -= self.speed

        if self.keypress[Settings.DOWN] and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed

        if self.keypress[Settings.FIRE] and self.firecount == 0:
            bullet = Bullet(self)
            self.bullets.add(bullet)
            self.firecount = Settings.SHIP_COOLDOWN