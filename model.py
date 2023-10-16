import numpy as np
import random

# Sim-Defining Editable Variables

planet_radius = 2439 #km, Mercury
surface_gravity = 3705 #m/s^2, Mercury
temp_in_light = 500 #K, can go back and make more complex later
rotational_speed = 10.892 #km/hr, planetary rotation
radius_poles = 300 #km, location of stable regions
num_particles = 1000

# Setup (Pre-defined/Empty Variables, etc)

#escape velocity
#particles_active list
#particles_caught list
#time spent during hop
#photodissociation time scale

def random_polar_coords():
    """
    Generates uniformly distributed random polar coordinates on the surface of the sphere

    Returns:
        tuple: The random coordinate, in the form (radius, polar angle, azimuth angle)
    """
    rand_u = random.random()
    rand_v = random.random()
    phi = 2*np.pi*rand_u
    theta = np.arccos(2*rand_v - 1) #Unclusters the final distibution from around the poles
    return (planet_radius, theta, phi)


def inside_sunlight():
    #checks if coordinates are inside the current circle of sunlight
    return()

def inside_pole():
    # checks if 

class Particle:

    def __init__(self):
        self.coordinates = random_polar_coords()
        self.hop = None

    def move(self):
        if self.coordinates[0] <= planet_radius:
            self.coordinates[0] = planet_radius
            self.hop = None

        if self.hop != None:
            self.hop.move()
            self.coordinates = self.hop.current_pos()
        elif inside_sunlight(self.coordinates):
            self.hop = Hop()

    def is_caught(self):
        # return T/F depending on if in polar region

class Hop:

    def __init__(self):
        #random angle to move in direction of
        #starting position
        #starting angle of launch
        #starting velocity (start with "constant" based on temp, eventually random)
        #starting time

    def current_pos(self):
        #return current position

    def move(self):
        #generate new position

def first_spawn():
    #spawn num_particles particles


def projection(coordinate):
    #turn spherical coordinates into equidistant 2d projection
    #(maybe mercator projection eventually?? something funky with maps)


def update_model():
    #for particle in particles_active
        #particle.jump()
        #if particle.is_caught()
            #particles_caught.append(particle)
    #particles_active = all not is_caught

def main():
    #this will be in another file - going to animate with pygame :)


main()