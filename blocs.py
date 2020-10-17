import pygame

class Block():
    def __init__(self, screen, pos):
        self.screen = screen
        self.image = pygame.image.load("assets/block.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = pos 
        self.rect.top = self.screen_rect.top + 15
        self.life = 1
    
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def decrese_life(self):
        self.life -= 1
            
