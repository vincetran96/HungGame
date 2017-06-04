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

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hung Game")
    return screen
#bay mất cmn music là sao zạ?
#đang tìm hiểu nguyên nhân
def run():
    game_manager.run()
    physics.check_hit_wall()
    physics.check_hit_ground()

def mix():
    game_manager.mix()

def draw(screen):
    screen.fill((0, 0, 0))
    game_manager.draw(screen)

def draw_text( text, size, color, x, y): #For score and player's status
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
player = Player()
game_manager.add(player)
player.constraints = Constraints(0,800,0,600)


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
        eat.position.x = random.randrange(50, 750)
        non_eat.position.x = random.randrange(50, 750)

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
    draw(screen)
    draw_text(str(player.score), 40, (255, 255, 255), 400, 20)
    ## play sfx
    mix()

    ## delay by frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()