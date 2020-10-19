import pygame
import functions
import math
import settings
from player import Player
from ball import Ball

pygame.init()
player = Player(settings.screen)
ball = Ball(settings.screen, player)

while True:
    functions.check_events(player, ball)    
    settings.screen.fill(settings.background_color)
    player.update()
    ball.update(settings.levels[0], player)
    functions.update_level(settings.levels[0])
    pygame.display.flip()
