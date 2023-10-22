from model import Particle, System
from view import view_update

import pygame
import sys
from pygame.locals import *
pygame.init()

# Editable variables
num_particles = 1000


# Animation setup
FPS = 60
clock = pygame.time.Clock()


def first_spawn(system):
    # spawn num_particles particles
    for _ in range(num_particles):
        system.particles_active.append(Particle())


def update_model(system):
    for particle in system.particles_active:
        particle.move()
        if particle.is_caught():
            system.particles_caught.append(particle)
    system.particles_active = [
        particle for particle in system.particles_active if not particle.is_caught()]


def main():
    """Main loop"""

    planet = System()
    first_spawn(planet)

    looping = True
    while looping:
        clock.tick(FPS)
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Processing
        update_model(planet)

        # Render
        view_update(planet)


main()
