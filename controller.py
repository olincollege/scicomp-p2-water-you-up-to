from model import System
from view import view_update

import pygame
import sys
from pygame.locals import *
pygame.init()


# Animation setup
FPS = 60
clock = pygame.time.Clock()


def main():
    """Main loop"""

    planet = System()
    planet.first_spawn()

    looping = True
    while looping:
        clock.tick(FPS)
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        planet.update_model()

        # Render
        view_update(planet)


main()
