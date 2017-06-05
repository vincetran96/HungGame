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
from trap import *
from lion import *
from settings import *

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    return screen

pygame.mixer.init()
pygame.mixer.music.load("resources/music.mp3")
pygame.mixer.music.play(-1,0.0)

def run():
    game_manager.run()
    physics.check_hit_wall()
    physics.check_hit_ground()

def mix():
    game_manager.mix()

def draw_screen(screen):
    screen.fill((0, 0, 0))
    game_manager.draw(screen)

def check_lose():
    if player.missed_edibles >= 10:
        print ("NOOB")

screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
player = Player()
game_manager.add(player)
player.constraints = Constraints(0, WIDTH, 0, HEIGHT)

playing = True

i = 0
while playing:
    events = pygame.event.get()

    # Handle QUIT event
    for event in events:
        if event.type == pygame.QUIT:
            playing = False

    input_manager.run(events)
    i += 1
    if i % 90 == 0:
        #non_edible = Bird()
        #edible = Fly()
        trap = Trap ()
        game_manager.add (trap)
    # if i == 120:
    #     lion = Lion ()
    #     game_manager.add (lion)

    ## Update logic
    run()

    ## update graphics
    draw_screen(screen)
    draw_text(screen, str(player.score), 40, WHITE, WIDTH/2, 20 )

    ## play sfx
    mix()

    ## delay by frame rate
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()