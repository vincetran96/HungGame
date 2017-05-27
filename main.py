import pygame
from inputmanager import *
from gamemanager import *
from player import *
from background import *
from constraints import *
from physics import *
from fruit import *
import random

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("Hung Game")

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

i = 0
while loop:
    events = pygame.event.get()
    # Handle QUIT event
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
    input_manager.run(events)

    edible = Edible()
    i += 1
    if i == 80:
        # edible.position.x = random.randrange(50, 350)
        # edible.direction_x = random.randrange(-1,1)
        # edible.direction_y = random.choice((3,5))
        edible.position.x = 200
        edible.direction_x = 1
        edible.direction_y = 1
        game_manager.add(edible)
        physics.wall_bouncing(edible)
        # i = 0
        if edible.position.x == 400:
            edible.direction_x = edible.direction_x * (-1)


    ## Update logic
    run()

    ## update graphics
    draw(screen)

    ## delay by frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()