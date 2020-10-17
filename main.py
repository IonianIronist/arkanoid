import pygame
from player import Player
import functions
from blocs import Block
import math
from ball import Ball

pygame.init()
size = width, height = 800, 600

grey = 230, 230, 230

screen = pygame.display.set_mode(size)
screen.fill(grey)
pygame.display.set_caption("Arkanoid")
player = Player(screen)
ball = Ball(screen, player)
blox = [Block(screen, 21)]

for i in range(1, 11):
    blox.append(Block(screen, blox[-1].rect.right + 10))
while True:
    functions.check_events(player, ball)    
    screen.fill(grey)
    player.update()
    ball.update(blox, player)
    dead = []    
    for i in range(len(blox)):
        blox[i].blitme()
        if blox[i].life == 0 :
            dead.append(i)
    for d in dead:
        blox.pop(d)
    pygame.display.flip()

