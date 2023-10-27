import pygame
import pygame.freetype
from model import planet_radius
import numpy as np
pygame.init()

# Screen Setup
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = WINDOW_WIDTH/2
view_percent = .7
view_buffer = (1-view_percent)/2
particle_size = 4


# Animation Setup
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Planets + Particles')

# Aesthetics

colors = {
    "light-gray": (237, 237, 237),
    "dark-gray": (100, 100, 100),
    "yellow": (255, 250, 162),
    "red": (223, 152, 82),
    "blue": (121, 158, 223),
    "green": (36, 158, 31)
}
title_font = pygame.freetype.Font("Kanit-Bold.ttf", 48)
cap_font = pygame.freetype.Font("Kanit-Bold.ttf", 24)


def projection(coordinate):
    theta = coordinate[1]
    phi = coordinate[2]
    return (((phi/360)*view_percent + view_buffer)*WINDOW_WIDTH,
            ((theta/180)*view_percent + view_buffer)*WINDOW_HEIGHT)


def view_update(system):
    # Draw the surface of the planet
    pygame.draw.rect(WINDOW, colors['light-gray'], pygame.Rect(
        WINDOW_WIDTH*view_buffer, WINDOW_HEIGHT*view_buffer,
        WINDOW_WIDTH*view_percent, WINDOW_HEIGHT*view_percent))

    draw_sun(system)

    for particle in system.particles_active:
        draw_active_particle(particle)

    for particle in system.particles_caught:
        draw_caught_particle(particle)

    for particle in system.particles_lost:
        draw_lost_particle(particle)

    draw_border()

    pygame.display.update()


def init_background():
    """Draws the stars + words in the background"""
    img = pygame.image.load("img/space.jpg").convert()
    imageWidth, imageHeight = img.get_size()
    tilesX = int(np.ceil(WINDOW_WIDTH / imageWidth))
    tilesY = int(np.ceil(WINDOW_HEIGHT / imageHeight))

    # Loop over both and blit accordingly
    for x in range(tilesX):
        for y in range(tilesY):
            WINDOW.blit(img, (.8*x * imageWidth, .8*y * imageHeight))

    # Draw the title + legend
    draw_title()
    draw_legend()


def draw_title():
    # Border to background
    # pygame.draw.rect(WINDOW, colors['dark-gray'], pygame.Rect(
    #     WINDOW_WIDTH/2 - 400 - particle_size*2, WINDOW_HEIGHT *
    #     view_buffer/2 - 30 - particle_size*2,
    #     800 + particle_size*4, 60 + particle_size*4))

    # # Background
    # pygame.draw.rect(WINDOW, colors['light-gray'], pygame.Rect(
    #     WINDOW_WIDTH/2 - 400, WINDOW_HEIGHT*view_buffer/2 - 30,
    #     800, 60))

    title_font.render_to(WINDOW, (WINDOW_WIDTH/2 - 300,
                                  WINDOW_HEIGHT*view_buffer/2-15), 'Water Molecules on Mercury', colors['light-gray'])


def draw_legend():
    # # Border to background
    # pygame.draw.rect(WINDOW, colors['dark-gray'], pygame.Rect(
    #     WINDOW_WIDTH/2 - 200 - particle_size, WINDOW_HEIGHT *
    #     (1 - view_buffer/2) - 50 - particle_size,
    #     400 + particle_size*2, 40 + particle_size*2))

    # # Background
    # pygame.draw.rect(WINDOW, colors['light-gray'], pygame.Rect(
    #     WINDOW_WIDTH/2 - 200, WINDOW_HEIGHT*(1-view_buffer/2) - 50,
    #     400, 40))

    cap_font.render_to(WINDOW, (WINDOW_WIDTH/2 - 150,
                                WINDOW_HEIGHT*(1-view_buffer/2)-10), 'Active', colors['green'])
    cap_font.render_to(WINDOW, (WINDOW_WIDTH/2 - 30,
                                WINDOW_HEIGHT*(1-view_buffer/2)-10), 'Lost', colors['red'])
    cap_font.render_to(WINDOW, (WINDOW_WIDTH/2 + 70,
                                WINDOW_HEIGHT*(1-view_buffer/2)-10), 'Caught', colors['blue'])


def draw_border():
    pygame.draw.rect(WINDOW, colors['dark-gray'], pygame.Rect(
        WINDOW_WIDTH*view_buffer - particle_size *
        2, WINDOW_HEIGHT*view_buffer - particle_size*2,
        particle_size*2, WINDOW_HEIGHT*view_percent + (particle_size*4)))

    pygame.draw.rect(WINDOW, colors['dark-gray'], pygame.Rect(
        WINDOW_WIDTH*(1-view_buffer), WINDOW_HEIGHT *
        view_buffer - particle_size*2,
        particle_size*2, WINDOW_HEIGHT*view_percent + (particle_size*4)))

    pygame.draw.rect(WINDOW, colors['dark-gray'], pygame.Rect(
        WINDOW_WIDTH*view_buffer - particle_size*2, WINDOW_HEIGHT *
        view_buffer - particle_size*2,
        WINDOW_WIDTH*view_percent + (particle_size*4), particle_size*2))

    pygame.draw.rect(WINDOW, colors['dark-gray'], pygame.Rect(
        WINDOW_WIDTH*view_buffer - particle_size*2, WINDOW_HEIGHT *
        (1-view_buffer),
        WINDOW_WIDTH*view_percent + (particle_size*4), particle_size*2))


def draw_sun(system):
    if 0 <= system.sun_pos <= 180:
        pygame.draw.rect(WINDOW, colors['yellow'], pygame.Rect(
            WINDOW_WIDTH*(view_buffer + system.sun_pos*view_percent/360),
            WINDOW_HEIGHT*view_buffer,
            WINDOW_WIDTH*view_percent/2,
            WINDOW_HEIGHT*view_percent
        ))
    else:
        pygame.draw.rect(WINDOW, colors['yellow'], pygame.Rect(
            WINDOW_WIDTH*view_buffer, WINDOW_HEIGHT*view_buffer,
            WINDOW_WIDTH*((system.sun_pos-180)*view_percent/360),
            WINDOW_HEIGHT*view_percent
        ))
        pygame.draw.rect(WINDOW, colors['yellow'], pygame.Rect(
            WINDOW_WIDTH*(view_buffer + system.sun_pos/360*view_percent),
            WINDOW_HEIGHT*view_buffer,
            WINDOW_WIDTH*((360-system.sun_pos)*view_percent/360),
            WINDOW_HEIGHT*view_percent
        ))


def draw_active_particle(particle):
    if particle.hop == None:
        particle_height = particle_size
    else:
        # Height off the ground as a function of highest possible height
        # Size of drawn particle grows to up to double
        particle_height = particle_size * (1 + min(
            1, max(0, (particle.coordinates[0] - planet_radius)/300000)))

    projected_coord = projection(particle.coordinates)
    pygame.draw.rect(WINDOW, colors['green'], pygame.Rect(
        projected_coord[0], projected_coord[1], particle_height, particle_height))


def draw_caught_particle(particle):
    projected_coord = projection(particle.coordinates)
    pygame.draw.rect(WINDOW, colors['blue'], pygame.Rect(
        projected_coord[0], projected_coord[1], particle_size, particle_size))


def draw_lost_particle(particle):
    projected_coord = projection(particle.coordinates)
    pygame.draw.rect(WINDOW, colors['red'], pygame.Rect(
        projected_coord[0], projected_coord[1], particle_size, particle_size))
