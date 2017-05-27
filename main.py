import pygame
from inputmanager import *
from gamemanager import *
from player import *
from background import *
from constraints import *

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

while loop:
    events = pygame.event.get()

    # Handle QUIT event
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

    input_manager.run(events)

    ## Update logic
    run()

    ## update graphics
    draw(screen)

    ## delay by frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()