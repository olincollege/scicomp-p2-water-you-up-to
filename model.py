import numpy as np
import random

# Sim-Defining Editable Variables

planet_radius = 2439  # km, Mercury
surface_gravity = 3.705  # km/s^2, Mercury
temp_in_light = 500  # K, can go back and make more complex later
rotational_speed = 10.892  # km/hr, planetary rotation
radius_poles = 300  # km, location of stable regions

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


def inside_sunlight(coords):
    # checks if coordinates are inside the current circle of sunlight
    return ()


def inside_pole(coords):
    # checks if coordinates are inside the poles of the planet
    return ()


class System:

    def __init__(self):
        self.particles_active = []
        self.particles_caught = []


class Particle:

    def __init__(self):
        self.coordinates = random_polar_coords()
        self.hop = None

    def move(self):
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
        else:
            # elif inside_sunlight(self.coordinates):
            self.hop = Hop(self.coordinates)

    def is_caught(self):
        # return T/F depending on if in polar region
        return inside_pole(self.coordinates)


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
        self.current_coords[2] = self.current_coords[2] + 1
