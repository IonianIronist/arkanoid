import pygame
import functions
import settings
from player import Player
from ball import Ball
from buttons import Button

class Game():
    def __init__(self):
        pygame.init()
        self.player = Player(settings.screen, self)
        self.ball = Ball(settings.screen, self.player)
        self.go_button = Button(settings.screen)
        self.go = False
        self.level = settings.get_level()[0]
    def loop(self):
        functions.check_events(self.player, self.ball, self.go, self)    
        settings.screen.fill(settings.background_color)
        self.player.update()
        self.ball.update(self.level, self.player)
        if self.go:
            self.go_button.blitme()
        functions.update_level(self.level)
        pygame.display.flip()
    def game_over(self):
        self.ball.paused = True
        self.player.paused = True
        self.go = True
    def restart(self):
        self.player = Player(settings.screen, self)
        self.ball = Ball(settings.screen, self.player)
        self.go = False
        self.level = settings.get_level()[0]

def run():
    game = Game()
    while True:
        game.loop()

run()


