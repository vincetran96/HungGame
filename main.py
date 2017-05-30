import pygame
from inputmanager import *
from gamemanager import *
from player import *
from background import *
from constraints import *
from edible import *
from nonedible import *
import random
from physics import *
from sfx_mixer import *


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hung Game")

    return screen

def run():
    game_manager.run()
    physics.check_hit_wall()
    physics.check_hit_ground()
    # sound_manager.play_sounds()

def draw(screen):
    screen.fill((0, 0, 0))
    game_manager.draw(screen)

def mix():
    #game_manager.mix()
    pass

screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
player = Player()
game_manager.add(player)
player.constraints = Constraints(0,800,0,600)

#test_sound = pygame.mixer.Sound("resources/player/sounds/")
#sound_manager.add(test_sound)

loop = True

i = 30
while loop:
    events = pygame.event.get()

    # Handle QUIT event
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

    input_manager.run(events)
    i -= 1
    if i == 0:
        eat = NonEdible()
        eat.position.x = random.randrange(50, 750)
        game_manager.add(eat)
        physics.add_fruits(eat)
        i = 30

    ## Update logic
    run()

    ## update graphics
    draw(screen)

    ## play sfx
    mix()

    ## delay by frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()