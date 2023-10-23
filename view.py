import pygame
from model import planet_radius

# Screen Setup
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = WINDOW_WIDTH/2
view_percent = .7
view_buffer = (1-view_percent)/2
particle_size = 4


# Animation Setup
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Planets + Particles')


def projection(coordinate):
    theta = coordinate[1]
    phi = coordinate[2]
    return (((phi/360)*view_percent + view_buffer)*WINDOW_WIDTH,
            ((theta/180)*view_percent + view_buffer)*WINDOW_HEIGHT)


def view_update(system):
    pygame.draw.rect(WINDOW, 'gray', pygame.Rect(
        WINDOW_WIDTH*view_buffer, WINDOW_HEIGHT*view_buffer,
        WINDOW_WIDTH*view_percent, WINDOW_HEIGHT*view_percent))

    if 0 <= system.sun_pos <= 180:
        pygame.draw.rect(WINDOW, 'yellow', pygame.Rect(
            WINDOW_WIDTH*(view_buffer + system.sun_pos*view_percent/360),
            WINDOW_HEIGHT*view_buffer,
            WINDOW_WIDTH*view_percent/2,
            WINDOW_HEIGHT*view_percent
        ))
    else:
        pygame.draw.rect(WINDOW, 'yellow', pygame.Rect(
            WINDOW_WIDTH*view_buffer, WINDOW_HEIGHT*view_buffer,
            WINDOW_WIDTH*((system.sun_pos-180)*view_percent/360),
            WINDOW_HEIGHT*view_percent
        ))
        pygame.draw.rect(WINDOW, 'yellow', pygame.Rect(
            WINDOW_WIDTH*(view_buffer + system.sun_pos/360*view_percent),
            WINDOW_HEIGHT*view_buffer,
            WINDOW_WIDTH*((360-system.sun_pos)*view_percent/360),
            WINDOW_HEIGHT*view_percent
        ))

    for particle in system.particles_active:
        if particle.hop == None:
            color = 'black'
        else:
            # Percentage convered
            f = min(
                1, max(0, (particle.coordinates[0] - planet_radius)/300000))

            # No Pheromone: 135 116 72 -> Fully Covered: 97 65 15
            color = (255, 255*f, 255*f)
        projected_coord = projection(particle.coordinates)
        pygame.draw.rect(WINDOW, color, pygame.Rect(
            projected_coord[0], projected_coord[1], particle_size, particle_size))

    for particle in system.particles_caught:
        projected_coord = projection(particle.coordinates)
        pygame.draw.rect(WINDOW, 'blue', pygame.Rect(
            projected_coord[0], projected_coord[1], particle_size, particle_size))

    pygame.display.update()
