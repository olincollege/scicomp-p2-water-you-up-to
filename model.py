import numpy as np
import random

# Sim-Defining Editable Variables

planet_radius = 2439  # km, Mercury
surface_gravity = 3.705  # km/s^2, Mercury
temp_in_light = 500  # K, can go back and make more complex later
rotational_speed = 10.892  # km/hr, planetary rotation
radius_poles = 300  # km, location of stable regions
num_particles = 1000
polar_deg = 10

# Setup (Pre-defined/Empty Variables, etc)


# escape velocity
# time spent during hop
# photodissociation time scale


def random_polar_coords():
    """
    Generates uniformly distributed random polar coordinates on the surface of the sphere

    Returns:
        list: The random coordinate, in the form [radius, polar angle, azimuth angle]
    """
    rand_u = random.random()
    rand_v = random.random()
    phi = 360*rand_u
    # Unclusters the final distibution from around the poles
    # theta = np.arccos(2*rand_v - 1)
    theta = 180*rand_v
    return [planet_radius, theta, phi]


class System:

    def __init__(self):
        self.particles_active = []
        self.particles_caught = []
        self.sun_pos = 0  # phi of the furthestmost clockwise edge of sunlight

    def update_model(self):
        for particle in self.particles_active:
            particle.move(self.sun_pos)
            if particle.is_caught():
                self.particles_caught.append(particle)
        self.particles_active = [
            particle for particle in self.particles_active if not particle.is_caught()]
        self.sun_pos += 1
        self.sun_pos = self.sun_pos % 360

    def first_spawn(self):
        # spawn num_particles particles
        for _ in range(num_particles):
            self.particles_active.append(Particle())


class Particle:

    def __init__(self):
        self.coordinates = random_polar_coords()
        self.hop = None

    def move(self, sun_pos):
        # VERY clunky way to deal with a particle landing on the surface
        if self.coordinates[0] < planet_radius:
            # photodissociation would go here
            self.coordinates[0] = planet_radius
            self.hop = None

        # Continue current hop
        if self.hop != None:
            self.hop.move()
            self.coordinates = self.hop.current_coords
        # Or start a new one!
        elif self.inside_sunlight(sun_pos):
            self.hop = Hop(self.coordinates)

    def is_caught(self):
        if self.coordinates[1] > 180-polar_deg or self.coordinates[1] < polar_deg:
            return True
        return False

    def inside_sunlight(self, sun_pos):
        # checks if coordinates are inside the current area of sunlight
        if sun_pos <= self.coordinates[2] <= (sun_pos+180) % 360:
            return True
        return False


class Hop:

    def __init__(self, coords):
        # random angle to move in direction of
        self.current_coords = coords  # starting coords
        # starting angle of launch
        # self.current_velocity  # starting velocity
        # self.start_time  # starting time

    def move(self):
        # generate new position
        self.current_coords[1] = self.current_coords[1] + 1
        self.current_coords[2] = self.current_coords[2] + .2
        self.current_coords[2] = self.current_coords[2] % 360
