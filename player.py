import pygame
import functions
import settings

class Player():
    def __init__(self, screen, game):
        self.screen = screen
        self.image = pygame.image.load("assets/player.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = settings.speed
        self.move_right = False
        self.move_left = False
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        self.paused = True
        self.lives = 3
        self.game = game

    def reduce_life(self, ball):
        self.lives -= 1
        if self.lives == 0:
            self.game.game_over()
               
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right and not self.paused:
            self.rect.centerx += self.speed
        if self.move_left and self.rect.left > 0 and not self.paused:
            self.rect.centerx -= self.speed
        self.blitme()
