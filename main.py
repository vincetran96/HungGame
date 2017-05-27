import pygame
from inputmanager import *
from gamemanager import *
from player import *
from background import *
from constraints import *
from edible import *
import random

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("Hưng game")
    return screen

def run():
    game_manager.run()

def draw(screen):
    screen.fill((0, 0, 0))

    game_manager.draw(screen)

screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
player = Player()
game_manager.add(player)
player.constraints = Constraints(0,400,0,600)

loop = True

i = 120
while loop:
    events = pygame.event.get()

    # Handle QUIT event
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

    input_manager.run(events)
    i -= 1
    if i == 0:
        eat = Edible()
        eat.position.x = random.randrange(50, 350)
        eat.direction_x = random.randrange(-1,1)
        eat.direction_y = random.choice((3,5))
        game_manager.add(eat)
        i = 120

    ## Update logic
    run()

    ## update graphics
    draw(screen)

    ## delay by frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()