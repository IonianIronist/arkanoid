import pygame

class Ball():
    def __init__(self, screen, player):
        self.screen = screen
        self.image = pygame.image.load("assets/ball.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = player.rect.top
        self.blitme()
        self.speed = [0,-4]    
        self.paused = True

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def move(self, speed):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

    def check_collision(self, blox, player):
        for block in blox:
            if self.rect.colliderect(block.rect):
                if ((self.rect.left < block.rect.right and self.rect.right > block.rect.right) or 
                    (self.rect.right > block.rect.left and self.rect.left < block.rect.left)):
                    self.speed[0] = - self.speed[0]
                elif ((self.rect.top < block.rect.bottom and self.rect.bottom > block.rect.bottom) or 
                      (self.rect.bottom > block.rect.top and self.rect.top < block.rect.bottom)):
                    self.speed[1] = - self.speed[1]
                block.decrese_life()
        if self.rect.right > self.screen_rect.right or self.rect.left < self.screen_rect.left:
            self.speed[0] = - self.speed[0]         
        if self.rect.top < self.screen_rect.top:
            self.speed[1] = - self.speed[1]
        elif self.rect.bottom > self.screen_rect.bottom:
            self.speed[1] = - self.speed[1]
            player.reduce_life(self)
                    
        if self.rect.colliderect(player.rect):
            if self.rect.centerx > player.rect.centerx:
                self.speed[0] , self.speed[1] = 2, -2
            else:
                self.speed[0] , self.speed[1] = -2, -2
    def update(self, blox, player):
        self.check_collision(blox, player)    
        if not self.paused:
            self.move(self.speed)
        self.blitme()
