import pygame
from blocs import Block

colors = {
          'grey' : (230, 230, 230)
            }

background_color = colors['grey']

width, height = 800, 600

size = width, height
screen = pygame.display.set_mode(size)
screen.fill(background_color)
pygame.display.set_caption("Arkanoid")
speed = 2
ball_speed = 5



def get_level():
    level = [[Block(screen, 21)]]
    for i in range(1, 11):
        level[0].append(Block(screen, level[0][-1].rect.right + 10))
    return level
