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
from levels import *

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((game.screen_width, game.screen_height))
    pygame.display.set_caption(game.game_title)
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

screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
player = Player()
game_manager.add(player)
player.constraints = Constraints(0, game.screen_width, 0, game.screen_height)


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
        eat, non_eat = Edible(), NonEdible()

    if i == 120:
        lion = Lion ()
        print ("Spawn Lion!")
        game_manager.add (lion)
        lion.position.x = 50
        lion.position.y = 520
        # trap = Trap()
        # trap.position.x = random.randrange (50, 750)

    ## Update logic
    run()

    ## update graphics
    draw_screen(screen)
    game.draw_text(screen, str(player.score), 40, (255, 255, 255), 400, 20 )

    ## play sfx
    mix()

    ## delay by frame rate
    pygame.display.flip()
    clock.tick(game.FPS)

pygame.quit()