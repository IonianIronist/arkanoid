import pygame

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assets/player.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 3
        self.move_right = False
        self.move_left = False
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        self.paused = True


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right and not self.paused:
            self.rect.centerx += self.speed
        if self.move_left and self.rect.left > 0 and not self.paused:
            self.rect.centerx -= self.speed
        self.blitme()
