import pygame
from inputmanager import *
from gamemanager import *


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("HungGame")
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
player.constraints = Constraints(0, 600, 0, 800)
game_manager.add(player)
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